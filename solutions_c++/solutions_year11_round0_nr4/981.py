#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n;
		scanf("%d", &n);
		int cnt = 0;
		for (int i = 1; i <= n; ++i) {
			int x;
			scanf("%d", &x);
			if (x != i) ++cnt;
		}
		printf("Case #%d: %d.000000\n", tt, cnt);
	}
}
