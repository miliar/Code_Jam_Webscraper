#include<iostream>
#include<string>
using namespace std;
#define eps 1e-8
struct pt
{
	int d,v;
	bool operator <(const pt & rhs)const
	{
		return d<rhs.d;
	}
};
pt a[500];
int n;
double d;
bool judge(double x)
{
	double now;
	int i,j;
	now=-1e14;
	for(i=1;i<=n;i++)
		for(j=1;j<=a[i].v;j++)
	{
			double l=a[i].d;
			if (now+d>l+x) return false;
			if (l-x>=d+now) now=l-x;
			else now=now+d;
	}
}
int main()
{
	int tcase,cas,i;
	double l,r,mid;
	freopen("Bs.in","r",stdin);
	freopen("Bs.out","w",stdout);
	scanf("%d",&tcase);
	for(cas=1;cas<=tcase;cas++)
	{
		scanf("%d%lf",&n,&d);
	    for(i=1;i<=n;i++)
		 scanf("%d%d",&a[i].d,&a[i].v);
		l=0;r=1e13;
		while(l+eps<r)
		{
            mid=(l+r)/2;
            if (judge(mid)) {r=mid-eps;}
			else l=mid+eps;
		}
		printf("Case #%d: %.8lf\n",cas,l);
	}
}