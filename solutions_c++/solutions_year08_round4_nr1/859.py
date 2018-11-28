#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <queue>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PARENT(i) ((i) >> 1)
#define LEFT(i) ((i) << 1)
#define RIGHT(i) (LEFT(i) + 1)
const int INF = 1000000;

int gate[10005];
int yl[10005];
int dp[10005][2];

inline void check(int& x)
{
	if (x > INF - 10) x = INF;
}

void Search(int n)
{
	if (dp[n][0] != -1) return;
	int l = LEFT(n), r = RIGHT(n);
	Search(l);
	Search(r);
	dp[n][1] = dp[n][0] = INF;
	if (gate[n] & 2)
	{
		int v = (yl[n] == 1);
		dp[n][1] = dp[l][1] + dp[r][1] + v;
		dp[n][0] = min(min(dp[l][1] + dp[r][0], dp[l][0] + dp[r][1]), dp[l][0] + dp[r][0]) + v;
		check(dp[n][1]);
		check(dp[n][0]);
	}
	if (gate[n] & 1)
	{
		int v = (yl[n] == 2);
		dp[n][1] = min(dp[n][1], min(dp[l][1] + dp[r][1], min(dp[l][1] + dp[r][0], dp[l][0] + dp[r][1])) + v);
		dp[n][0] = min(dp[n][0], dp[l][0] + dp[r][0] + v);
		check(dp[n][1]);
		check(dp[n][0]);
	}
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for (int i=0;i<tt;i++)
	{
		memset(dp, -1, sizeof(dp));
		int m, v;
		scanf("%d%d", &m, &v);
		for (int i=1;i<=(m-1)/2;i++)
		{
			int g, c;
			scanf("%d%d", &g, &c);
			yl[i] = gate[i] = g + 1;
			if (c == 1) gate[i] = 3;
		}
		for (int i=(m-1)/2+1;i<=m;i++)
		{
			scanf("%d", &gate[i]);
			dp[i][gate[i]] = 0;
			dp[i][1 - gate[i]] = INF;
		}
		Search(1);
		printf("Case #%d: ", i + 1);
		if (dp[1][v] == INF) printf("IMPOSSIBLE\n");
		else printf("%d\n", dp[1][v]);
	}
	return 0;
}