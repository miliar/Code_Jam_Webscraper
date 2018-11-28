#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

struct reco{
	double b,e,v;
}a[100000];

double s,t,r,x;
int n,tes;

bool cmp(reco a,reco b)
{
	return a.b<b.b;
}

bool cmp2(reco a,reco b)
{
	return a.v<b.v;
}


int main()
{
	//freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		printf("Case #%d: ",ttt);
		
		scanf("%lf%lf%lf%lf",&x,&s,&r,&t);
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%lf%lf%lf",&a[i].b,&a[i].e,&a[i].v);		
			a[i].v+=s;
		}
		
		sort(a+1,a+n+1,cmp);
		int nn=n;
		int pos=0;
		for (int i=1;i<=n;i++)
		{
			if (pos<a[i].b)
			{
				nn++; a[nn].b=pos; a[nn].e=a[i].b; a[nn].v=s;
			}
			pos=a[i].e;
		}
		if (pos<x) { nn++; a[nn].b=pos; a[nn].e=x; a[nn].v=s; }
		n=nn;
		sort(a+1,a+n+1,cmp2);
		double ans=0;
		for (int i=1;i<=n;i++) ans=ans+(a[i].e-a[i].b)/a[i].v;
		int i=1;
		while (t>0 && i<=n)
		{
			double nw=min(t,(a[i].e-a[i].b)/(a[i].v+r-s));
			t-=nw;
			ans=ans-(nw*(a[i].v+r-s)*(1/a[i].v-1/(a[i].v+r-s)));
			i++;
		}
		printf("%.10f\n",ans);
	}
}

