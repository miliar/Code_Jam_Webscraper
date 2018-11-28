#include <cstdio>

int main() {
	freopen("D:\\a.in", "r", stdin);
	freopen("D:\\a.out", "w", stdout);
	int cas, n, k;
	scanf("%d", &cas);
	for (int cc = 1; cc <= cas; ++cc) {
		scanf("%d%d", &n, &k);
		bool ok = 1;
		for (int i = 0; i < n; ++i) {
			if (!(k & 1 << i)) {
				ok = 0;
				break;
			}
		}
		if (ok) {
			printf("Case #%d: ON\n", cc);
		} else {
			printf("Case #%d: OFF\n", cc);
		}
	}
	return 0;
}
