#include <stdio.h>
#include <string.h>

int T, n, k, p[110][110];
bool overlap[110][110];
int chk[65536];
int overlaid[65536], op;
int d[20][65536];

bool check(int s, int p) {
	if (p == n) {
		if (!chk[s]) {
			overlaid[op++] = s;
			return true;
		}
		return false;
	}
	bool chk1, chk2 = false;
	int i;
	for (i = 0; i < p; i++)
		if ((s & (1 << i)) && overlap[i][p]) break;
	if (i == p) chk2 = check(s + (1 << p), p + 1);
	if (!chk[s]) chk[s] = p;
	chk1 = check(s, p + 1);
	if (!chk1 && !chk2 && chk[s] == p) {
		overlaid[op++] = s;
		return true;
	}
	return (chk1 || chk2);
}

int main() {
	int lT, i, j, s;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (lT = 1; lT <= T; lT++) {
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++)
			for (j = 0; j < k; j++)
				scanf("%d", &p[i][j]);
		for (i = 0; i < n; i++) {
			for (j = i + 1; j < n; j++) {
				for (s = 0; s < k; s++)
					if (p[i][s] == p[j][s] || (p[i][0] < p[j][0]) != (p[i][s] < p[j][s]))
						break;
				overlap[i][j] = (s < k ? true : false);
			}
		}
		op = 0;
		memset(chk, 0, sizeof(chk));
		check(0, 0);
		memset(d, 0, sizeof(d));
		d[0][0] = true;
		for (i = 1; i <= n; i++) {
			for (s = 0; s < (1 << n); s++)
				if (d[i - 1][s])
					for (j = 0; j < op; j++)
						d[i][s | overlaid[j]] = true;
			if (d[i][(1 << n) - 1]) break;
		}
		printf("Case #%d: %d\n", lT, i);
	}
	return 0;
}