#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const int maxn=1005;
struct node
{
	double s,e;
	double sp;
}a[maxn];

bool cmp(node a,node b)
{
	if (a.sp<b.sp) return true;
	else if (a.sp==b.sp&&a.s<b.s) return true;
	else return false;
}

int main()
{
	int cas,ca;
	double len,l,s,r,sp;
	int n,i;
	double t1;
	double t;
	ca=0;
	double t2;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%lf",&len);
		scanf("%lf%lf%lf%d",&s,&r,&t,&n);
		t2=t;
		l=0;
		for (i=0;i<n;i++)
		{
			scanf("%lf%lf%lf",&a[i].s,&a[i].e,&a[i].sp);
			l+=a[i].e-a[i].s;
		}
		a[n].s=0;
		a[n].e=len-l;
		a[n].sp=0;
		n++;
		sort(a,a+n,cmp);
		l=0;
		t1=0;
		for (i=0;i<n;i++)
		{
			sp=r+a[i].sp;
			if ((a[i].e-a[i].s)/sp<=t)
			{
				t-=(a[i].e-a[i].s)/sp;
			}
			else
			{
				t1=((a[i].e-a[i].s)-t*sp)/(s+a[i].sp);
				t=0;
				break;
			}
		}
		i++;
		while (i<n)
		{
			sp=s+a[i].sp;
			t1+=(a[i].e-a[i].s)/sp;
			i++;
		}
		ca++;
		printf("Case #%d: %.9lf\n",ca,t1+t2-t);
	}
		


return 0;
}