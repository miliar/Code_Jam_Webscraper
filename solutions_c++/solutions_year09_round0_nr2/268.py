#include <stdio.h>
#include <stdlib.h>

const int mov[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int mat[105][105], mark[105][105];
int g[105][105][5];
int queue[10005];

int main() {

	//freopen("B.in", "r", stdin);
	//freopen("B.out", "w", stdout);

	int h, w, nprob;
	scanf("%d", &nprob);

	for (int prob = 0; prob < nprob; prob ++) {
		scanf("%d%d", &h, &w);
		for (int i = 0; i < h; i ++) {
			for (int j = 0; j < w; j ++) {
				scanf("%d", &mat[i][j]);
				g[i][j][0] = 0;
				mark[i][j] = -1;
			}
		}

		for (int i = 0; i < h; i ++) {
			for (int j = 0; j < w; j ++) {
				int lowest = INT_MAX, x, y;
				for (int dir = 0; dir < 4; dir ++) {
					int i1 = i + mov[dir][0];
					int j1 = j + mov[dir][1];
					if (i1 < 0 || i1 >= h || j1 < 0 || j1 >= w) continue;
					if (mat[i1][j1] < lowest) {
						lowest = mat[i1][j1];
						x = i1, y = j1;
					}
				}

				if (lowest >= mat[i][j]) continue;
				g[i][j][++g[i][j][0]] = x * w + y;
				g[x][y][++g[x][y][0]] = i * w + j;
			}
		}

		int flag = 0;
		for (int i = 0; i < h; i ++) {
			for (int j = 0; j < w; j ++) {
				if (mark[i][j] != -1) continue;
				int op = 0, cl = 1;
				queue[0] = i * w + j;
				mark[i][j] = flag;

				while (op < cl) {
					int x = queue[op] / w;
					int y = queue[op] % w;
					op ++;
					
					int tot = g[x][y][0];
					for (int k = 1; k <= tot; k ++) {
						int nx = g[x][y][k] / w;
						int ny = g[x][y][k] % w;
						if (mark[nx][ny] == -1) {
							mark[nx][ny] = flag;
							queue[cl++] = nx * w + ny;
						}
					}
				}

				flag ++;
			}
		}

		printf("Case #%d:\n", prob + 1);
		for (int i = 0; i < h; i ++) {
			for (int j = 0; j < w; j ++) printf("%c ", mark[i][j] + 'a');
			printf("\n");
		}
	}

	return 0;
}