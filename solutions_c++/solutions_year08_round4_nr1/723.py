#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<iostream>
#include<sstream>
#include<functional>
#include<map>
#include<set>

using namespace std;


int M,V;

int able[10002];
int val[10002];
int dp[10002][2];

int border;
/*
int dfs(int ind)
{
	if(ind >= border)
		return val[ind];
	
	int& ret = dp[ind];
	if(ret>=0)
		return ret;
	
	if(val[ind] == 1)
	{
		tmp |= hash[val[ind*2] & val[ind*2+1]]; 
		if(able[ind] == 1)
			tmp |= val[ind*2] | val[ind*2+1];

	}
	else
	{
		tmp |= hash[val[ind*2] | val[ind*2+1]];
		if(able[ind]==1)
			tmp |= hash[val[ind*2] & val[ind*2+1]];
	}
	if(able[ind])
	{
		
	}
}*/
int calc(int x, int y, int c)
{
	if(c==0)
		return x|y;
	else
		return x&y;
}

const int inf=1000000000;

void init()
{
	memset(able, -1, sizeof(able));
	memset(val , -1, sizeof(val));
	
	for(int i=0; i<=M; i++)
		dp[i][0]=dp[i][1]=inf;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		scanf("%d %d", &M, &V);
		init();
		int border=(M-1)/2;
		for(int i=1; i<=border; ++i)
		{
			scanf("%d%d", val+i, able+i);
		}
		for(int i=border+1; i<=M; i++)
		{
			scanf("%d", val+i);
			dp[i][val[i]]=0;
		//	dp[i][1-val[i]]=0;
		}
		for(int ind=border; ind>=1; ind--)
		{
			if(dp[ind*2][0]<inf)
			{
				if(dp[ind*2+1][0]<inf)
				{
					int tmp=dp[ind*2][0]+dp[ind*2+1][0];
					dp[ind][calc(0,0,val[ind])]=min(dp[ind][calc(0,0,val[ind])], tmp);
					if(able[ind])
						dp[ind][calc(0,0,1-val[ind])]=min(dp[ind][calc(0,0,1-val[ind])],tmp+1);
				}
				if(dp[ind*2+1][1]<inf)
				{
					int tmp=dp[ind<<1][0]+dp[ind*2+1][1];
					dp[ind][calc(0,1,val[ind])]=min(dp[ind][calc(0,1,val[ind])], tmp);
					if(able[ind])
						dp[ind][calc(0,1,1-val[ind])]=min(dp[ind][calc(0,1,1-val[ind])],tmp+1);
				}
			}
			if(dp[ind*2][1]<inf)
			{
				if(dp[ind*2+1][0]<inf)
				{
					int tmp=dp[ind*2][1]+dp[ind*2+1][0];
					dp[ind][calc(1,0,val[ind])]=min(dp[ind][calc(1,0,val[ind])], tmp);
					if(able[ind])
						dp[ind][calc(1,0,1-val[ind])]=min(dp[ind][calc(1,0,1-val[ind])],tmp+1);
				}
				if(dp[ind*2+1][1]<inf)
				{
					int tmp=dp[ind*2][1]+dp[ind*2+1][1];
					dp[ind][calc(1,1,val[ind])]=min(dp[ind][calc(1,1,val[ind])], tmp);
					if(able[ind])
						dp[ind][calc(1,1,1-val[ind])]=min(dp[ind][calc(1,1,1-val[ind])],tmp+1);
				}
			}
		}
		printf("Case #%d: ", c);
		if(dp[1][V]<inf)
		{
			printf("%d\n", dp[1][V]);
		}
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}