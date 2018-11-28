#include <math.h>
#include <stdio.h>
#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

double f,R,t,r,g,RR;
double ans,S,i,j;
	
double dis(double x,double y,double xx,double yy)
{return sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy));}
int sig(double a)
{ return fabs(a)<EPS ? 0 : (a>0?1:-1) ;}

double ss(double s,double e)
{
	return 	 e/2*sqrt(RR - e*e) + RR/2*asin(e/R)
			-s/2*sqrt(RR - s*s) - RR/2*asin(s/R);
}
double CulS1()
{
	double x = sqrt(RR - (j+g)*(j+g));
	return (x-i)*g + ss(x,i+g) - j*(i+g-x);
}

double CulS2()
{
	return ss(j,j+g) - g*i;
}

double CulS3()
{
	return ss(i,i+g) - g*j;
}

double CulS4()
{
	double x = sqrt(RR - j*j);
	return ss(i,x) - j*(x-i);
}

int main()
{
	freopen("C.out","w",stdout);
	int ttt,st;
	double ii,jj,s,rtc;
	scanf("%d",&st);
	for (ttt=0;ttt<st;++ttt)
	{
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		S = PI * R * R /4;
		r += f;
		g -= 2*f;
		R -= t+f;
		s = 0;
		RR=R*R;
		if (sig(g)<=0)
		{
			ans=1;
		}
		else
		{
			ii = 2*r+g;
			rtc = g*g;
			for (i=r;sig(i-R)<0;i+=ii)
			{
				for (j=r;sig(j-R)<0;j+=ii)
				{
					if (dis(i,j,0,0)>=R) break;
					if (dis(i+g,j+g,0,0)<=R)
					{//全在里面的情况 
						//printf("all in %lf\n",rtc);
						s += rtc;
					}
					else if (dis(i+g,j,0,0)<=R)
					{//右下在内 
						if (dis(i,j+g,0,0)<=R)
						{//左上在内 1 
							//printf("type 1 (%lf %lf) %lf\n",i,j,CulS1());
							s += CulS1();
						}
						else
						{//左上在外 3 
							//printf("type 3 (%lf %lf) %lf\n",i,j,CulS3());
							s += CulS3();
						}
					}
					else
					{//右下在外 
						if (dis(i,j+g,0,0)<=R)
						{//左上在内 2
							//printf("type 2 (%lf %lf) %lf\n",i,j,CulS2());
							s += CulS2();
						}
						else
						{//左上在外 4 
							//printf("type 4 (%lf %lf) %lf\n",i,j,CulS4());
							s += CulS4();
						}
					}
				}
			}
			ans = 1 - s/S;
		}
		printf("Case #%d: %.6lf\n",ttt+1,ans);
	}
	return 0;
}


