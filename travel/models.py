from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    price_estimate = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name
