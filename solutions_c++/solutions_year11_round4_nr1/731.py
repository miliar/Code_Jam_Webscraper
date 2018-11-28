#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
const int MAXN=2011;
const double o=1e-8;
struct walkway
{
	int b,e,w;
} a[MAXN];
int s,r,x, T,n,m;
double t;

void init()
{
	scanf("%d %d %d %lf",&x,&s,&r,&t);
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
		scanf("%d %d %d",&a[i].b,&a[i].e,&a[i].w);
}

bool cmp(walkway u,walkway v)
{
	return u.b<v.b;
}

bool cmp2(walkway u,walkway v)
{
	return u.w<v.w;
}

void work()
{
	sort(a+1,a+n+1,cmp);	
	a[0].e=a[0].b=0;	n++;	a[n].b=a[n].e=x;
	m=n;	
	for (int i=0;i<=n;i++)
		if (a[i+1].b>a[i].e)
		{
			m++;	a[m].b=a[i].e;	a[m].e=a[i+1].b;
			a[m].w=0;
		}
	sort(a+1,a+m+1,cmp2);
	double ans=0;
	for (int i=1;i<=m;i++)
	{
		if ((double)(a[i].e-a[i].b)/(a[i].w+r)<t+o)
		{
			ans+=double(a[i].e-a[i].b)/(a[i].w+r); t-=double(a[i].e-a[i].b)/(a[i].w+r);
		}
		else 
		{
			double tt=t+(a[i].e-a[i].b-t*(a[i].w+r))/(a[i].w+s);
			ans+=tt;	t=0;
		}
	}
	printf("%.9lf\n",ans);
}

int main()
{
	freopen("a.in","r",stdin);	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		init();
		work();
	}
	return 0;
}




