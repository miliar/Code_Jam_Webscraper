#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
char sets[100][100];
int dp[100][2025];
int M, N;
void dfs(int k, int d, int src, int des, int num)
{
	if(d >= N)
	{
		dp[k+1][des] = max(dp[k][src] + num, dp[k+1][des]);
	}
	else
	{
		if(d == 0 && !(src & (1<<(d+1))) && sets[k][d] == '.')
		{
			dfs(k, d+1, src, des | (1<<d), num+1);
		}
		else if(d >= 1 && d <= N-2 && !(des & (1<<(d-1))) && !(src & (1<<(d-1))) && !(src & (1<<(d+1))) && sets[k][d] == '.')
		{
			dfs(k, d+1, src, des | (1<<d), num+1);
		}
		else if(d > N-2 && !(src & (1<<(d-1))) && !(des & (1<<(d-1))) && sets[k][d] == '.')
		{
			dfs(k, d+1, src, des | (1<<d), num+1);
		}
		dfs(k, d+1, src, des, num);
	}
}
int main()
{
	freopen("c.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	//ifstream cin("c.txt");
	//ofstream cout("out.txt");
	int T;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++)
	{
		printf("Case #%d: ", Case);
		
		scanf("%d%d ", &M, &N);
		for(int i = 0; i < M; i++)
			gets(sets[i]);
		memset(dp, 0, sizeof(dp));
		//dp[0][0] = 0;
		for(int i = 0; i <= M; i ++)
			//for(int j = 0; j <= N; j )
				for(int j = 0; j < (1 << N); j++)
				//if(dp[i][j])
				{
					dfs(i, 0, j, 0, 0);
				}
		int ans = 0;
	
		for(int i = 0; i < (1<<N); i++)
			if(dp[M][i] > ans)
				ans = dp[M][i];
		printf("%d\n", ans);
	}
}