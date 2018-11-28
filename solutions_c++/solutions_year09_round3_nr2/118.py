#include <iostream>
#include <cmath>

using namespace std;
#define sqr(x) (x*x)

struct tfly{
	double x, y, z, vx, vy, vz;
	void init()
	{
		cin>>x>>y>>z>>vx>>vy>>vz;
	}
};
tfly a[1000], c;
double dmin, tmin;
int n;

void init()
{
	cin>>n;
	for (int i=0;i<n;i++)
	{
		a[i].init();
	}
}

void calc()
{
	double d, t=-1;
	c.x = c.y = c.z = c.vx = c.vy = c.vz = 0;
	for (int i=0;i<n;i++)
	{
		c.x+=a[i].x;
		c.y+=a[i].y;
		c.z+=a[i].z;
		c.vx+=a[i].vx;
		c.vz+=a[i].vz;
		c.vy+=a[i].vy;
	}
	c.x/=n;
	c.y/=n;
	c.z/=n;
	c.vx/=n;
	c.vy/=n;
	c.vz/=n;
	
	double x, y, z;
	x = -(c.y*c.vz-c.z*c.vy);
	y = c.x*c.vz-c.z*c.vx;
	z = -(c.x*c.vy-c.y*c.vx);
	tmin = -1;
	if ((sqr(c.vx)+sqr(c.vy)+sqr(c.vz))>0)
	{
		dmin = sqrt((sqr(x)+sqr(y)+sqr(z))/(sqr(c.vx)+sqr(c.vy)+sqr(c.vz)));
		tmin = (-c.x*c.vx-c.y*c.vy-c.z*c.vz)/(sqr(c.vx)+sqr(c.vy)+sqr(c.vz));
	}
	if (tmin<0)
	{
		tmin = 0;
		dmin = sqrt(sqr(c.x)+sqr(c.y)+sqr(c.z));
	}
}
int main()
{
	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		init();
		calc();
		printf("Case #%d: %.8lf %.8lf\n",i+1,dmin,tmin);
	}
	return 0;
}
