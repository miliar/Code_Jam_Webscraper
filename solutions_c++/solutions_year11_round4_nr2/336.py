#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

const int MAXN = 505;

llong sum[3][MAXN][MAXN];

inline llong get(int s, int i, int j) {
	if (i < 0 || j < 0)
		return 0;
	return sum[s][i][j];
}

inline bool eq(double a, double b) {
	if (abs(a - b) < 1e-9)
		return true;
	return false;
}

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		char dif[MAXN][MAXN];
		int r, c, d, mass[MAXN][MAXN];
		scanf("%d %d %d", &r, &c, &d);
		for (int i = 0; i < r; i++) {
			scanf("%s", dif[i]);
			for (int j = 0; j < c; j++)
				mass[i][j] = dif[i][j] - '0' + d;
		}
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				sum[0][i][j] = get(0, i - 1, j) + get(0, i, j - 1) - get(0, i - 1, j - 1) + mass[i][j];
				sum[1][i][j] = get(1, i - 1, j) + get(1, i, j - 1) - get(1, i - 1, j - 1) + (llong)i * mass[i][j];
				sum[2][i][j] = get(2, i - 1, j) + get(2, i, j - 1) - get(2, i - 1, j - 1) + (llong)j * mass[i][j];
			}
		bool good = false;
		for (int ans = min(r, c); ans >= 3 && !good; ans--)
			for (int i = 0; i + ans - 1 < r && !good; i++)
				for (int j = 0; j + ans - 1 < c && !good; j++) {
					int k = i + ans - 1, l = j + ans - 1;
					llong a = get(0, k, l) - get(0, i - 1, l) - get(0, k, j - 1) + get(0, i - 1, j - 1);
					llong b = get(1, k, l) - get(1, i - 1, l) - get(1, k, j - 1) + get(1, i - 1, j - 1);
					llong c = get(2, k, l) - get(2, i - 1, l) - get(2, k, j - 1) + get(2, i - 1, j - 1);
					a -= mass[i][j] + mass[i][l] + mass[k][j] + mass[k][l];
					b -= i * mass[i][j] + i * mass[i][l] + k * mass[k][j] + k * mass[k][l];
					c -= j * mass[i][j] + j * mass[k][j] + l * mass[i][l] + l * mass[k][l];
					double X = (double)b / (double)a, Y = (double)c / (double)a;
					double X1 = (i + k) / 2.00, Y1 = (j + l) / 2.00;
					if (eq(X, X1) && eq(Y, Y1)) {
						printf("Case #%d: %d\n", t, ans);
						good = true;
						break;
					}
				}
		if (!good)
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}

