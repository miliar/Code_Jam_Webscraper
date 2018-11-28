#include <stdio.h>

int m, x, n, t, T, i, s;

int main() {
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%d", &n);
		m = 987654321;
		x = s = 0;
		while (n--) {
			scanf("%d", &i);
			if (i < m) m = i;
			x ^= i;
			s += i;
		}
		if (x == 0) {
			printf("%d\n", s - m);
		} else printf("NO\n");
	}
	return 0;
}
