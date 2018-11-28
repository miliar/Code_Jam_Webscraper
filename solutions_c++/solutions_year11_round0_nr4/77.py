#include <cstdio>

int T, n, cnt, x;

int main() {
	scanf("%d", &T);
	for (int r = 0; r < T; ) {
		scanf("%d", &n);
		cnt = n;
		for (int i = 1; i <= n; ++i)
			scanf("%d", &x), cnt -= (i == x);
		printf("Case #%d: %d.000000\n", ++r, cnt);
	}
	return 0;
}
