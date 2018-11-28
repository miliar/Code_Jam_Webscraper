#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;
#define MIN(a,b) ( (a) < (b) ? (a) : (b) )
#define MAX(a,b) ( (a) > (b) ? (a) : (b) )
#define sqr(a) ((a)*(a))
#define PI acos(-1.0)
#define eps (1e-9)
double c[1001];
double cc[1001];
double x[1001];
double R;
double He(double x1,double y1,double x2,double y2,double x3,double y3)
{
	double l12=sqrt(sqr(x1-x2)+sqr(y1-y2));
	double l13=sqrt(sqr(x1-x3)+sqr(y1-y3));
	double l23=sqrt(sqr(x2-x3)+sqr(y2-y3));
	double p=0.5*(l12+l13+l23);
	double S=sqrt(p*(p-l12))*sqrt((p-l13)*(p-l23));
	return S;
}
double Se(double x1,double y1,double x2,double y2)
{
	double l=sqrt(sqr(x1-x2)+sqr(y1-y2));
	l/=2.0;
	double a=2.0*asin(l/R);
	return 0.5*R*R*(a-sin(a));
}
int main()
{
	int N;
	
	int ind=0;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	cin>>N;
	while(N)
	{
		N--;
		ind++;
		double t,r,f,g;
		cin>>f>>R>>t>>r>>g;
		double S=PI*R*R;
		R-=t;
		R-=f;
		r+=f;
		g-=2*f;
		double res=1.0;
		if(g<eps)
		{
			printf("Case #%d: %.7f\n",ind,res);
			continue;
		}
		double xx=-r-g;
		int i,j;
		for(i=0;i<1001;i++)
		{
			xx+=r+r+g;
			x[i]=xx;
			if(sqr(xx)>sqr(R)-eps)c[i]=0;
			else c[i]=sqrt(sqr(R)-sqr(xx));

			if(sqr(xx+g)>sqr(R)-eps)cc[i]=0;
			else cc[i]=sqrt(sqr(R)-sqr(xx+g));
		}
		double Sd=0;
		for(i=0;x[i]<R;i++)
		{
			for(j=0;j<=i;j++)
			{
				if(x[i]>c[j])break;
				if(x[i]+g<cc[j])
				{
					Sd+=g*g;
					if(i!=j)Sd+=g*g;
					continue;
				}
				double Spot=0;
				double x1,x2,x3,x4,y1,y2,y3,y4;
				double x0=x[i];
				double y0=x[j];
				if(x[i]<cc[j] && x[i]+g<c[j])
				{
					x1=x[i]+g;
					y1=x[j];
					x2=x1;
					y2=cc[i];
					x3=cc[j];
					y3=x[j]+g;
					x4=x0;
					y4=y3;
					Spot=He(x0,y0,x1,y1,x2,y2)+He(x0,y0,x2,y2,x3,y3)+He(x0,y0,x3,y3,x4,y4)+Se(x2,y2,x3,y3);
				}
				else
				{
					if(x[i]<cc[j])
					{
						x1=c[j];
						y1=y0;
						x2=cc[j];
						y2=x[j]+g;
						x3=x0;
						y3=y2;
						Spot=He(x0,y0,x1,y1,x2,y2)+He(x0,y0,x2,y2,x3,y3)+Se(x1,y1,x2,y2);
					}
					else
					{
						x1=c[j];
						y1=y0;
						x2=x0;
						y2=c[i];
						Spot=He(x0,y0,x1,y1,x2,y2)+Se(x1,y1,x2,y2);
					}
				}
				if(i!=j)Spot*=2.0;
				Sd+=Spot;
			}
		}
		Sd*=4.0;
		res=(S-Sd)/S;
		printf("Case #%d: %.7f\n",ind,res);
	}
	return 0;
}