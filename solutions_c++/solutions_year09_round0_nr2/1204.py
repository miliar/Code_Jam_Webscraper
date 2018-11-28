#include <iostream>
#include <string.h>
using namespace std;

#define N 105
#define K 10005
int a[N][N];
int b[N][N];
int r[N];
int p[K];
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int i, j, k, n, m, x, y, z, t ,T;
char fr;
int ch(int x, int y) {
	return x >= 0  && x < n && y >= 0 && y < m;
}

int dfs(int x, int y) {
	int i, j, mn, xx, yy;
	if (b[x][y] != -1) {
		return b[x][y];
	}
	mn = a[x][y];
	for (i = 0; i < 4; i ++) {
		xx = x + dx[i];
		yy = y + dy[i];
		if (ch(xx, yy)) {
			if (a[xx][yy] < mn) {
				mn = a[xx][yy];
			}
		}
	}
	if (mn == a[x][y]) {
		b[x][y] = fr ++;
		return b[x][y];
	}
	for (i = 0; i < 4; i ++) {
		xx = x + dx[i];
		yy = y + dy[i];
		if (ch(xx, yy)) {
			if (a[xx][yy] == mn) {
				b[x][y] = dfs(xx, yy);
				return b[x][y];
			}
		}
	}
	return -1;
}



int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n >> m;
		memset(a, 0, sizeof(a));
		memset(b, -1, sizeof(b));
		memset(r, -1, sizeof(r));
		for (i = 0; i < n; i ++) {
			for (j = 0; j < m; j ++) {
				cin >> a[i][j];
			}
		}
		fr = 0;
		for (i = 0; i < n; i ++) {
			for (j = 0; j < m; j ++) {
				if (b[i][j] == -1) {
					b[i][j] = dfs(i, j);
				}
			}
		}
		fr = 'a';
		for (i = 0; i < n; i ++) {
			for (j = 0; j < m; j ++) {
				x = b[i][j];
				if (r[x] == -1) {
					r[x] = fr ++;
				}
			}
		}
		printf("Case #%d:\n", t);
		for (i= 0; i < n; i ++) {
			for (j = 0; j < m; j ++) {
				printf("%c ", r[b[i][j]]);
			}
			printf("\n");
		}
	}
	return 0;
}



