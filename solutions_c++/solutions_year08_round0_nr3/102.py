#include <iostream>
#include <math.h>
#include <string>
#include <assert.h>

using namespace std;

const double pi=acos(-1.0);

double L(double a,double r)
{
	if(a>=r)
		return pi*r*r;
	if(a<=-r)
		return 0;
	if(a>0)
		return L(r+1,r)-L(-a,r);
	double an=2*acos(-a/r);
	return an*r*r/2-r*r*sin(an)/2;
}

double T(double b,double r)
{
	return L(-b,r);
}

double LT(double a,double b,double r)
{
	if(a>0)
		return T(b,r)-LT(-a,b,r);
	if(b<0)
		return L(a,r)-LT(a,-b,r);
	double d=sqrt(a*a+b*b);
	if(d>r)
		return 0;
	double b1=sqrt(r*r-a*a);
	return (T(b,r)-T(b1,r))/2+a*(b1-b);
}

double LTRB(double x1,double y1,double x2,double y2,double r)
{
	return LT(x1,y1,r)+LT(x2,y2,r)-LT(x1,y2,r)-LT(x2,y1,r);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	cin>>n;
	int cnt;
	for(cnt=1;cnt<=n;cnt++)
	{
		double f,R,t,r,g;
		cin>>f>>R>>t>>r>>g;
		printf("Case #%d: ",cnt);
		if(2*f>=g)
		{
			printf("%.6lf\n",1.0);
			continue;
		}
		double d=g+2*r;
		double x1,x2;
		double sum=0;
		for(x1=r+f,x2=r+g-f;x1<=R-t;x1+=d,x2+=d)
		{
			double y1,y2;
			for(y1=r+f,y2=r+g-f;y1<=R-t;y1+=d,y2+=d)
			{
				assert(x1<=x2&&y1<=y2);
				sum+=LTRB(x1,y2,x2,y1,R-t-f);
			}
		}
		sum*=4;
		double s=pi*R*R;
		printf("%.6lf\n",1-sum/s);
	}
	return 0;
}