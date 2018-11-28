#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cstring>
#include<algorithm>
using namespace std;

int Case , TC = 1;
int P , num;
int M[1024];
int cost[1024];
long long dp[1024][2][15];

long long DP(int v , int k , int Count)
{
	if(v >= num)
	{
		if(k)
			Count--;
		if(Count < P - M[v - num])
			return (int)1e9;
		else
			return 0;
	}
	if(dp[v][k][Count] != -1) return dp[v][k][Count];
	dp[v][k][Count] = (int)1e9;
	
	dp[v][k][Count] = min( dp[v][k][Count] , DP(2*v , 0 , Count) + DP(2*v+1 , 0 , Count));
	dp[v][k][Count] = min( dp[v][k][Count] , DP(2*v , 1 , Count+1) + DP(2*v+1 , 0 , Count));
	dp[v][k][Count] = min( dp[v][k][Count] , DP(2*v , 0 , Count) + DP(2*v+1 , 1 , Count + 1));
	dp[v][k][Count] = min( dp[v][k][Count] , DP(2*v , 1 , Count+1) + DP(2*v+1 , 1 , Count + 1));
	if(k)
		dp[v][k][Count] += cost[v];
	return dp[v][k][Count];	
}
	
	

int main()
{
	int i;
	freopen("B-large(2).in","r",stdin);
	freopen("Output.txt","w",stdout);
	scanf("%d",&Case);
	for(;Case>0;Case--)
	{
		scanf("%d",&P);
		num = 1;
		for(i=0;i<P;i++) num*=2;
		for(i=0;i<num;i++)
		{
			scanf("%d",&M[i]);
		}
		int tmp = num/2;
		for(i=0;i<P;i++)
		{
			for(int j=0;j<tmp;j++)
			{
				scanf("%d",&cost[tmp+j]);
			}
			tmp/=2;
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %lld\n",TC++,min( DP(1,0,0) , DP(1,1,1)));			
	}
	return 0;
}
