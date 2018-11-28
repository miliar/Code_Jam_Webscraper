#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

#define inf 1<<20

int cost[2000],must[2000];
int dp[10000][15];

int query(int node,int b,int e,int taken)
{
	if(b==e)
	{
		if(taken>=must[b])
			return 0;
		return inf;
	}
	if(dp[node][taken]!=-1)
		return dp[node][taken];
	dp[node][taken]=cost[node]+query(2*node,b,(b+e)/2,taken+1)+query(2*node+1,(b+e)/2+1,e,taken+1);
	int k=query(2*node,b,(b+e)/2,taken)+query(2*node+1,(b+e)/2+1,e,taken);
	if(k<dp[node][taken])
		dp[node][taken]=k;
	return dp[node][taken];
}

int main()
{
	freopen("world.in","r",stdin);
	freopen("world.out","w",stdout);
	int t,cs,n;
	scanf("%d",&t);
	for(cs=0;cs<t;cs++)
	{
		scanf("%d",&n);
		int i,j,k=1<<n;
		for(i=0;i<k;i++)
			scanf("%d",&must[i]),must[i]=n-must[i];
		k/=2;
		j=0;
		while(k)
		{
			int now=j;
			for(i=0;i<k;i++)
				scanf("%d",&cost[j]),j++;
			reverse(cost+now,cost+j);
			k/=2;
		}
		cost[j]=inf;
		reverse(cost,cost+(1<<n));
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",cs+1,query(1,0,(1<<n)-1,0));
	}
	return 0;
}