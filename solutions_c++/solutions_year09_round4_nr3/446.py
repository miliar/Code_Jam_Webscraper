#include <iostream>

using namespace std;

const int INF = 1000000000;

int T;
int n;
int k;
int price[32][32];
bool g[32][32];

bool ok[1 << 16];
int best[1 << 16];

bool compatible(int a[], int b[])
{
	for (int i = 0; i < k - 1; ++i)  {
		if (a[i] == b[i] || a[i + 1] == b[i + 1])
			return false;
		if ((a[i] > b[i]) ^ (a[i + 1] > b[i + 1]))
			return false;
	}
	return true;
}

int minCharts()
{
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j)
			g[i][j] = g[j][i] = compatible(price[i], price[j]);
		g[i][i] = false;
	}

	for (int set = 0; set < 1 << n; ++set) {
		ok[set] = true;
		for (int i = 0; i < n; ++i)
			if ((set >> i & 1) == 1) {
				if (!ok[set ^ 1 << i]) {
					ok[set] = false;
					break;
				}
				for (int j = i + 1; j < n; ++j)
					if ((set >> j & 1) == 1 && !g[i][j]) {
						ok[set] = false;
						break;
					}
				break;
			}
	}

	for (int set = 0; set < 1 << n; ++set)
		best[set] = INF;
	best[0] = 0;
	for (int set = 0; set < 1 << n; ++set)
		if (best[set] < INF) {
			int t = ((1 << n) - 1) ^ set;
			for (int v = t; v != 0; v = (v - 1) & t)
				if (ok[v])
					best[set | v] = min(best[set | v], best[set] + 1);
		}

	return best[(1 << n) - 1];
}

int main()
{
	scanf("%d", &T);
	for (int ncase = 1; ncase <= T; ++ncase) {
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < k; ++j)
				scanf("%d", &price[i][j]);
		printf("Case #%d: %d\n", ncase, minCharts());
	}
	return 0;
}
