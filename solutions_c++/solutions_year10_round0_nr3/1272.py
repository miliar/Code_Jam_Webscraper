#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>

const int MAXN = 1000;

int g[MAXN];
int next[MAXN];
int money[MAXN];
long long lastMoney[MAXN];
int lastStep[MAXN];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		memset(lastStep, -1, sizeof(lastStep));
		memset(lastMoney, -1, sizeof(lastMoney));
		for (int j = 0; j < n; j++)
			scanf("%d", &g[j]);

		int curGroup = 1 % n;
		int curPeople = g[0];
		for (int j = 0; j < n; j++)
		{
			if (j != 0) curPeople -= g[j - 1];
			while (!curPeople || (curGroup != j && curPeople + g[curGroup] <= k))
			{
				curPeople += g[curGroup];
				curGroup = (curGroup + 1) % n;
			}
			next[j] = curGroup;
			money[j] = curPeople;
		}

		int place = 0;
		long long res = 0;
		for (int j = 0; j < r; j++)
		{
			if (lastStep[place] == -1)
			{
				lastStep[place] = j;
				lastMoney[place] = res;
			} else {
				// got a cycle
				int len = j - lastStep[place];
				long long weight = res - lastMoney[place];
				int cycleNum = (r - j) / len;
				res += cycleNum * weight;
				j += len * cycleNum;
				if (j == r) break;
			}
			res += money[place];
			place = next[place];
		}

		printf("Case #%d: %lld\n", i, res);
	}
	return 0;
}