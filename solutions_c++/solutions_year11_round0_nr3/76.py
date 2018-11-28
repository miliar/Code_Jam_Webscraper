#include <cstdio>

int T, x, s, t, m, n;

int main() {
	scanf("%d", &T);
	for (int r = 0; r < T; ) {
		s = t = 0;
		m = 1 << 28;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &x);
			s ^= x;
			t += x;
			if (x < m)
				m = x;
		}
		printf("Case #%d: ", ++r);
		if (s)
			puts("NO");
		else
			printf("%d\n", t - m);
	}
	return 0;
}
