#include <stdio.h>
#include <algorithm>
using namespace std;
const int maxn=1100;
struct line
{
	double len,v;
	bool operator<(const line &a)const
	{
		return v<a.v;
	}
}l[maxn];
int main()
{
	freopen("1_large.in","r",stdin);
	freopen("1_large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		double x,s,r,t;
		int n;
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		r-=s;
		double sum=0,ans=0;
		for(int i=0;i<n;i++)
		{
			double b,e;
			scanf("%lf%lf%lf",&b,&e,&l[i].v);
			l[i].len=e-b;	
			sum+=l[i].len;
			l[i].v+=s;
		}
		l[n].len=x-sum;
		l[n].v=s;
		n++;
		sort(l,l+n);
		for(int i=0;i<n;i++)
		{
			ans+=l[i].len/l[i].v;
			double lin=min(t,l[i].len/(r+l[i].v));
			t-=lin;
			ans-=(r*lin)/l[i].v;
		}
		printf("Case #%d: %.9f\n",cas,ans);
	}
}
