#include <stdio.h>

int i, j, t, tt, n, k;

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: O", tt);
		scanf("%d%d", &n, &k);
		while (k > 0) {
			if (k & 1) {
				n--;
				k /= 2;
			} else break;
		}
		if (n <= 0) printf("N\n");
		else printf("FF\n");

	}
	return 0;
}
