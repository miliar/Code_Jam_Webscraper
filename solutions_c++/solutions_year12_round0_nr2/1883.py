#include <cstdio>

int main() {
	int T; scanf("%d", &T);
	for (int Case = 1; Case <= T; Case ++) {
		int n, s, p; scanf("%d%d%d", &n, &s, &p);
		int lim1 = p * 3 - 2, lim2 = p * 3 - 4;
		if (lim1 < p) lim1 = p; if (lim2 < p) lim2 = p;

		int ans = 0;
		for (int i = 0; i < n; i ++) {
			int a; scanf("%d", &a);
			if (a >= lim1) ans ++;
			else if (a >= lim2 && s) {
				ans ++; s --;
			}
		}
		printf("Case #%d: %d\n", Case, ans);
	}

	return 0;
}
