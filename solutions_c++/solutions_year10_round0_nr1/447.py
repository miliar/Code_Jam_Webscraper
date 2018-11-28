#include <cstdio>

int main () {
	int t, n, k, p[31];
	p[0] = 0;
	for (int i = 1; i < 31; i++) p[i] = 2 * p[i-1] + 1;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", i, (k + 1) & p[n] ? "OFF" : "ON");
	}
	return 0;
}

