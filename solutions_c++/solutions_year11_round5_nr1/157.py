#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <math.h>
#include <string.h>
using namespace std;
const double E=1e-10;
struct cor
{
	double x,y;
};
struct data
{
	double x,y1,y2;
};
int nw,nl,nu,n;
cor lc[100];
cor uc[100];
data d[500];
int nd;
double caljiaoy(cor r,cor s,int x)
{
	return (x-r.x)*(s.y-r.y)/(s.x-r.x)+r.y;
}

int main()
{
	int tc,cas,i,j,k;
	freopen("A-large.in","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	freopen("output_la.txt","w",stdout);
	scanf("%d",&tc);
	for (cas=1;cas<=tc;++cas)
	{
		scanf("%d%d%d%d",&nw,&nl,&nu,&n);
		for (i=0;i<nl;++i) scanf("%lf%lf", &lc[i].x,&lc[i].y);
		for (i=0;i<nu;++i) scanf("%lf%lf", &uc[i].x,&uc[i].y);
		i=1;
		j=1;
		nd=1;
		d[0].x=0;
		d[0].y1=lc[0].y;
		d[0].y2=uc[0].y;
		while (i<nl && j<nu)
		{
			if (fabs(lc[i].x-uc[j].x)>E)
			{
				if (lc[i].x>uc[j].x)
				{
					double y = caljiaoy(lc[i-1],lc[i],uc[j].x);
					d[nd].x=uc[j].x;
					d[nd].y1=y;
					d[nd++].y2=uc[j].y;
					++j;
				}
				else
				{
					double y=caljiaoy(uc[j-1],uc[j],lc[i].x);
					d[nd].x=lc[i].x;
					d[nd].y1=lc[i].y;
					d[nd++].y2=y;
					++i;
				}
			}
			else
			{
				d[nd].x=lc[i].x;
				d[nd].y1=lc[i].y;
				d[nd++].y2=uc[j].y;
				++i; ++j;
			}
		};
		double total_s=0, one, cur, next;
		for (i=0;i+1<nd;++i) total_s+=(d[i+1].x-d[i].x)*(d[i].y2-d[i].y1+d[i+1].y2-d[i+1].y1)/2;
		one=total_s/n;
		next=one;
		cur=0.0;
		i=0;
		printf("Case #%d:\n", cas);
		while (--n)
		{
			while (cur+(d[i+1].x-d[i].x)*(d[i].y2-d[i].y1+d[i+1].y2-d[i+1].y1)/2 < next)
			{
				cur+=(d[i+1].x-d[i].x)*(d[i].y2-d[i].y1+d[i+1].y2-d[i+1].y1)/2;
				++i;
			}
			double remv = next-cur;
			double a = d[i].y2-d[i].y1;
			double b = d[i+1].y2-d[i+1].y1;
			double h = d[i+1].x-d[i].x;
			double ra = (b-a)/h;
			double rb=2*a;
			double rc=-2*remv;
			double ansx=0;
			if (fabs(ra)<E)
			{
				ansx=-rc/rb;
			}
			else
			{
			double dt=sqrt(rb*rb-4*ra*rc);
			double x1=(-rb+dt)/(2*ra);
			double x2=(-rb-dt)/(2*ra);
			if (x1>-E&&x1<h+E) ansx=x1;
			else ansx=x2;
			}
			printf("%.12lf\n", d[i].x+ansx);
			next+=one;
			/*
			cor r1,r2,r3,r4;
			r1.x=d[i].x; r1.y=d[i].y1;
			r2.x=d[i+1].x; r1.y=d[i+1].y1;
			r3.x=d[i].x; r3.y=d[i].y2;
			r4.x=d[i+1].x; r4.y=d[i+1].y2;
			d[i].x=d[i].x+ansx;
			d[i].y1=caljiaoy(r1,r2,d[i].x+ansx);
			d[i].y2=caljiaoy(r3,r4,d[i].x+ansx);
			cur=0;
			*/
		}
	}
	return 0;
}