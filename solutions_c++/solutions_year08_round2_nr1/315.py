#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;
typedef vector<int> VI;

#define SZ(c) ((int) (c).size())

ll numTriangles(const VI &x, const VI &y) {
	int	cnt[3][3] = {};
	for (int i = 0; i < SZ(x); ++i)
		++cnt[x[i] % 3][y[i] % 3];
	ll res = 0;
	for (int i = 0; i < 3; ++i)
		for (int j = 0; j < 3; ++j) {
			ll n = cnt[i][j];
			res += n * (n - 1) * (n - 2) / 6;
		}
	for (int a = 0; a < 9; ++a)
		for (int b = a + 1; b < 9; ++b)
			for (int c = b + 1; c < 9; ++c) {
				int x1 = a / 3;
				int y1 = a % 3;
				int x2 = b / 3;
				int y2 = b % 3;
				int x3 = c / 3;
				int y3 = c % 3;
				if ((x1 + x2 + x3) % 3 == 0 && (y1 + y2 + y3) % 3 == 0)
					res += (ll) cnt[x1][y1] * cnt[x2][y2] * cnt[x3][y3];
			}
	return res;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int nCases;
	int n, A, B, C, D, x0, y0, M;
	cin >> nCases;
	for (int c = 1; c <= nCases; ++c) {
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		VI x(n);
		VI y(n);
		x[0] = x0;
		y[0] = y0;
		for (int i = 1; i < n; ++i) {
			x[i] = (int) (((ll) A * x[i - 1] + B) % M);
			y[i] = (int) (((ll) C * y[i - 1] + D) % M);
		}
		printf("Case #%d: %lld\n", c, numTriangles(x, y));
	}
	return 0;
}
