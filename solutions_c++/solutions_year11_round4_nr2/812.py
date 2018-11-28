#include <iostream>
#include <cstdio>

using namespace std;

#define EPS 1e-6
#define MAX 100

int w[MAX][MAX];

bool ok(int x, int y, int l) {
	int u = 2 * x + l;
	int v = 2 * y + l;
	int sx = 0;
	int sy = 0;
	for (int i = x; i < x + l; i++)
		for (int j = y; j < y + l; j++) {
			if (i == x || i == x + l - 1)
				if (j == y || j == y + l - 1)
					continue;
			sx += (2 * i + 1 - u) * w[i][j];
			sy += (2 * j + 1 - v) * w[i][j];
		}
	if (sx == 0 && sy == 0)
		return true;
	return false;
}

void solve(int test) {
	int m, n, d;

	cin >> m >> n >> d;

	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++) {
			char c;
			cin >> c;
			w[i][j] = c - '0';
		}

	cout << "Case #" << test << ": ";

	for (int k = min(m, n); k > 2; k--) {
		for (int i = 0; i <= m - k; i++)
			for (int j = 0; j <= n - k; j++) {
				if (ok(i, j, k)) {
//					cout << i << ' ' << j << endl;
					printf("%d\n", k);
					return;
				}
			}
	}
	printf("IMPOSSIBLE\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;

	cin >> nTest;

	for (int i = 0; i < nTest; i++)
		solve(i + 1);

	return 0;
}
