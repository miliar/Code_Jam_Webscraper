#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

#define q(z) ((z)*(z))

#define MAX 100

typedef pair<double,double> pdd;

pdd vert[MAX];


double arcar(double a, double r)
{
	if(a>r)
		return 0;
	return (acos(a/r)*q(r))/2-(a*sqrt(q(r)-q(a)))/2;
}


/*
 * area limitada pela reta y=b e y=0, pelas retas x=a.first e x=a.second e pela circunferencia x2+y2=r2
 */
double limar(pdd a, double b,double r) 
{
	double xint;
	xint=q(r)-q(b);
	if(xint<0)
		xint=0;
	else
		xint=sqrt(xint);
	if(xint>a.second)
		xint=a.second;
	else if(xint<a.first)
		xint=a.first;
	return (xint-a.first)*b+arcar(xint,r)-arcar(a.second,r);
}


double intar(pdd a, pdd b,double r)
{
	return limar(a,max(b.first,b.second),r)-limar(a,min(b.first,b.second),r);
}

double ocarea(double R, double r, double f, double t, double g)
{
	int i,j;
	double ret=0;
	int n;
	vert[0].first=0;
	vert[0].second=r+f;
	for(n=1;vert[n-1].second+g-2*f<R-t-f;++n)
	{
		vert[n].first=vert[n-1].second+g-2*f;
		vert[n].second=vert[n].first+2*r+2*f;
	}
	for(i=0;i<n;++i)
		ret+=arcar(vert[i].first,R-t-f)-arcar(vert[i].second,R-t-f);
	ret*=2;
	for(i=0;i<n;++i)
		for(j=0;j<n;++j)
			ret-=intar(vert[i],vert[j],R-t-f);
	ret*=4;
	ret+=M_PI*(q(R)-q(R-t-f));
	return ret;
}

int main()
{
	double R,r,t,f,g;
	int cnt;
	int ncase;
	double resp;
	scanf("%d",&ncase);
	for(cnt=1;cnt<=ncase;++cnt)
	{
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		resp=ocarea(R,r,f,t,g)/(M_PI*q(R));
		printf("Case #%d: %.6lf\n",cnt,resp);
	}
	return 0;
}

