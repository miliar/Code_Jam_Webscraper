#include <stdio.h>

int t, T, i, n, j, k;

int main() {
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d", &n);
		k = 1;
		for (i = 1; i <= n; i++) {
			scanf("%d", &j);
			k += (i != j);
		}
		printf("Case #%d: ", t);
		printf("%d\n", (k & 1) ? (k / 2) * 2 : ((k-3)/2)*2+3);
	}
	return 0;
}
