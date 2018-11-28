#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

int dp[10][1 << 10];
int room[10];

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int m, n;
		cin >> m >> n;
		for(int i = 0; i < m; ++i)
		{
			string str;
			cin >> str;
			for(int j = 0; j < n; ++j)
			{
				if(str[j] == '.') room[i] &= ~(1 << j);
				else room[i] |= 1 << j;
			}
		}
		memset(dp, 0, (1 << 10) * 10 * 4);
		int max_n = 0;
		for(int i = 0; i < m; ++i)
		{
			for(int j = 0; j < (1 << n); ++j) if((room[i] & j) == 0 && ((j >> 1) & j) == 0 && ((j << 1) & j) == 0)
			{
				int num = 0;
				for(int k = 0; j >> k; ++k) num += (j >> k) & 1;
				dp[i][j] = num;
				if(i)
				{
					int sup = ~((j << 1) | (j >> 1)) & ((1 << n) - 1), sub = sup;
					do
					{
						dp[i][j] = max(dp[i][j], dp[i - 1][sub] + num);
						sub = (sub - 1) & sup;
					}while (sub != sup);
				}
				max_n = max(max_n, dp[i][j]);
			}
		}
		printf("Case #%d: ", t);
		printf("%d\n", max_n);
	}
	return 0;
}