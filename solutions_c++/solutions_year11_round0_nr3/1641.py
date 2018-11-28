#include <cstdio>
#include <cstring>

const int MAXN = 1000 + 1;

int main() {
	int m;
	scanf("%d", &m);
	for (int q = 1; q <= m; q++) {
		int n;
		scanf("%d", &n);
		int min = 100000000;
		int sum = 0;
		int tot = 0;
		for (int i = 1; i <= n; i++) {
			int t;
			scanf("%d", &t);
			if (min > t) min = t;
			sum ^= t;
			tot += t;
		}
		if (sum == 0) printf("Case #%d: %d\n", q, tot - min);
		else printf("Case #%d: NO\n", q);
	}
	return 0;
}
