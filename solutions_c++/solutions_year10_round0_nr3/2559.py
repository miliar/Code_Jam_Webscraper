#include <stdio.h>
#include <string.h>
int t, r, k, n, c, g[1010], p;
int f() {
	int t = 0, s = p, f = 0;
	while (t + g[p] <= k && !(f && p == s)) { f = 1; t += g[p]; p = (p + 1) % n; }
	return t;
}
int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf(" %d", &t);
	for (int i = 1; i <= t; i++) {
		p = c = 0;
		scanf(" %d %d %d", &r, &k, &n);
		for (int j = 0; j < n; j++) scanf(" %d", &g[j]);
		for (int j = 0; j < r; j++) 
			c += f();
		printf("Case #%d: %d\n", i, c);
	}
	return 0;
}