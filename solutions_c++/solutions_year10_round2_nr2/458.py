#include <cstdio>

#define N_MAX 50

int c, n, k, b, t, x[N_MAX], v[N_MAX];
int cnt;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int lc, i, j, tmp;
	scanf("%d", &c);
	for (lc = 1; lc <= c; lc++) {
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for (i = 0; i < n; i++) scanf("%d", &x[i]);
		for (i = 0; i < n; i++) scanf("%d", &v[i]);
		cnt = tmp = 0;
		for (i = n - 1; i >= 0; i--) {
			if (b - x[i] <= t * v[i]) {
				cnt += tmp;
				k--;
				if (!k) break;
			} else tmp++;
		}
		if (k) printf("Case #%d: IMPOSSIBLE\n", lc);
		else printf("Case #%d: %d\n", lc, cnt);
	}
	return 0;
}