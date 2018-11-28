#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
#define MOD 10007
int dp[1000][1000];
int uncan[1000][1000];
int offset[2][2] = {-2, -1, -1, -2};
int main()
{
	freopen("d.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	//ifstream cin("d.txt");
	//ofstream cout("out.txt");
	int T;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++)
	{
		printf("Case #%d: ", Case);
		int H, W, R;
		scanf("%d%d%d", &H, &W, &R);
		memset(dp, 0, sizeof(dp));
		memset(uncan, 0, sizeof(uncan));
		for(int i =0 ; i < R; i++)
		{
			int r, c;
			scanf("%d%d", &r, &c);
			uncan[r][c] = 1;
		}
		dp[1][1] = 1;
		for(int i = 1; i <= H; i ++)
		{
			for(int j = 1; j <= W; j++)
			{
				for(int k = 0; k < 2; k++)
				{
					int tx = i + offset[k][0];
					int ty = j + offset[k][1];
					if(tx >= 1 && ty >= 1 && uncan[tx][ty] == 0)
					{
						dp[i][j] = (dp[i][j] + dp[tx][ty]) % MOD;
					}
				}
			}
		}
		printf("%d\n", dp[H][W]);
	}
}