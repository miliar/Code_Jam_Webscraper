#include <cstdio>
#include <cstring>
#include <algorithm>
using std::sort;

const int maxn = 100;

int a[maxn + 2];
int opt[maxn + 2][maxn + 2];
int p, n;

int calc(int x, int y)
{
	if (opt[x][y] != -1) return opt[x][y];
	if (y == x + 1) return opt[x][y] = 0;
	int min = 0x7fffffff;
	int t;
	for (int i = x + 1; i < y; i++)
		if ((t = calc(x, i) + calc(i, y)) < min) min = t;
	return opt[x][y] = (min + a[y] - a[x] - 2);
}

int main()
{
	int testnumber, testcount;
	
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d%d", &p, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		a[n] = 0;
		a[n + 1] = p + 1;
		sort(a, a + n + 2);
		memset(opt, 0xff, sizeof opt);
		printf("Case #%d: %d\n", testcount + 1, calc(0, n + 1));
	}
	
	return 0;
}
