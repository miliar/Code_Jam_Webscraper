#include <stdio.h>

int a[128];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, s, n, p, cas = 0;
	int i;

	scanf("%d", &T);
	while (T--) {
		scanf("%d%d%d", &n, &s, &p);
		for (i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
		}

		int low = 0, hi = n;
		int mid;
		//while (low < hi - 1) {
			mid = (low + hi) >> 1;
			int sn = 0;
			int cnt = 0;
			for (i = 0; i < n; ++i) {
				
				if (a[i] % 3 == 0) {
					if (a[i] / 3 + 1 == p && sn < s && a[i] / 3 - 1 >= 0) {
						++sn;
						++cnt;
					} else if (a[i] / 3 >= p) {
						++cnt;
					}
				} else if (a[i] % 3 == 1) {
					if (a[i] / 3 + 1 >= p) {
						++cnt;
					}
				} else if (a[i] % 3 == 2) {
					if (a[i] / 3 + 2 == p && sn < s) {
						++sn;
						++cnt;
					} else if (a[i] / 3 + 1 >= p) {
						++cnt;
					}
				}
			}
			printf("Case #%d: %d\n", ++cas, cnt);
		//}
	}
	return 0;
}