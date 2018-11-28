#include <cstdio>
#include <cstring>
#include <cstdlib>

const int maxn = 100;
const int maxv = 256;

int cost[maxv];
int a[maxn];
int opt[maxv];
int now[maxv];

int cd, ci, m, n;

int main()
{
	int testnumber, testcount;
	
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d%d%d", &cd, &ci, &m, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		
		for (int i = 0; i <= m; i++)
			cost[i] = 0;
		for (int i = m + 1; i < maxv; i++)
		{
			int t = i - m;
			cost[i] = cost[t] + ci;
			if (m == 0) cost[i] = 0x70000000;
		}

		for (int i = 0; i < maxv; i++)
			now[i] = 0;
		int min = 0x7fffffff;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < maxv; j++)
			{
				opt[j] = now[j] + abs(j - a[i]);
				if (opt[j] + cd * (n - i - 1) < min) min = opt[j] + cd * (n - i - 1);
			}
			for (int j = 0; j < maxv; j++)
			{
				now[j] += cd;
				for (int k = 0; k < maxv; k++)
					if (opt[k] + cost[abs(k - j)] < now[j]) now[j] = opt[k] + cost[abs(k - j)];
			}
		}
		printf("Case #%d: %d\n", testcount + 1, min);
	}
	
	return 0;
}
