#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <set>
#include <ctime>
#include <algorithm>
#define min(a,b)	((a)<(b)?(a):(b))
#define max(a,b)	((a)>(b)?(a):(b))
#define abs(a)	((a)<0?-(a):(a))
#define inf 214748364
#define pi 3.141592653589793
using namespace std;
typedef long long ll;

const ll maxn = 10001;
struct tinfo
{
	ll x,y,r,no;
}	g[maxn];
ll n;
ll tim;
ll w,h;

bool cmp(const tinfo a,const tinfo b)
{
	return a.r>b.r;
}

bool cmp2(const tinfo a,const tinfo b)
{
	return a.no<b.no;
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	#endif
	scanf("%I64d",&tim);
	for(ll tt=1;tt<=tim;++tt)
	{
		printf("Case #%I64d: ",tt);
		scanf("%I64d%I64d%I64d",&n,&w,&h);
		for(ll i=1;i<=n;++i)
			scanf("%I64d",&g[i].r),g[i].no=i;
		sort(g+1,g+n+1,cmp);
		for(ll i=1;i<=n;++i)
		{
			ll l = g[i-1].x+g[i-1].r;
			ll r = l+g[i].r*2;
			if(l+g[i].r>w)
				l=-g[i].r,r=g[i].r;
			if(i==1)
				l=-g[i].r,r=g[i].r;
			ll ma = -g[i].r;
			for(ll j=1;j<i;++j)
			if(g[j].x-g[j].r<r&&l<g[j].x+g[j].r)
				ma = max(ma,g[j].y+g[j].r);
			g[i].x=l+g[i].r,g[i].y=ma+g[i].r;
//			if(y[i]>h)			i++,i--;
		}
		sort(g+1,g+n+1,cmp2);
		for(int i=1;i<=n;++i)
			printf("%I64d %I64d ",g[i].x,g[i].y);
		/*
		for(ll i=1;i<=n;++i)
		{
			if(x[i]<0||x[i]>=w||y[i]<0||y[i]>=h)
				i++,i--;
			for(ll j=1;j<=n;++j)
			if(i!=j)
			{
				if(x[i]-g[i]<x[j]+g[j]&&x[j]-g[j]<x[i]+g[i])
				if(y[i]-g[i]<y[j]+g[j]&&y[j]-g[j]<y[i]+g[i])
					i++,i--;
			}
		}
		*/
		printf("\n");
	}
	return 0;
}

