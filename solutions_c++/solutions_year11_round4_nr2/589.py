#include <iostream>
#include <cmath>

using namespace std;

const int MAX_N = 504;
const long double eps = 1e-10;

long b[MAX_N][MAX_N];
int R, C;
long long D;
long long sx[MAX_N][MAX_N], sy[MAX_N][MAX_N], s[MAX_N][MAX_N];

long long getSx(int i, int j, int x, int y) {
	return sx[x][y] - sx[x][j-1] - sx[i-1][y] + sx[i-1][j-1];
}

long long getSy(int i, int j, int x, int y) {
	return sy[x][y] - sy[x][j-1] - sy[i-1][y] + sy[i-1][j-1];
}

long long getS(int i, int j, int x, int y) {
	return s[x][y] - s[x][j-1] - s[i-1][y] + s[i-1][j-1];
}

bool equal(long double a, long double b) {
	return (fabs(a-b) < eps);
}

void solve() {
	cin >> R >> C;
	cin >> D;
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			char ch;
			cin >> ch;
			b[i][j] = (ch - '0') + D;
		}
	}

	memset(sx, 0, sizeof(sx));
	memset(sy, 0, sizeof(sy));
	memset(s, 0, sizeof(s));
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			sx[i][j] = (sx[i][j-1] + sx[i-1][j] - sx[i-1][j-1]) + b[i][j]*i;
			sy[i][j] = (sy[i][j-1] + sy[i-1][j] - sy[i-1][j-1]) + b[i][j]*j;
			s[i][j] = (s[i][j-1] + s[i-1][j] - s[i-1][j-1]) + b[i][j];
		}
	}
	
	for (int K = min(R, C); K >= 3; --K) {
		for (int i = 1; i <= R - K + 1; ++i) {
			for (int j = 1; j <= C - K + 1; ++j) {
				int x = i+K-1;
				int y = j+K-1;
				long long tx = getSx(i, j, x, y) - b[i][j]*i - b[i][y]*i - b[x][j]*x - b[x][y]*x;
				long long ty = getSy(i, j, x, y) - b[i][j]*j - b[i][y]*y - b[x][j]*j - b[x][y]*y;
				long double cx = tx*1.0 / (getS(i, j, x, y) - b[i][j] - b[i][y] - b[x][j] - b[x][y]);
				long double cy = ty*1.0 / (getS(i, j, x, y) - b[i][j] - b[i][y] - b[x][j] - b[x][y]);
					if (equal(x+i, cx*2) && equal(y+j, cy*2)) {
						cout << K << endl;
						return;
					}
				
			}
		}
	}
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	int nTest;
	cin >> nTest;
	for (int i = 1; i <= nTest; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

