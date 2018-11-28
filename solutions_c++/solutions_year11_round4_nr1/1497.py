#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
struct N
{
	double x,y,v;
}ww[1005];
bool cmp(const N a,const N b)
{
	return a.v<b.v;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Aout.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		int n,m;
		double v1,v2,ti;
		scanf("%d%lf%lf%lf%d",&n,&v1,&v2,&ti,&m);
		int i;
		for(i=0;i<m;i++)
			scanf("%lf%lf%lf",&ww[i].x,&ww[i].y,&ww[i].v);
		double sum=0,p=0;
		for(i=0;i<m;i++)
		{
			sum+=ww[i].x-p;
			p=ww[i].y;
		}
		sum+=n-p;
		sort(ww,ww+m,cmp);
		double ans=0;
		if(sum/v2>=ti)
		{
			ans=ti;
			ans+=(sum-v2*ti)/v1;
			for(i=0;i<m;i++)
				ans+=(ww[i].y-ww[i].x)/(ww[i].v+v1);
			printf("Case #%d: %.8f\n",cas,ans);
		}
		else
		{
			ans=sum/v2;
			double tmp=ti-ans,res;
			for(i=0;i<m;i++)
			{
				if(tmp>0)
				{
					res=tmp*(v2+ww[i].v);
					if(res>=ww[i].y-ww[i].x)
					{
						ans+=(ww[i].y-ww[i].x)/(v2+ww[i].v);
						tmp-=(ww[i].y-ww[i].x)/(v2+ww[i].v);
					}
					else
					{
						ans+=tmp;
						ans+=(ww[i].y-ww[i].x-tmp*(v2+ww[i].v))/(ww[i].v+v1);
						tmp=0;
					}
				}
				else
					ans+=(ww[i].y-ww[i].x)/(ww[i].v+v1);
			}
			printf("Case #%d: %.8f\n",cas,ans);
		}
	}
	return 0;
}
