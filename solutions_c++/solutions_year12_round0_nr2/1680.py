#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

int x[150];
int dp[150][150];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tt, T;
	scanf("%d", &T);
	for (tt = 0; tt < T; ++tt)
	{
		int n, s, p;
		int i, j;
		scanf("%d%d%d", &n, &s, &p);
		for (i = 0; i < n; ++i)
			scanf("%d", &x[i]);
		dp[0][0] = 0;
		for (i = 1; i <= n; ++i)
		{
			for (j = 0; j <= i; ++j)
			{
				dp[i][j] = dp[i - 1][j] + int((x[i - 1] + 2)/3 >= p);
				if (x[i - 1] >= 2 && x[i - 1] <= 28 && j > 0)
					dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + int((1 + (x[i - 1] + 1)/3) >= p));
			}
		}
		printf("Case #%d: %d\n", tt + 1, dp[n][s]);
	}
	return 0;
}