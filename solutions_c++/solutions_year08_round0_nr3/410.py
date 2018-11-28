#include<iostream>
#include<math.h>
using namespace std;
const double pi=acos(-1);
double ex=1e-10;
double s;
int cnt;
double mefun(double x1,double y1,double x2,double y2,double r)
{
	return asin(fabs(x1*y2-x2*y1)/r/r)*r*r/2-0.5*fabs(x1*y2-x2*y1);
}
double fun(double x1,double x2,double y1,double y2,double r)
{
	if(r>=sqrt(x2*x2+y2*y2))
	{
		cnt++;
		return 0;
	}
	if(r<=sqrt(x1*x1+y1*y1))
		return 0;
	double t1=sqrt(x2*x2+y1*y1);
	double t2=sqrt(x1*x1+y2*y2);
	double a,b;
	if(r<=t1&&r<=t2)
	{
		a=sqrt(r*r-x1*x1);
		b=sqrt(r*r-y1*y1);
		return .5*(a-y1)*(b-x1)+mefun(x1,a,b,y1,r);
	}
	if(r<=t1)
	{
		a=sqrt(r*r-y1*y1);
		b=sqrt(r*r-y2*y2);
		return mefun(a,y1,b,y2,r)+.5*(a+b-x1-x1)*(y2-y1);
	}
	if(r<=t2)
	{
		a=sqrt(r*r-x1*x1);
		b=sqrt(r*r-x2*x2);
		return mefun(x1,a,x2,b,r)+.5*(a-y1-y1+b)*(y2-y1);
	}

		a=sqrt(r*r-x2*x2);
		b=sqrt(r*r-y2*y2);
		return mefun(x2,a,b,y2,r)+(y2-y1)*(b-x1)+(x2-b)*(y2-y1+a-y1)*.5;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int ca;
	scanf("%d",&ca);
	double  f,R,t,r,g;
	int tca=0;
	while(tca++<ca)
	{
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		if(g-2*f<=0)
		{
			printf("Case #%d: 1.00000000\n",tca);
			continue;
		}
		cnt=0;
		s=(g-2*f)*(g-2*f);
		double area=pi*R*R;
		double rr=R-t-f;
		int i,j,k;
		double x1,y1,x2,y2;
		double a,b,a1,b1;
		double ans=0;
		for(i=0;;i++)
		{
			a=r+(g+2*r)*i+f;
			a1=g+r+(g+2*r)*i-f;
			if(a>rr+g)break;
			for(j=0;;j++)
			{
				b=r+(g+2*r)*j+f;
				b1=g+r+(g+2*r)*j-f;
				if(b>=rr+g)break;
				ans+=fun(a,a1,b,b1,rr);//cout<<"___"<<fun(a,a1,b,b1,rr)<<endl;
			}
		}
		ans+=s*cnt;
		printf("Case #%d: %.10lf\n",tca,1-4*ans/area);
	}
}
