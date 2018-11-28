#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

const int maxn = 105;
const int inf = 100000000;

const int UP = 0;
const int LEFT = 1;
const int RIGHT = 2;
const int DOWN = 3;

int R, C;
char g[maxn][maxn][4];
int a[maxn][maxn];
int mov[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
char label;
char mk[maxn][maxn];

void dfs(int r, int c) {
	mk[r][c] = label;
	for (int k = 0; k < 4; k++) {
		if (g[r][c][k]) {
			int rr = r + mov[k][0];
			int cc = c + mov[k][1];
			if (!mk[rr][cc]) {
				dfs(rr, cc);
			}
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				scanf("%d", &a[i][j]);
			}
		}
		memset(g, 0, sizeof(g));
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				int up = inf, left = inf, right = inf, down = inf;
				if (i > 0) {
					up = a[i - 1][j];
				}
				if (j > 0) {
					left = a[i][j - 1];
				}
				if (j + 1 < C) {
					right = a[i][j + 1];
				}
				if (i + 1 < R) {
					down = a[i + 1][j];
				}
				int m = min(min(up, down), min(left, right));
				if (m < a[i][j]) {
					if (up == m) {
						g[i][j][UP] = 1;
						g[i - 1][j][DOWN] = 1;
					} else if (left == m) {
						g[i][j][LEFT] = 1;
						g[i][j - 1][RIGHT] = 1;
					} else if (right == m) {
						g[i][j][RIGHT] = 1;
						g[i][j + 1][LEFT] = 1;
					} else {
						g[i][j][DOWN] = 1;
						g[i + 1][j][UP] = 1;
					}
				}
			}
		}
		label = 'a';
		memset(mk, 0, sizeof(mk));
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (!mk[i][j]) {
					dfs(i, j);
					++label;
				}
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < R; i++) {
			putchar(mk[i][0]);
			for (int j = 1; j < C; j++) {
				putchar(' ');
				putchar(mk[i][j]);
			}
			puts("");
		}
	}
	return 0;
}

