#include <iostream>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iterator>
#include <utility>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) for(int i = 0; i < (int)v.size(); ++i)
#define fors(i, s) for(int i = 0; i < (int)s.length(); ++i)
#define all(c) c.begin(), c.end()
#define pb push_back
#define abs(a) ((a) >= 0 ? (a) : -(a))
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

vector<pair<ll, ll>> x;
ll cnt[3][3];

int code(int x, int y) {
	return x * 3 + y;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d", &tk);

	ll a, b, c, d, m, x0, y0;
	int n;
	for(int tc = 1; tc <= tk; ++tc) {
		x.clear();
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		ll X = x0;
		ll Y = y0;
		x.push_back(make_pair(X, Y));
		for(int i = 1; i < n; ++i) {
			 X = (a * X + b) % m;
			 Y = (c * Y + d) % m;
			 x.pb(make_pair(X, Y));
		}
		sort(all(x));
		x.erase(unique(all(x)), x.end());
		memset(cnt, 0, sizeof cnt);
		forn(i, n)
			++cnt[x[i].first % 3][x[i].second % 3];
		ll ans = 0;
		forn(x1, 3)
			forn(y1, 3)
				forn(x2, 3)
					forn(y2, 3)
						if (code(x2, y2) <= code(x1, y1))
							forn(x3, 3)
								forn(y3, 3)
									if (code(x3, y3) <= code(x2, y2))
										if ((x1 + x2 + x3) % 3 == 0 && (y1 + y2 + y3) % 3 == 0) {
											int c1 = code(x1, y1);
											int c2 = code(x2, y2);
											int c3 = code(x3, y3);
											ll a1 = cnt[x1][y1];
											ll a2 = cnt[x2][y2];
											ll a3 = cnt[x3][y3];
											if (c1 == c2 && c2 == c3) {
												ans += a1 * (a1 - 1) * (a1 - 2) / 6;
											} else if (c1 == c2) {
												ans += a3 * (a1 * (a1 - 1) / 2);
											} else if (c2 == c3) {
												ans += a1 * (a2 * (a2 - 1) / 2);
											} else if (c1 == c3) {
												ans += a2 * (a1 * (a1 - 1) / 2);
											} else {
												ans += a1 * a2 * a3;
											}
										}
		printf("Case #%d: ", tc);
		cout << ans << endl;
	}

	return 0;
}