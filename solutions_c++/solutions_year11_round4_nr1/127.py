#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <string.h>
using namespace std;
struct data
{
	int l;
	int s;
};
data a[10000];
bool cmp(const data &r, const data &s)
{
	return r.s<s.s;
}
int main()
{
	int tc,cas;
	int ln,sw,sr,ti,n,m,p,i;
	double rem,ans;
	freopen("A-large.in","r",stdin);
	freopen("output_la.txt","w",stdout);
	scanf("%d",&tc);
	
	for (cas=1;cas<=tc;++cas)
	{
		m=0;
		p=0;
		scanf("%d%d%d%d%d",&ln,&sw,&sr,&ti,&n);
		sr-=sw;
		for (i=0;i<n;++i)
		{
			int st,en,sp;
			scanf("%d%d%d",&st,&en,&sp);
			if (st > p) {a[m].l = st-p; a[m++].s=sw;}
			a[m].l=en-st; a[m++].s=sp+sw;
			p=en;
		}
		if (ln>p) {a[m].l=ln-p; a[m++].s = sw;}
		sort(a,a+m,cmp);
		rem=ti;
		ans=0;
		for (i=0;i<m;++i)
		{
			if (rem*(sr+a[i].s)>=a[i].l)
			{
				double cost = double(a[i].l)/double(sr+a[i].s);
				rem-=cost;
				ans+=cost;
			}
			else
			{
				double cost = double(a[i].l-rem*(sr+a[i].s))/double(a[i].s) + rem;
				rem=0;
				ans+=cost;
			}
		}
		printf("Case #%d: %.12lf\n", cas, ans);
	}
	return 0;
}