#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <map>
#include <string.h>
#include <string>
#include <assert.h>
#include <math.h>
using namespace std;
#define EPS 1e-20
bool inCircle(double x,double y,double r)
{
	return x*x+y*y<r*r+EPS;
}
double circleIntegral(double t1,double t2,double r)
{
	assert(t1<t2+EPS);
	double x1=asin(t1/r);
	double x2=asin(t2/r);
	assert(x1<x2+EPS);
	double re=r*r/2;
	re*=(x2-x1)+sin(x2)*cos(x2)-sin(x1)*cos(x1);
	assert(re>-EPS);
	return re;
}
double getArea(double x,double y,double d,double r)
{
	if(!inCircle(x,y,r))return 0.0;
	double re=0.0;
	if(inCircle(x+d,y+d,r))return d*d;
	if(inCircle(x+d,y,r)&&inCircle(x,y+d,r))
	{
		assert(r*r+EPS>(y+d)*(y+d));
		double x1=sqrt(r*r-(y+d)*(y+d));
		re+=(x1-x)*d;
		assert(x1<x+d+EPS);
		re+=circleIntegral(x1,x+d,r);
		re-=y*(x+d-x1);
//		puts("1");
	}
	else if(inCircle(x,y+d,r))
	{
		assert(r*r+EPS>(y+d)*(y+d));
		double x1=sqrt(r*r-(y+d)*(y+d));
		re+=(x1-x)*d;
		assert(x1<x+d+EPS);
		assert(x1<r+EPS);
		assert(r*r+EPS>y*y);
		double x2=sqrt(r*r-y*y);
		re+=circleIntegral(x1,x2,r);
		re-=y*(x2-x1);
//		puts("2");
	}
	else if(inCircle(x+d,y,r))
	{
		re+=circleIntegral(x,x+d,r);
		re-=d*y;
//		puts("3");
	}
	else
	{
		assert(r*r+EPS>y*y);
		double x2=sqrt(r*r-y*y);
		re+=circleIntegral(x,x2,r);
		re-=(x2-x)*y;
//		puts("4");
	}
//	printf("%lf %lf %lf %lf %lf\n",x,y,d,r,re);
	assert(re>-EPS&&re<d*d+EPS);
	return re;
}
int main()
{
	int t,ca;
	//printf("%.10lf\n",4.0*getArea(0,0,1.0,1.0));
	for(scanf("%d",&t),ca=1;ca<=t;ca++)
	{
		double ans=0.0;
		double f,R,t,r,g;
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		if(g-2.0*f<EPS)
		{
			ans=0.0;
			goto end;
		}
		//r+=f;
		for(double x=r;x<R-t-f+EPS;x+=g+2*r)
		{
			for(double y=r;;y+=g+2*r)
			{
				if(!inCircle(x+f,y+f,R-t-f))
					break;
				double aa=getArea(x+f,y+f,g-2.0*f,R-t-f);
				ans+=aa;
				//printf("%lf %lf %lf %lf=%lf\n",x,y,g-2.0*f,R-t-f,aa);
			}
		}
		ans/=acos(-1.0)*R*R/4;
end:
		printf("Case #%d: %.8lf\n",ca,1.0-ans);
	}
	return 0;
}
