#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <functional>
#include <cmath>
using namespace std;

struct vect
{
	double x,y,z;
	vect(double x,double y,double z)
	{
		this->x=x;
		this->y=y;
		this->z=z;
	}
	double len()
	{
		return sqrt(x*x+y*y+z*z);
	}
	vect operator*(double c)
	{
		return vect(x*c,y*c,z*c);
	}
};
struct point
{
	double x,y,z;
	point(double x,double y,double z)
	{
		this->x=x;
		this->y=y;
		this->z=z;
	}
	point &operator+=(vect &v)
	{
		x+=v.x;
		y+=v.y;
		z+=v.z;
		return *this;
	}
};
double skal_mul(vect &v1,vect &v2)
{
	return v1.x*v2.x+v1.y*v2.y+v1.z*v2.z;
}
double rast(point &p1,point &p2)
{
	double x=p1.x-p2.x,y=p1.y-p2.y,z=p1.z-p2.z;
	return sqrt(x*x+y*y+z*z);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n;
		scanf("%d",&n);
		int x=0,y=0,z=0,vx=0,vy=0,vz=0;
		for(int i=0;i<n;i++)
		{
			int tx,ty,tz,tvx,tvy,tvz;
			scanf("%d%d%d%d%d%d",&tx,&ty,&tz,&tvx,&tvy,&tvz);
			x+=tx;
			y+=ty;
			z+=tz;
			vx+=tvx;
			vy+=tvy;
			vz+=tvz;
		}
		point p((double)x/n,(double)y/n,(double)z/n);
		vect v((double)vx/n,(double)vy/n,(double)vz/n);
		vect v2(-p.x,-p.y,-p.z);
		double len=skal_mul(v,v2)/v.len();
		double tm;
		if(len>0)
			tm=len/v.len();
		else
			tm=0;
		p+=v*tm;
		printf("Case #%d: %.10lf %.10lf\n",t,rast(p,point(0,0,0)),tm);
	}
	//
	return 0;
}