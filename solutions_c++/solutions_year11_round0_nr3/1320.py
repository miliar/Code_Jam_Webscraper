#include <cstdio>

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int cases, n, x;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		scanf("%d", &n);
		int mini = 1000000000;
		int addsum = 0, xorsum = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &x);
			if (mini > x) mini = x;
			xorsum ^= x;
			addsum += x;
		}
		printf("Case #%d: ", cc);
		if (xorsum) {
			puts("NO");
		} else {
			printf("%d\n", addsum - mini);
		}
	}
	return 0;
}
