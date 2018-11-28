#include<iostream>
#include<algorithm>
using namespace std;
struct WW
{
	double b,e,w;
}d[2005];
bool cmp1(WW  a, WW  c)
{
	return a.b<c.b;
}
bool cmp2(WW  a, WW  c)
{
	return a.w<c.w;
}
int main()
{
	int r,s,x,n,tt,t,i,now,nn;
	double ans,ttt;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		ans=0;
		scanf("%d%d%d%lf%d",&x,&s,&r,&ttt,&n);
		for(i=1;i<=n;i++)
		{
			scanf("%lf%lf%lf",&d[i].b,&d[i].e,&d[i].w);
			d[i].w+=s;
		}
		r-=s;
		sort(d+1,d+n+1,cmp1);
		nn=n;
		for(now=0,i=1;i<=n;i++)
		{
			if(d[i].b>d[i-1].e)
			{
				d[++nn].b=d[i-1].e;
				d[nn].e=d[i].b;
				d[nn].w=s;
			}
		}
		sort(d+1,d+nn+1,cmp1);
		if(d[nn].e!=x)
		{
			nn++;
			d[nn].b=d[nn-1].e;
			d[nn].e=x;
			d[nn].w=s;
		}
		for(i=0;i<=nn;i++)
		{
			d[i].e-=d[i].b;
		}
		sort(d+1,d+nn+1,cmp2);
		for(i=1;i<=nn&&ttt>0;i++)
		{
			if((d[i].e)/(d[i].w+r)<=ttt)
			{
				ttt-=(d[i].e)/(d[i].w+r);
				ans+=(d[i].e)/(d[i].w+r);
			}
			else
			{
				ans+=ttt;
				ans+=(d[i].e-ttt*(d[i].w+r))/d[i].w;
				ttt=-1;
			}
		}
		for(;i<=nn;i++)
		{
			ans+=(d[i].e)/(d[i].w);
		}
		printf("Case #%d: %f\n",tt,ans);
	}
	return 0;
}
