#include <cstdio>

int t, n, k;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		scanf("%d%d", &n, &k);
		k %= (1 << n);
		printf("Case #%d: %s\n", i, (k == (1 << n) - 1 ? "ON" : "OFF"));
	}
	return 0;
}