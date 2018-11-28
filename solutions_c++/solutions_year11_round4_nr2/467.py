#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include <set>
#include <cstring>

using namespace std;

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

typedef long long i64;

const int MAXN = 600;

char s[MAXN][MAXN];
i64 d[MAXN][MAXN];
i64 qx[MAXN][MAXN];
i64 qy[MAXN][MAXN];
i64 qd[MAXN][MAXN];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n, m, D;
		cin >> n >> m >> D;
		for (int i = 0; i < n; ++i) {
			cin >> s[i];
			for (int j = 0; j < m; ++j) {
				d[i][j] = D + (s[i][j] - '0');
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				qx[i][j] = (j ? qx[i][j - 1] : 0) + d[i][j] * (2 * i + 1);
			}
			for (int j = 0; j < m; ++j) {
				if (i) qx[i][j] += qx[i - 1][j];
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				qy[i][j] = (j ? qy[i][j - 1] : 0) + d[i][j] * (2 * j + 1);
			}
			for (int j = 0; j < m; ++j) {
				if (i) qy[i][j] += qy[i - 1][j];
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				qd[i][j] = (j ? qd[i][j - 1] : 0) + d[i][j];
			}
			for (int j = 0; j < m; ++j) {
				if (i) qd[i][j] += qd[i - 1][j];
			}
		}
		int k = min(n, m);
		bool f = false;
		while (!f && k >= 3) {
			f = false;
			for (int i = 0; i <= n - k; ++i) {
				for (int j = 0; j <= m - k; ++j) {
					i64 cx = 2 * i + k;
					i64 cy = 2 * j + k;
					i64 sx = qx[i + k - 1][j + k - 1];
					if (i) sx -= qx[i - 1][j + k - 1];
					if (j) sx -= qx[i + k - 1][j - 1];
					if (i && j) sx += qx[i - 1][j - 1];
					sx -= d[i][j] * (2 * i + 1);
					sx -= d[i + k - 1][j] * (2 * (i + k - 1) + 1);
					sx -= d[i][j + k - 1] * (2 * i + 1);
					sx -= d[i + k - 1][j + k - 1] * (2 * (i + k - 1) + 1);
					i64 sy = qy[i + k - 1][j + k - 1];
					if (i) sy -= qy[i - 1][j + k - 1];
					if (j) sy -= qy[i + k - 1][j - 1];
					if (i && j) sy += qy[i - 1][j - 1];
					sy -= d[i][j] * (2 * j + 1);
					sy -= d[i + k - 1][j] * (2 * j + 1);
					sy -= d[i][j + k - 1] * (2 * (j + k - 1) + 1);
					sy -= d[i + k - 1][j + k - 1] * (2 * (j + k - 1) + 1);
					i64 sd = qd[i + k - 1][j + k - 1];
					if (i) sd -= qd[i - 1][j + k - 1];
					if (j) sd -= qd[i + k - 1][j - 1];
					if (i && j) sd += qd[i - 1][j - 1];
					sd -= d[i][j];
					sd -= d[i + k - 1][j];
					sd -= d[i][j + k - 1];
					sd -= d[i + k - 1][j + k - 1];
					sx -= cx * sd;
					sy -= cy * sd;
//					cout << sx << " " << sy << endl;
					if (!sx && !sy) {
						f = true;
						break;
					}
				}
				if (f) break;
			}
/*			for (int i = 0; i <= n - k; ++i) {
				for (int j = 0; j <= m - k; ++j) {
					int sx = 0, sy = 0;
					double cx = 2 * i + k;
					double cy = 2 * j + k;
					//cout << cx << " " << cy << endl;
					for (int a = 0; a < k; ++a) {
						for (int b = 0; b < k; ++b) {
							if ((int)((a == 0) || (a == k - 1)) + (int)((b == 0) || (b == k - 1)) >= 2) continue;
							//cout << i << " " << a << " " << 2 * (i + a) - cx << endl;
							sx += d[i + a][j + b] * (2 * (i + a) + 1 - cx);
							sy += d[i + a][j + b] * (2 * (j + b) + 1 - cy);
						}
					}
					if (!sx && !sy) {
						f = true;
						break;
					}
				}
				if (f) break;
			}*/
			if (!f) --k;
		}
		if (k >= 3) printf("Case #%d: %d\n", tt + 1, k);
		else printf("Case #%d: IMPOSSIBLE\n", tt + 1);
	}
	return 0;
}
