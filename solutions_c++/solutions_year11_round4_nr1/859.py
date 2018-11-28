#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <algorithm>


using namespace std;

struct test
{
	int b,e,w,l;
	double kl;
}tes[1005];

int cmp(test a,test b)
{
	return a.kl>b.kl;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outaL.txt","w",stdout);
	int cas=1;
	int T;scanf("%d",&T);
	while(T--)
	{
		int i,j;
		int x,s,r,t,n;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		double ans=0;
		int sun=x;
		for(i=0;i<n;++i)
		{
			scanf("%d%d%d",&tes[i].b,&tes[i].e,&tes[i].w);
			tes[i].l=tes[i].e-tes[i].b;
			sun-=tes[i].e-tes[i].b;
			tes[i].kl=(double)(tes[i].w+r)/(tes[i].w+s)-1.0;
		}
		tes[n].w=0;
		tes[n].kl=(double)r/s-1.0;
		tes[n].l=sun;n++;
		for(i=0;i<n;++i)
		{
			ans+=(double)tes[i].l/(s+tes[i].w);
		}
		//cout<<ans<<endl;
		sort(tes,tes+n,cmp);
		double tt=t;
		for(i=0;i<n;++i)
		{
			double tim=(double)tes[i].l/(r+tes[i].w);
			if(tim>tt)
			{
				
				ans-=tt*tes[i].kl;
				tt=0;
				break;
			}
			ans-=tim*tes[i].kl;
			tt-=tim;
		}
		printf("Case #%d: %.6f\n",cas++,ans);
	}
}