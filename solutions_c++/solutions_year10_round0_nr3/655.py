#include <cstdio>
#include <cstring>
const int MAXN = 1005;
int T;
int R, K, N, Q;
long long G[2*MAXN];
long long cost[MAXN], next[MAXN];
int cycle, cycleStart;
long long cycleCost;
int main()
{
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int R, K, N;
		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%lld", &G[i]);
			G[i+N] = G[i];
		}
		memset(cost, 0, sizeof cost);
		Q = cycle = 0;
		int u = 0;
		while (true)
		{
			long long cur = 0;
			for (int i = 0; i <= N; i++)
			{
				if (i==N || cur + G[u+i] > K)
				{
					next[u] = (u+i) % N;
					cost[u] = cur;
					break;
				}
				else
					cur += G[u+i];
			}
			u = next[u];
			if (cost[u]) // cycle
			{
				int v = u;
				cycleCost = 0;
				cycleStart = u;
				do
				{
					cycle++;
					cycleCost += cost[v];
					v = next[v];
				} while (v != u);
				break;
			}
		}
		u = 0;
		long long res = 0;
		while (R)
		{
			if (u == cycleStart && R >= cycle)
			{
				res += R/cycle * cycleCost;
				R %= cycle;
			}
			else
			{
				res += cost[u];
				u = next[u];
				R--;
			}
		}
		printf("Case #%d: %lld\n", t, res);
	}
}
