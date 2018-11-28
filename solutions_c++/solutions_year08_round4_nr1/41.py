#include <cstdio>

using namespace std;

#define can(x) ((x) >= 0)

int table[10005][2];
int g[10005], c[10005];
int T;
int M, V;

int main() {
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {

		scanf("%d%d", &M, &V);
		for (int i = 1; i <= M; ++i)
			table[i][0] = table[i][1] = 999999;

		for (int i = 1; i <= (M - 1) / 2; ++i)
			scanf("%d%d", &g[i], &c[i]);
		for (int i = (M + 1) / 2; i <= M; ++i) {
			int num;
			scanf("%d", &num);
			table[i][num] = 0;
			table[i][1 - num] = 999999;
		}

		for (int i = (M - 1) / 2; i >= 1; --i) {
			int lc = i * 2, rc = i * 2 + 1;

			if (g[i] == 0) { // OR
				table[i][0] <?= table[lc][0] + table[rc][0];
				table[i][1] <?= table[lc][0] + table[rc][1];
				table[i][1] <?= table[lc][1] + table[rc][0];
				table[i][1] <?= table[lc][1] + table[rc][1];
			} else { // AND
				table[i][0] <?= table[lc][0] + table[rc][0];
				table[i][0] <?= table[lc][0] + table[rc][1];
				table[i][0] <?= table[lc][1] + table[rc][0];
				table[i][1] <?= table[lc][1] + table[rc][1];
			}
			if (c[i] == 1) {
				if (g[i] == 0) { // CAN AND
					table[i][0] <?= table[lc][0] + table[rc][0] + 1;
					table[i][0] <?= table[lc][0] + table[rc][1] + 1;
					table[i][0] <?= table[lc][1] + table[rc][0] + 1;
					table[i][1] <?= table[lc][1] + table[rc][1] + 1;
				} else { // CAN OR
					table[i][0] <?= table[lc][0] + table[rc][0] + 1;
					table[i][1] <?= table[lc][0] + table[rc][1] + 1;
					table[i][1] <?= table[lc][1] + table[rc][0] + 1;
					table[i][1] <?= table[lc][1] + table[rc][1] + 1;
				}
			}
		}
		printf("Case #%d: ", cn);
		if (table[1][V] == 999999) printf("IMPOSSIBLE\n"); else printf("%d\n", table[1][V]);
	}
}
