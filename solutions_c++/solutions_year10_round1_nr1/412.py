#include <stdio.h>
char g[111][111], rg[111][111];

int main() {
	int tn, n, k;
	int i, j, prob = 0;
//	freopen("a.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	for (scanf("%d", &tn); tn--; ) {
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++) {
			scanf("%s", g[i]);
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				rg[i][j] = g[n - 1 - j][i];
			}
		}
		for (j = 0; j < n; j++) {
			int la = n - 1;
			while (la >= 0 && rg[la][j] == '.') {
				la--;
			}
			for (i = n - 1; i >= 0; i--) {
				if (la < 0) {
					rg[i][j] = '.';
				} else {
					rg[i][j] = rg[la--][j];
					while (la >= 0 && rg[la][j] == '.') {
						la--;
					}
				}
			}
		}
/*		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				printf("%c", rg[i][j]);
			}
			printf("\n");
		}*/
		bool wr = false, wb = false;
		int si, sj, sr, sb;
		for (i = 0; i < n; i++) {
			sr = 0, sb = 0;
			for (j = 0; j < n; j++) {
				if (rg[i][j] == 'R') {
					if (++sr >= k) {
						wr = true;
					}
					sb = 0;
				} else if (rg[i][j] == 'B') {
					if (++sb >= k) {
						wb = true;
					}
					sr = 0;
				} else {
					sr = sb = 0;
				}
			}
		}

		for (j = 0; j < n; j++) {
			sr = 0, sb = 0;
			for (i = 0; i < n; i++) {
				if (rg[i][j] == 'R') {
					if (++sr >= k) {
						wr = true;
					}
					sb = 0;
				} else if (rg[i][j] == 'B') {
					if (++sb >= k) {
						wb = true;
					}
					sr = 0;
				} else {
					sr = sb = 0;
				}
			}
		}
		
		for (si = 0; si < n; si++) {
			for (sj = 0; sj < n; sj++) {
				i = si, j = sj;
				sr = 0, sb = 0;
				while (i >= 0 && i < n && j >= 0 && j < n) {
					if (rg[i][j] == 'R') {
						if (++sr >= k) {
							wr = true;
						}
						sb = 0;
					} else if (rg[i][j] == 'B') {
						if (++sb >= k) {
							wb = true;
						}
						sr = 0;
					} else {
						sr = sb = 0;
					}
					i++, j++;
				}

				i = si, j = sj;
				sr = 0, sb = 0;
				while (i >= 0 && i < n && j >= 0 && j < n) {
					if (rg[i][j] == 'R') {
						if (++sr >= k) {
							wr = true;
						}
						sb = 0;
					} else if (rg[i][j] == 'B') {
						if (++sb >= k) {
							wb = true;
						}
						sr = 0;
					} else {
						sr = sb = 0;
					}
					i++, j--;
				}
			}
		}

		printf("Case #%d: ", ++prob);
		if (wr && wb) {
			printf("Both\n");
		} else if (!wr && !wb) {
			printf("Neither\n");
		} else if (wr && !wb) {
			printf("Red\n");
		} else {
			printf("Blue\n");
		}
	}
	return 0;
}
