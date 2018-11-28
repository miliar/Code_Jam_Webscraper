#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN = 105;
const double EPS = 1e-8;
struct Tpoint{
	double x,y;
}pl[MAXN],pu[MAXN];
int w,u,l,g;
double y1,y2;
double Calc(const Tpoint&a,const Tpoint&b,double f,double r)
{
	if (f>b.x || r<a.x) return 0;
	f = max(f,a.x);
	r = min(r,b.x);
	y1 = (b.y-a.y)/(b.x-a.x)*(f-a.x)+a.y;
	y2 = (b.y-a.y)/(b.x-a.x)*(r-a.x)+a.y;
	return (r-f)*(y1+y2)/2;
}
double GetS(double f,double r)
{
	double res=0;
	for (int i=1;i<l;i++)
		res += Calc(pl[i],pl[i+1],f,r);
	for (int i=1;i<u;i++)
		res -= Calc(pu[i],pu[i+1],f,r);
	return -res;
}
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d%d%d%d",&w,&l,&u,&g);
		for (int i=1;i<=l;i++)
			scanf("%lf%lf",&pl[i].x,&pl[i].y);
		for (int i=1;i<=u;i++)
			scanf("%lf%lf",&pu[i].x,&pu[i].y);
		double totS=GetS(0,w);

		double last=0,one=totS/g;
		last=min(pl[1].x,pu[1].x);
		double mw;
		mw=max(pu[l].x,pl[l].x);
		printf("Case #%d:\n",tcase);
		for (int i=1;i<g;i++)
		{
			double f=last,r,mid;
			r=mw;
			while (f+EPS<r)
			{
				mid = (f+r)/2;
				if (GetS(last,mid)>one) r=mid;
						else f=mid;
			}
			last=(f+r)/2;
			printf("%.6f\n",(f+r)/2);
		}
	}
	return 0;
}
