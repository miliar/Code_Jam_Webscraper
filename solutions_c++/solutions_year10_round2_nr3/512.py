#include <cstdio>

int t, n;
int cnt;

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int lt, i, j, k, l;
	scanf("%d", &t);
	for (lt = 1; lt <= t; lt++) {
		scanf("%d", &n);
		cnt = 0;
		for (i = (1 << n); i < (1 << (n + 1)); i += 4) {
			k = n;
			while (i & (1 << k)) {
				l = 0;
				for (j = 2; j <= k; j++)
					if (i & (1 << j)) l++;
				k = l;
				if (k == 1) cnt++;
			}
		}
		printf("Case #%d: %d\n", lt, cnt % 100003);
	}
	return 0;
}