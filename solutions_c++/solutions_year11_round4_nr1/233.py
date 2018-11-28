#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

struct T
{
	int b,e,w;
}a[3000];

bool operator <(T t1,T t2)
{
	return t1.b<t2.b;
}

struct TT
{
	double d;
	int s;
	bool r;
}b[3000];
int ts;

bool operator <(TT t1,TT t2)
{
	return t1.s<t2.s;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,i,n,x,s,r,m;
	double ans,t;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		for(i=0;i<n;i++)
			scanf("%d%d%d",&a[i].b,&a[i].e,&a[i].w);
		sort(a,a+n);
		m=n;
		for(i=0;i<n-1;i++)
			if(a[i].e!=a[i+1].b)
			{
				a[m].b=a[i].e;
				a[m].e=a[i+1].b;
				a[m].w=0;
				m++;
			}
		if(a[0].b!=0)
		{
			a[m].b=0;
			a[m].e=a[0].b;
			a[m].w=0;
			m++;
		}
		if(a[n-1].e!=x)
		{
			a[m].b=a[n-1].e;
			a[m].e=x;
			a[m].w=0;
			m++;
		}
		sort(a,a+m);
		n=m;
		for(i=0;i<n;i++)
		{
			b[i].d=a[i].e-a[i].b;
			b[i].s=a[i].w+s;
			b[i].r=0;
		}
		sort(b,b+n);
		ans=0;
		r-=s;
		for(i=0;i<n;i++)
			if(t*(r+b[i].s)>=b[i].d)
			{
				ans+=b[i].d/(r+b[i].s);
				t-=b[i].d/(r+b[i].s);
			}
			else
			{
				ans+=t;
				b[i].d-=t*(b[i].s+r);
				t=0;
				ans+=b[i].d/b[i].s;
			}
			printf("Case #%d: %.12lf\n",++ts,ans);
	}
	return 0;
}