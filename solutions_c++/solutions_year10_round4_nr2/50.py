#include <cstdio>
#include <cstring>

const int maxn = 10 + 1;

int opt[(1 << maxn) + 1][maxn];
int a[(1 << maxn) + 1];
int p[(1 << maxn) + 1];
int n, m;

int getbest(int now, int prev)
{
	if (now >= m)
		if (n - a[m * 2 - now - 1] > prev) return 0x7000000;
		else return 0;
	else;
	if (opt[now][prev] != -1) return opt[now][prev];
	int left = now * 2;
	int right = now * 2 + 1;
	int min = 0x7000000;
	int o1 = getbest(left, prev) + getbest(right, prev);
	int o2 = getbest(left, prev + 1) + getbest(right, prev + 1) + p[now];
	if (o1 < min) min = o1;
	if (o2 < min) min = o2;
	return opt[now][prev] = min;
}

int main()
{
	int testnumber;
	
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (int testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d", &n);
		m = 1 << n;
		for (int i = 0; i < m; i++)
			scanf("%d", &a[i]);
		for (int i = 0; i < m - 1; i++)
			scanf("%d", &p[m - i - 1]);
		memset(opt, 0xff, sizeof opt);
		int best = getbest(1, 0);
		printf("Case #%d: %d\n", testcount + 1, best);
	}
	
	return 0;
}
