#include <stdio.h>
#include <math.h>

#define PI 3.1415926

double f,R,t,r,g;
double k,d,l,s;
double dd;

inline double OK(double x,double y)
{
	return x*x+y*y<dd;
}

inline double S(double a,double b,double c)
{
	return ((dd*asin(b/d)+b*sqrt(dd-b*b))-((dd*asin(a/d)+a*sqrt(dd-a*a))))/2-(b-a)*c;
}

int main() 
{
	int n,x;
	double i,j,a,b;

	scanf("%d",&n);
	for(x=1;x<=n;x++)
	{
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		d=R-t-f;
		dd=d*d;
		l=g+r+r;
		k=g-f-f;
		s=0.0;

		for(i=r+f;i<d;i+=l)
		{
			for(j=r+f;j<d;j+=l)
			{
				if(!OK(i,j)) continue;

				if(OK(i+k,j+k))
				{
					s+=k*k;
				}
				else if(OK(i+k,j) && OK(i,j+k))
				{
					a=sqrt(dd-(j+k)*(j+k));
					b=sqrt(dd-(i+k)*(i+k));
					s+=k*k-(i+k-a)*(j+k-b)+S(a,i+k,b);
				}
				else if(OK(i+k,j))
				{
					s+=S(i,i+k,j);
				}
				else if(OK(i,j+k))
				{
					s+=S(j,j+k,i);
				}
				else
				{
					s+=S(i,sqrt(dd-j*j),j);
				}
			}
		}
		printf("Case #%d: %.06lf\n",x,1-(s*4)/(R*R*PI));
	}

	return 0;
}
