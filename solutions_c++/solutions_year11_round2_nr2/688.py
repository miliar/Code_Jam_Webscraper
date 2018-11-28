#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
const int MAXN=200;
const double o=1e-9;
double d,a,x[MAXN],y[MAXN];
int c,t,n;

void init()
{
	scanf("%d %lf",&c,&d);	n=0;
	for (int i=1;i<=c;i++)	
	{
		double p;	int v;	scanf("%lf %d",&p,&v);
		while (v--) x[++n]=p;
	}
}
	
bool check(double m)
{
	memcpy(y,x,sizeof(y));
	y[1]-=m;
	for (int i=2;i<=n;i++)
	{
		if (y[i]<y[i-1]+d-m-o) return false;
		if (fabs(y[i]-(y[i-1]+d))<(m+o)) y[i]=y[i-1]+d;
		else y[i]-=m;
	}
	return true;
}

void binary_search()
{
	double l=0,r=d*n;
	while (r-l>1e-7)
	{
		double m=(l+r)/2;
		if (check(m)) r=m;	else l=m;
	}
	a=(l+r)/2;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (int test=1;test<=t;test++)
	{
		init();
		sort(x+1,x+n+1);
		binary_search();
		printf("Case #%d: %.7lf\n",test,a);
	}
	return 0;
}
	