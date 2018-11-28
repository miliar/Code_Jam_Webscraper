#include <cstdio>
using namespace std;


int main() {
	freopen("c.in", "r", stdin);
	freopen("c1.out", "w", stdout);
	int t, T, i, j, l, h, n, ok;
	int a[14000];
	for (t = 1, scanf("%d", &T); t <= T; t++) {
		scanf("%d %d %d", &n, &l, &h);
		for (i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		for (i = l; i <= h; i++) {
			ok = 1;
			for (j = 0; j < n && ok == 1; j++) {
				if (a[j] % i != 0 && i % a[j] != 0) ok = 0;
			}
			if (ok == 1) {
				break;
			}
		}
		printf("Case #%d: ", t);
		if (ok == 1) {
			printf("%d\n", i);
		} else {
			printf("NO\n");
		}
	}
	fclose(stdout);
	return 0;
}
