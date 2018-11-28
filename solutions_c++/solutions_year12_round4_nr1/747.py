#include <stdio.h>
#include <algorithm>

using namespace std;

struct s
{
	long long d,l;
};

s arr[10003],temp;
long long dp[10003];

int main()
{
	freopen("a.txt","r",stdin);
	freopen("a.out","w",stdout);
	long long test,cas,n,i,j,D;
	scanf("%lld",&test);
	for (cas=1;cas<=test;cas++)
	{
		scanf("%lld",&n);
		for (i=0;i<n;i++) scanf("%lld%lld",&arr[i].d,&arr[i].l);
		scanf("%lld",&D);
		temp.d=D;
		temp.l=1e9;
		arr[n++]=temp;
		for (i=0;i<n;i++) dp[i]=-1;
		dp[0]=arr[0].d;

		for (i=1;i<n;i++)
		{
			for (j=0;j<i;j++)
			{
				if (dp[j]==-1) continue;
				if (arr[j].d+dp[j]<arr[i].d) continue;
				//req=min(dp[j],sqrt(arr[i].l*arr[i].l+(arr[i].d-arr[j].d)*(arr[i].d-arr[j].d)));
				if (dp[j]!=-1&&min(arr[i].d-arr[j].d,arr[i].l)>dp[i])
				{
					dp[i]=min(arr[i].d-arr[j].d,arr[i].l);
				}
			}
		}
		if (dp[n-1]!=-1) printf("Case #%lld: YES\n",cas);
		else printf("Case #%lld: NO\n",cas);
	}
	return 0;
}
