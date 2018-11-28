#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <deque>

using namespace std;

int m[40000];
int cost[40000];
int p;
long long res[40000][11];
long long inf = 1000000000;

void solve(int i)
{
	for (int c = 0; c <= p; ++c)
		res[i][c] = inf;
	for (int a = 0; a <= p; ++a)
	{
		for (int b = 0; b <= p; ++b)
		{
			int c = max(a, b);
			res[i][c] = min(res[i][c], res[i * 2][a] + res[i * 2 + 1][b]);
			res[i][c] = min(res[i][c], inf);
			if (c > 0)
			{
				res[i][c - 1] = min(res[i][c - 1], res[i * 2][a] + res[i * 2 + 1][b] + cost[i]);
				res[i][c - 1] = min(res[i][c - 1], inf);
			}
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		scanf("%d", &p);
		for (int i = 0; i < (1 << p); ++i)
			scanf("%d", &m[i + (1 << p)]);

		for (int j = p - 1; j >= 0; --j)
		{
			for (int i = 0; i < (1 << j); ++i)
				scanf("%d", &cost[i + (1 << j)]);
		}

		for (int i = 0; i < (1 << p); ++i)
		{
			for (int c = 0; c <= p; ++c)
				res[i + (1 << p)][c] = inf;
			res[i + (1 << p)][p - m[i + (1 << p)]] = 0;
		}
		for (int i = (1 << p) - 1; i > 0; --i)
			solve(i);

		printf("Case #%d: %lld\n", t + 1, res[1][0]);
	}

	return 0;
}