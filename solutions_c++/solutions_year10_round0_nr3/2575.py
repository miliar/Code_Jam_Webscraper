// GCJ2010_3.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<cstdio>
#include<memory>
#include <math.h>
using namespace std;
int per[1000];
long long dp[1000][1000];
int can[1000];
bool used[1000];
int tt[1000];
int ttp[1000];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,n,k,r;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;++i)
		{
			scanf("%d",&per[i]);
			dp[i][i] = per[i];
		}
		memset(can,-1,sizeof(can));
		for(int i=0;i<n;++i)
		{
			/*if(per[i] <= k) */can[i] = i;
			for(int j=(i+1)%n;j!=i;j=(j+1)%n)
			{
				int last = j-1;
				if(j == 0) last = n-1;
				dp[i][j] = dp[i][last] + per[j];
				if(dp[i][j] <= k) can[i] = j;
			}
		}
		
		memset(used,false,sizeof(used));
		int pos = 0;
		long long res = 0;
		int turn = 0;
		while(used[pos] == false)
		{
			used[pos] = true;
			/*if(can[pos] == -1)
			{
				pos++;
				continue;
			}*/
			int next = can[pos];
			ttp[pos] = res;
			res += dp[pos][next];
			turn++;
			tt[pos] = turn;
			pos = (next+1)%n;
			if(turn == r) break;
		}
		if(turn != r)
		{
			r -= turn;
			int xun = turn+1-tt[pos];
			long long base = res - ttp[pos];
			/*if(xun == 0)
			{
				int pa =0 ;
			}*/
			long long tttp = base*(r/xun);
			res += tttp;
			turn = r%xun;
			while(turn--)
			{
				if(can[pos] == -1)
				{
					pos++;
					continue;
				}
				int next = can[pos];
				res += dp[pos][next];
				pos = (next+1)%n;
			}
		}
		printf("Case #%d: %lld\n",x,res);
	}
	return 0;
}

