#include <stdio.h>
#include <string.h>

int T, h, w, t[100][100];
int W[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int min, minpos;
int s[10000][2], st;
char l[100][100], lc;

int main() {
	int lT, i, j, k, p, q;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (lT = 1; lT <= T; lT++) {
		scanf("%d%d", &h, &w);
		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
				scanf("%d", &t[i][j]);
		memset(l, 0, sizeof(l));
		lc = 'a';
		for (i = 0; i < h; i++) {
			for (j = 0; j < w; j++) {
				if (l[i][j]) continue;
				st = 0;
				s[st][0] = i;
				s[st][1] = j;
				while (true) {
					if (l[s[st][0]][s[st][1]])
						break;
					min = t[s[st][0]][s[st][1]];
					minpos = -1;
					for (k = 0; k < 4; k++) {
						p = s[st][0] + W[k][0];
						q = s[st][1] + W[k][1];
						if (p < 0 || p >= h || q < 0 || q >= w) continue;
						if (min > t[p][q]) {
							min = t[p][q];
							minpos = k;
						}
					}
					if (minpos == -1) {
						l[s[st][0]][s[st][1]] = lc++;
						break;
					}
					s[st + 1][0] = s[st][0] + W[minpos][0];
					s[st + 1][1] = s[st][1] + W[minpos][1];
					st++;
				}
				for (; st; st--)
					l[s[st - 1][0]][s[st - 1][1]] = l[s[st][0]][s[st][1]];
			}
		}
		printf("Case #%d:\n", lT);
		for (i = 0; i < h; i++) {
			for (j = 0; j < w; j++)
				printf("%c ", l[i][j]);
			printf("\n");
		}
	}
	return 0;
}