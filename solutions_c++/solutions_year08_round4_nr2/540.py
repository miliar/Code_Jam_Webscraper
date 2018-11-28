#include<stdio.h>
#include<string>
#include<algorithm>
int n, m, A;
int T, casen;
int solve(int x1, int y1) {
	for (int x2 = 0; x2 <= n; x2++) {
		for (int y2 = 0; y2 <= m; y2++) {
			int a = y1 - y2;
			int b = x2 - x1;
			int c = x1 * (y2 - y1) + y1 * (x1 - x2) - A;
			if (a == 0) {
				if (b == 0) {
					continue;
				}
				if (c % b == 0) {
					int y = -c / b;
					if (y >= 0 && y <= m) {
						int x = n / 2;
						printf("Case #%d: %d %d %d %d %d %d\n", casen, x1, y1, x2, y2, x, y);
						return 1;
					}
				}
			} else {
				for (int y = 0; y <= m; y++) {
					if ((b * y + c) % a == 0) {
						int x = -(b * y + c) / a;
						if (x >= 0 && x <= n) {
							printf("Case #%d: %d %d %d %d %d %d\n", casen, x1, y1, x2, y2, x, y);
							return 1;
						}
					}
				}
			}
		}
	}
	return 0;
}
int main() {
	scanf("%d", &T);
	for (casen = 1; casen <= T; casen++) {
		scanf("%d%d%d", &n, &m, &A);
		if (!solve(0, 0) && !solve(0, m) && !solve(n, 0) && !solve(n, m)) {
			printf("Case #%d: IMPOSSIBLE\n", casen);
		}		
	}
}

