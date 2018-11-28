#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>
#include <climits>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define ll long long

#define NMAX 2 * 111111

ll x[NMAX], y[NMAX];

ll T[NMAX][5][3][3];

void solve(int tst) {

	int n;
	scanf("%d", &n);

	int a, b, c, d, x0, y0, m;
	scanf("%d%d%d%d%d%d%d", &a, &b, &c, &d, &x0, &y0, &m);

	forn (i, n) {
		x[i] = x0;
		y[i] = y0;
		x0 = ((ll)a * (ll)x0 + (ll)b) % m;
		y0 = ((ll)c * (ll)y0 + (ll)d) % m;
	}

	long long ans = 0;

	memset(T, 0, sizeof(T));
	T[0][0][0][0] = 1;

	forn (i, n)
		forn (k, 4)
			forn (rx, 3)
				forn (ry, 3) {
					T[i + 1][k][rx][ry] += T[i][k][rx][ry];
					T[i + 1][k + 1][(rx + x[i]) % 3][(ry + y[i]) % 3] += T[i][k][rx][ry];
				}

	ans = T[n][3][0][0];

	cout << "Case #" << tst << ": " << ans << endl;
}

int main() {

	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tst;
	scanf("%d", &tst);
	forn (i, tst) solve(i + 1);

	return 0;
}

