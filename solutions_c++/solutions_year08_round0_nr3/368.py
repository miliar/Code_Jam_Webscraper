#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <utility>
using namespace std;
bool inside(double b1,double b2,double i)
{
	if (b1-b2>-1e-10)
		if ((i-b2>-1e-10) && (b1-i>-1e-10))
			return true;
	if (b2-b1>-1e-10)
		if ((i-b1>-1e-10) && (b2-i>-1e-10))
			return true;
	return false;
}
bool bsize(double left,double bottom,double r)
{
	return r*r-(left*left+bottom*bottom)>-1e-10;
}
pair<double,double> getcp(pair<double,double> a,pair<double,double> b,double R)
{
	double A,B,C;
	A=b.first-a.first;
	B=a.second-b.second;
	C=a.second*(b.first-a.first)-a.first*(b.second-a.second);
	pair<double,double> t1,t2;
	if (A>-1e-10 && A<1e-10)
	{
		t1.second=-sqrt(-C*C+B*B*R*R)/B;
		t1.first=C/B;
		t2.second=sqrt(-C*C+B*B*R*R)/B;
		t2.first=C/B;
	}
	else
	{
		t1.second=(C-(B*B*C)/(A*A+B*B)-B*sqrt(-A*A*C*C+A*A*A*A*R*R+A*A*B*B*R*R)/(A*A+B*B))/A;
		t1.first=(B*C+sqrt(-A*A*C*C+A*A*A*A*R*R+A*A*B*B*R*R))/(A*A+B*B);
		t2.second=(C-(B*B*C)/(A*A+B*B)+B*sqrt(-A*A*C*C+A*A*A*A*R*R+A*A*B*B*R*R)/(A*A+B*B))/A;
		t2.first=(B*C-sqrt(-A*A*C*C+A*A*A*A*R*R+A*A*B*B*R*R))/(A*A+B*B);
	}
	if (inside(a.first,b.first,t1.first) && inside(a.second,b.second,t1.second))
		return t1;
	else
		return t2;
}
double getrads(pair<double,double> a,pair<double,double> b,double r)
{
	double rad1,rad2;
	rad1=atan2(a.second,a.first);
	rad2=atan2(b.second,b.first);
	return r*r/2.0*(rad1-rad2)-fabs(a.second*b.first-b.second*a.first)/2.0;
}
double csize(double left,double bottom,double height,double width,double r)
{
	double top=bottom+height;
	double right=left+width;
	bool o1,o2,o3;
	o1=bsize(left,top,r);
	o2=bsize(right,bottom,r);
	o3=bsize(right,top,r);
	pair<double,double> pt1,pt2;
	if (!o1) if (!o2)
	{
		/*
		o1---------o3
		|           |
		|           |
		cut1        |
		|           |
		+---cut2---o2
		*/
		pt1=getcp(make_pair(left,bottom),make_pair(left,top),r);
		pt2=getcp(make_pair(left,bottom),make_pair(right,bottom),r);
		return getrads(pt1,pt2,r)
			+(pt1.second-bottom)*(pt2.first-left)/2.0;
	}
	else
	{
		/*
		o1---------o3
		|           |
		|           |
		cut1     cut2
		|           |
		+----------o2
		*/
		pt1=getcp(make_pair(left,bottom),make_pair(left,top),r);
		pt2=getcp(make_pair(right,bottom),make_pair(right,top),r);
		return getrads(pt1,pt2,r)
			+(pt1.second-bottom+pt2.second-bottom)*width/2.0;
	}
	else if (!o2)
	{
		/*
		o1--cut1---o3
		|           |
		|           |
		|           |
		|           |
		+---cut2---o2
		*/
		pt1=getcp(make_pair(left,top),make_pair(right,top),r);
		pt2=getcp(make_pair(left,bottom),make_pair(right,bottom),r);
		return getrads(pt1,pt2,r)
			+(pt1.first-left+pt2.first-left)*height/2.0;
	} else if (!o3)
	{
		/*
		o1--cut1---o3
		|           |
		|        cut2
		|           |
		|           |
		+----------o2
		*/
		pt1=getcp(make_pair(left,top),make_pair(right,top),r);
		pt2=getcp(make_pair(right,bottom),make_pair(right,top),r);
		return getrads(pt1,pt2,r)
			+(pt2.second-bottom)*width+(width+pt1.first-left)*(top-pt2.second)/2.0;
	}
	else
	{
		return height*width;
	}
}
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	int total,T;
	scanf("%d",&total);
	T=total;
	while (total--)
	{
		printf("Case #%d: ",T-total);
		double f,R,t,r,g,tsiz;
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		t+=f;
		g-=2.0*f;
		r+=f;
		if (t-R>-1e-10)
		{
			printf("%.6lf",1.0);
			continue;
		}
		if (g<1e-10)
		{
			printf("%.6lf",1.0);
			continue;
		}
		tsiz=M_PI*R*R;
		R-=t; //Now R represents inner radius
		if (r-R>-1e-10)
		{
			printf("%.6lf",1.0);
			continue;
		}
		double osz=0.0,dy=r,dx;
		while (bsize(r,dy,R))
		{
			dx=r;
			while (bsize(dx,dy,R))
			{
				double tmp=csize(dx,dy,g,g,R);
				//printf("%lf %lf: %lf\n",dx,dy,tmp);
				osz+=csize(dx,dy,g,g,R);
				dx+=2.0*r+g;
			}
			dy+=2.0*r+g;
		}
		printf("%.6lf\n",1.0-osz*4.0/tsiz);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
