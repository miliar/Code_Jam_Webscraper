#include <iostream>

using namespace std;

int a[110][110], b[110][110], c[110][110];
int visx[10010], visy[10010], ccc[10010];

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int main() {
	#ifndef ONLINE_JUDGE
	freopen("solution.in", "rt", stdin);
	freopen("solution.out", "wt", stdout);
	#endif
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		int n, m;
		scanf("%d%d", &n, &m);
		memset(a, 0x3C, sizeof(a));
		memset(b, 0, sizeof(b));
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		int color = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) if (!b[i][j]) {
				color++;
				int x = i, y = j;
				bool shit = false;
				int p = 0;
				while (!b[x][y]) {
					visx[p] = x;
					visy[p] = y;
					p++;
					b[x][y] = color;
					int mn = 999999;
					for (int s = 0; s < 4; s++) {
						int xx = x + dx[s];
						int yy = y + dy[s];
						mn <?= a[xx][yy];
					}
					if (mn >= a[x][y]) {
						shit = true;
						break;
					}
					for (int s = 0; s < 4; s++) {
						int xx = x + dx[s];
						int yy = y + dy[s];
						if (a[xx][yy] == mn) {
							x = xx;
							y = yy;
							break;
						}
					}
				}
				if (!shit) for (int k = 0; k < p; k++) {
					b[visx[k]][visy[k]] = b[x][y];
				}
			}
		}
		memset(ccc, -1, sizeof(ccc));
		char cc = 'a';
		printf("Case #%d:\n", test);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (ccc[b[i][j]] == -1) {
					ccc[b[i][j]] = cc++;
				}
				printf("%c ", ccc[b[i][j]]);
			}
			printf("\n");
		}
	}
	return 0;
}
