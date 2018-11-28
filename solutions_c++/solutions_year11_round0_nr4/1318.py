#include <cstdio>

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int cases, n, cnt, x;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		scanf("%d", &n);
		cnt = 0;
		for (int i = 1; i <= n; ++i) {
			scanf("%d", &x);
			if (x != i) ++cnt;
		}
		printf("Case #%d: %d.000000\n", cc, cnt);
	}
	return 0;
}
