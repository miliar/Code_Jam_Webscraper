#include <stdio.h>
#include <algorithm>
using namespace std;

int i, j, k, n, b, T, t, tt;
int x[100], v[100], xpov[100];
bool can[100];

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		scanf("%d%d%d%d", &n, &k, &b, &T);
		for (i = 0; i < n; i++) scanf("%d", &x[i]);
		for (i = 0; i < n; i++) scanf("%d", &v[i]);

		int cnt = 0;
		for (i = 0; i < n; i++) {
			if (x[i] + T * v[i] < b) {
				can[i] = false;
			} else {
				can[i] = true;
				cnt++;
			}
		}

		if (cnt < k) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		cnt = 0;
		j = 0;
		for (i = n - 1; i >= 0; i--) {
			if (can[i]) {
				if (j >= k) break;
				cnt += (n-1-j) - i;
				j++;
			}
		}
		printf("%d\n", cnt);
/*
			for (i = 1; i <= T; i++) {
				for (j = n-1; j >= 0; j--) {
					x[j] += v[j];
					if (j < n-1 && x[j] > x[j+1]) x[j] = x[j+1];
				}
			}
			int cnt = 0;
			for (i = 0; i < n; i++) {
				if (x[i] >= b) cnt++;
			}
			if (cnt >= k) {
				for (i = 0; i < n; i++) { printf("%d ", p[i]); } printf("\n");
				j = numswaps();
				if (best == -1 || best > j) best = j;
			}
		} while (next_permutation(p, p+n));
		if (best == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", best);
*/
	}
	return 0;
}
