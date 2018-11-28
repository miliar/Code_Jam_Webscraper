#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;

int gr[4][510][510];
int sum[510][510];
int s[4][510][510];

ll calc(int sx, int sy, int tx, int ty) {
	return sum[tx + 1][ty + 1] - sum[tx + 1][sy] - sum[sx][ty + 1] + sum[sx][sy];
}

ll calc(int n, int sx, int sy, int tx, int ty, int dsx, int dsy, int dtx, int dty, bool odd) {
	ll res = s[n][tx + 1][ty + 1] - s[n][tx + 1][sy] - s[n][sx][ty + 1] + s[n][sx][sy];
	//cerr << res << " " << s[n][tx + 1][ty + 1] << " " << s[n][tx + 1][sy] << " " << s[n][sx][ty + 1] << " " << s[n][sx][sy] << endl;
	//cerr << calc(dsx, dsy, dtx, dty) << endl;
	//cerr << dsx << " " << dsy << " " << dtx << " " << dty << endl;
	if(odd) return res - calc(dsx, dsy, dtx, dty) * (sx - 1) - (gr[n][tx][sy] + gr[n][tx][ty]) * (tx - sx + 1);
	return res * 2 - calc(dsx, dsy, dtx, dty) * (2 * sx - 1) - (gr[n][tx][sy] + gr[n][tx][ty]) * (2 * tx - 2 * sx + 1);
}

ll calc(int n, int r, int c, int sx, int sy, int tx, int ty, bool odd) {
	if(n == 0) return calc(n, sx, sy, tx, ty, sx, sy, tx, ty, odd);
	else if(n == 1) return calc(n, min(r - tx - 1, r - sx - 1), sy, max(r - sx - 1, r - tx - 1), ty, sx, sy, tx, ty, odd);
	else if(n == 2) return calc(n, sy, sx, ty, tx, sx, sy, tx, ty, odd);
	else if(n == 3) return calc(n, min(c - ty - 1, c - sy - 1), sx, max(c - ty - 1, c - sy - 1), tx, sx, sy, tx, ty, odd);
	assert(false);
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int r, c, d;
		cin >> r >> c >> d;
		for(int i = 0; i < r; ++i) {
			char line[1000];
			scanf("%s", line);
			for(int j = 0; j < c; ++j) {
				gr[0][i][j] = line[j] - '0';
				gr[1][r - i - 1][j] = gr[0][i][j];
				gr[2][j][i] = gr[0][i][j];
				gr[3][c - j - 1][i] = gr[0][i][j];
			}
		}
		for(int i = 0; i < r; ++i) {
			for(int j = 0; j < c; ++j) {
				sum[i + 1][j + 1] = sum[i][j + 1] + sum[i + 1][j] - sum[i][j] + gr[0][i][j];
			}
		}
		for(int i = 0; i < r; ++i) {
			for(int j = 0; j < c; ++j) {
				for(int k = 0; k < 2; ++k) {
					s[k][i + 1][j + 1] = s[k][i][j + 1] + s[k][i + 1][j] - s[k][i][j] + gr[k][i][j] * i;
					swap(i, j);
					s[k + 2][i + 1][j + 1] = s[k + 2][i][j + 1] + s[k + 2][i + 1][j] - s[k + 2][i][j] + gr[k + 2][i][j] * i;
					swap(i, j);
				}
			}
		}
		int res = 0;
		for(int i = 3; i <= min(r, c); ++i) {
			for(int j = 0; j + i <= r; ++j) {
				for(int k = 0; k + i <= c; ++k) {
					int len = i / 2;
					ll w1 = calc(3, r, c, j, k, j + i - 1, k + len - 1, i % 2);
					ll w2 = calc(2, r, c, j, k + i - len, j + i - 1, k + i - 1, i % 2);
					ll w3 = calc(1, r, c, j, k, j + len - 1, k + i - 1, i % 2);
					ll w4 = calc(0, r, c, j + i - len, k, j + i - 1, k + i - 1, i % 2);
					//cerr << w1 << " " << w2 << " " << w3 << " " << w4 << endl;
					assert(w1 >= 0 && w2 >= 0 && w3 >= 0 && w4 >= 0);
					if(w1 == w2 && w3 == w4) res = i;
				}
			}
		}
		printf("Case #%d: ", t);
		if(res >= 3) printf("%d\n", res);
		else puts("IMPOSSIBLE");
	}
	return 0;
}
