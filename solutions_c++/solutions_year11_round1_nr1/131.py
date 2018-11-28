#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		int n, d, g;
		scanf("%d%d%d", &n, &d, &g);
		bool ok = false;
		if (n > 100) {
			if (d == g)
				ok = true;
			if (g != 0 && g != 100)
				ok = true;
		}
		else {
			for (int i = 1; i <= n; ++i) {
				if (i * d % 100 == 0)
					ok = true;
			}
			if ((g == 0 || g == 100) && d != g)
				ok = false;
		}
		printf("Case #%d: ", Ti);
		if (ok) {
			printf("Possible\n");
		}
		else 
			printf("Broken\n");
	}
}
