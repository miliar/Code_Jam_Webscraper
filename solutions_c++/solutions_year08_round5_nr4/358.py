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

#define MOD 10007

using namespace std;

int dp[100][100];

int is_in(int x, int y, int w, int h)
{
	return 0 <= x && x < w && 0 <= y && y < h;
}

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		memset(dp, 0, 100 * 100 * 4);
		int w, h, r;
		cin >> w >> h >> r;
		dp[0][0] = 1;
		for(int i = 0; i < r; ++i)
		{
			int x, y;
			cin >> x >> y;
			dp[x - 1][y - 1] = -1;
		}
		for(int y = 0; y < h; y += 2)
		{
			for(int x = 0; x + y / 2 < w && x / 2 + y < h; x += 2) if(x || y)
			{
				int add = 0;
				if(is_in(x + y / 2 - 2, y + x / 2 - 1, w, h) && dp[x + y / 2 - 2][y + x / 2 - 1] != -1)
					add += dp[x + y / 2 - 2][y + x / 2 - 1];
				if(is_in(x + y / 2 - 1, y + x / 2 - 2, w, h) && dp[x + y / 2 - 1][y + x / 2 - 2] != -1)
					add += dp[x + y / 2 - 1][y + x / 2 - 2];
				if(dp[x + y / 2][y + x / 2] != -1) dp[x + y / 2][y + x / 2] = add % MOD;
			}
		}
		printf("Case #%d: ", t);
		printf("%d\n", dp[w - 1][h - 1]);
	}
	return 0;
}