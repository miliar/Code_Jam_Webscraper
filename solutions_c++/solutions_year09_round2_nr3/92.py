#include <cstdio>
#include <cctype>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int n, m, tot, best;
char grid[21][21];
string a[21][21][1000], path, tstr, sol;
int qx[400000], qy[400000], qsum[400000], p, q;
int d[4][2] = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

void update(string str) {
	if (sol == "" || (str.size() == sol.size() && str < sol)) {
		sol = str;
		best = sol.size();
	}
}

void bfs() {
	int i, j, k, x, y, sum, tx1, ty1, tx2, ty2, tsum;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			for (k = 0; k < 1000; k++) {
				a[i][j][k] = "";
			}
		}
	}
	p = q = 0;
	best = 100000;
	sol = "";
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) if (isdigit(grid[i][j])) {
			qx[q] = i;
			qy[q] = j;
			qsum[q] = grid[i][j] - '0';
			a[i][j][qsum[q] + 500] = grid[i][j];
			if (qsum[q] == tot) update(a[i][j][qsum[q] + 500]);
			q++;
		}
	}
	for (; p < q; p++) {
		x = qx[p];
		y = qy[p];
		sum = qsum[p];
		path = a[x][y][sum + 500];
		if (path.size() > best) return;
		for (i = 0; i < 4; i++) {
			tx1 = x + d[i][0];
			ty1 = y + d[i][1];
			if (tx1 < 0 || ty1 < 0 || tx1 >= n || ty1 >= n) continue;
			for (j = 0; j < 4; j++) {
				tx2 = tx1 + d[j][0];
				ty2 = ty1 + d[j][1];
				if (tx2 < 0 || ty2 < 0 || tx2 >= n || ty2 >= n) continue;
				if (grid[tx1][ty1] == '+') {
					tsum = sum + (grid[tx2][ty2] - '0');
				}
				else {
					tsum = sum - (grid[tx2][ty2] - '0');
				}
				if (tsum < -250 || tsum > 400) continue;
				tstr = path + grid[tx1][ty1] + grid[tx2][ty2];
				if (tsum == tot) {
					update(tstr);
				}
				if (a[tx2][ty2][tsum + 500] == "" || (tstr.size() == a[tx2][ty2][tsum + 500].size() && tstr < a[tx2][ty2][tsum + 500])) {
					qx[q] = tx2;
					qy[q] = ty2;
					qsum[q] = tsum;
					a[tx2][ty2][tsum + 500] = tstr;
					q++;
				}
			}
		}
	}
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int i, T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) {
			scanf("%s", grid[i]);
		}
		printf("Case #%d:\n", t);
		for (i = 0; i < m; i++) {
			scanf("%d", &tot);
			bfs();
			printf("%s\n", sol.c_str());
		}
	}

	return 0;
}
