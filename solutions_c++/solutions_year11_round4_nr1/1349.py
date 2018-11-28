#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int N = 1000+10;
struct node
{
	int from,to;
	int E;
	bool operator<(const node &A)const
	{
		return E<A.E;
	}
}way[N];

int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	
	int cases;
	for(cases=1;cases<=T;cases++)
	{
		int x,s,r,t,n;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		double ans = 0;
		int i;
		double ts = x;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&way[i].from,&way[i].to,&way[i].E);
			ts=ts-(way[i].to-way[i].from);	
		}
		sort(way,way+n);
        int wi = 0;
        double left = t;
		if(left>0)
		{
			double lneed = ts/r;
			if(lneed<left)
			{
				ans=ans+lneed;
				left-=lneed;
			}
			else
			{
				ans = ans+left+(ts-r*left)/s;
			    left=-1;
			}
		}else
			ans = ans+ts/s;
		while(wi<n)
		{
			
			double curlen = way[wi].to-way[wi].from;
            double need;
			if(left>0)
			{
				need = (curlen)/(r+way[wi].E);
				if(need>left)
				{
					need = left+(curlen-left*(r+way[wi].E))/(s+way[wi].E);
					left = -1;
				}
				else
					left-=need;
			}else
				need = (curlen)/(s+way[wi].E);
			ans+=need;
			
			wi++;
		}
		printf("Case #%d: %.7lf\n",cases,ans);
	}
	return 0;
}