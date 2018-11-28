#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 505
typedef long long ll;
char c[N];
int a[N][N];
ll sx[N][N], sy[N][N];

int i, j, k, n, m, mx, d, l;
ll t, r, res, x, y, z;
int T,tt;

inline ll getx(int r, int i, int j) {
	return sx[r][j] - sx[r][i-1];
}
inline ll gety(int c, int i, int j) {
	return sy[c][j] - sy[c][i-1];
}
ll tx, ty;
int ii, jj;

int main() {
	freopen("b-large.in", "r", stdin);	freopen("b-large.out", "w", stdout);
		
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%d%d%d", &n, &m, &d);
		for (i = 1; i <= n; i ++) {
			scanf("%s", &c);
			for (j = 1; j <= m; j ++) {
				a[i][j] = c[j-1] - '0' + d;
			}
		}
		
		for (i = 1; i <= n; i ++) {
			for (j = 1; j <= m; j ++) {
				sx[i][j] = sx[i][j-1] + a[i][j];
			}
		}
		for (i = 1; i <= m; i ++) {
			for (j = 1; j <= n; j ++) {
				sy[i][j] = sy[i][j-1] + a[j][i];
			}
		}

				

		mx = 0;
		for (i = 2; i <= n - 1; i ++) {
			for (j = 2; j <= m - 1; j ++) {
				x = 0;
				y = 0;
				for (l = 1; i - l >= 1 && i + l <= n && j - l >= 1 && j + l <= m; l ++) {
					x += getx(i - l, j-l,j+l) * l;
					x -= getx(i + l, j-l,j+l) * l;
					y += gety(j - l, i-l, i+l) * l;
					y -= gety(j + l, i-l, i+l) * l;
					for (k = 1; k < l; k ++) {
						x += a[i-k][j-l]*k;
						x += a[i-k][j+l]*k;
						x -= a[i+k][j-l]*k;
						x -= a[i+k][j+l]*k;
					}
					for (k = 1; k < l; k ++) {
						y += a[i-l][j-k]*k;
						y += a[i+l][j-k]*k;
						y -= a[i-l][j+k]*k;
						y -= a[i+l][j+k]*k;
					}
					tx = (a[i-l][j-l] + a[i-l][j+l] - a[i+l][j-l] - a[i+l][j+l]) * l;
					ty = (a[i-l][j-l] - a[i-l][j+l] + a[i+l][j-l] - a[i+l][j+l]) * l;
					if (x - tx == 0 && y - ty == 0) {
						if (2*l + 1 > mx) {
							mx = 2*l + 1;
						}
					}
				}
			}
		}

		for (i = 2; i <= n - 1; i ++) {
			for (j = 2; j <= m - 1; j ++) {
				x = 0;
				y = 0;
				for (l = 0; i - l >= 1 && i + l+1 <= n && j - l >= 1 && j + l+1 <= m; l ++) {
					x += getx(i - l, j-l,j+l+1) * (2*l + 1);
					x -= getx(i + l+1, j-l,j+l+1) * (2*l + 1);
					y += gety(j - l, i-l, i+l+1) * (2*l + 1);
					y -= gety(j + l+1, i-l, i+l+1) * (2*l + 1);
					for (k = 0; k < l; k ++) {
						x += a[i-k][j-l]*(2*k+1);
						x += a[i-k][j+l+1]*(2*k+1);
						x -= a[i+k+1][j-l]*(2*k+1);
						x -= a[i+k+1][j+l+1]*(2*k+1);
					}
					for (k = 0; k < l; k ++) {
						y += a[i-l][j-k]*(2*k+1);
						y += a[i+l+1][j-k]*(2*k+1);
						y -= a[i-l][j+k+1]*(2*k+1);
						y -= a[i+l+1][j+k+1]*(2*k+1);
					}

					tx = (a[i-l][j-l] - a[i+l+1][j-l])*(2*l + 1) + (a[i-l][j+l+1] - a[i+l+1][j+l+1])*(2*l + 1);
					ty = (a[i-l][j-l] + a[i+l+1][j-l])*(2*l + 1) + (- a[i-l][j+l+1] - a[i+l+1][j+l+1])*(2*l + 1);
					if (x - tx == 0 && y - ty == 0) {
						if (2*l + 2 > mx) {
							mx = 2*l + 2;
						}
					}
				}
			}
		}
		printf("Case #%d: ", tt);
		if (mx < 3) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", mx);
		}
	}
	return 0;
}

				

/*
1
4 4 100000
1331
5775
5775
3332
*/