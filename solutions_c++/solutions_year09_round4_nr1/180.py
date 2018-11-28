#include <cstdio>
#define MAXN 100
int cc, cnt, a[MAXN], n, cases;
char st[MAXN][MAXN];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	for (scanf("%d", &cases); cases; cases--) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			scanf("%s", st[i] + 1);
		}
		for (int i = n; i > 0; i--) {
			a[i] = 0;
			for (int j = n; j > 0; j--)
				if (st[i][j] == '1') {
					a[i] = j;
					break;
				}
		}
		cnt = 0;
		for (int i = 1; i <= n; i++) {
			if (a[i] > i) {
				int p = i + 1;
				while (p <= n && a[p] > i) p++;
				int tmp = a[p];
				for (int j = p; j > i; j--) a[j] = a[j - 1];
				a[i] = tmp; cnt += p - i;
			}
		}
		printf("Case #%d: %d\n", ++cc, cnt);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}