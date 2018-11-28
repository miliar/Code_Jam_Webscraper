#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
struct Line
{
	int b,e,s;
} a[2010];
int T,x,s,r,t,n;
double ans;

bool cmp(Line p,Line q)
{
	return (p.s<q.s);
}

void calc()
{
	ans=0;
	int i;
	double xx=0;
	for (i=1;i<=n && ans<t;i++)
	{
		if ((a[i].e-a[i].b)*1.0/(a[i].s+r-s)+ans>t)
		{
			xx=(t-ans)*(a[i].s+r-s)+a[i].b;
			ans=t;
			ans+=(a[i].e-xx)*1.0/a[i].s;
			i++;
			break;
		}
		else
		{
			ans+=(a[i].e-a[i].b)*1.0/(a[i].s+r-s);
		}
	}
	for (;i<=n;i++)
	{
		ans+=(a[i].e-a[i].b)*1.0/a[i].s;
	}
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++)
	{
		a[0].e=0;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		if (tt==12)
			tt=tt;
		for (int i=1,j=1;i<=n;i++)
		{
			a[j].b=a[j-1].e;
			a[j].s=s;
			j++;
			scanf("%d%d%d",&a[j].b,&a[j].e,&a[j].s);
			a[j-1].e=a[j].b;
			a[j].s+=s;
			j++;
		}
		if (a[2*n].e<x)
		{
			a[2*n+1].b=a[2*n].e;
			a[2*n+1].e=x;
			a[2*n+1].s=s;
			n=2*n+1;
		}
		else n*=2;
		sort(a+1,a+n+1,cmp);
//		for (int i=1;i<=n;i++)
//			cout<<a[i].b<<" "<<a[i].e<<" "<<a[i].s<<endl;
		calc();
//		for (int i=1;i<=n;i++)
//			cout<<a[i].b<<" "<<a[i].e<<" "<<a[i].s<<endl;
		printf("Case #%d: %.8lf\n",tt,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
