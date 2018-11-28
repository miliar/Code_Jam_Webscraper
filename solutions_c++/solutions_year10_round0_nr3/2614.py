#include <stdio.h>
#include <stdlib.h>

int main(void) {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int z=1; z<=t; z++) {
		int r, k, n;
		int g[1006];
		scanf("%d %d %d", &r, &k, &n);
		for (int i=0; i<n; i++) scanf("%d", &g[i]);
		int money = 0;
		int sum = 0;
		int start = -1;
		for (int i=0; i<n; i++) {
			if (r == 0) break;
			if (sum + g[i] <= k && (start != i || start == -1)) {
				sum += g[i];
				if (start == -1) start = 0;
			} else {
				start = i;
				money += sum;
				sum = g[i];
				r--;
			}
			if (i == n-1) i = -1;
		}
		printf("Case #%d: %d\n", z, money);
	}
	return 0;
}
