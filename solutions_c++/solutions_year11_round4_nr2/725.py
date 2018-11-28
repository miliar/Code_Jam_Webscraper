#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int dist2(int x0, int y0, int x1, int y1) {
	return (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0);
}

string board[10];

bool solve(int i0, int j0, int sz) {
	double sx = 0, sy = 0;
	double cx = 0.5 * sz - 0.5;
	double cy = 0.5 * sz - 0.5;
	for (int di = 0; di < sz; di++)
		for (int dj = 0; dj < sz; dj++) {
			int i = i0 + di;
			int j = j0 + dj;
			if (di == 0 && dj == 0 || di == 0 && dj == sz - 1 || di == sz - 1
					&& dj == 0 || di == sz - 1 && dj == sz - 1)
				continue;
			sx += (cx - di) * board[i][j];
			sy += (cy - dj) * board[i][j];
		}
	if (fabs(sx) < 1e-5 && fabs(sy) < 1e-5)
		return true;
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst, T;
	cin >> T;
	for (tst = 1; tst <= T; tst++) {
		int n, m, i, j, k, d;
		cin >> n >> m >> d;
		for (i = 0; i < n; i++)
			cin >> board[i];
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
				board[i][j] = board[i][j] - '0' + d;
		for (k = n; k >= 3; k--) {
			bool good = false;
			for (i = 0; i <= n - k; i++)
				for (j = 0; j <= m - k; j++)
					if (solve(i, j, k))
						good = true;
			if (good)
				break;
		}
		printf("Case #%d: ", tst);
		if (k >= 3)
			printf("%d\n", k);
		else
			puts("IMPOSSIBLE");
	}

	return 0;
}
