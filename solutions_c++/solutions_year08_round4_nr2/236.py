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

int const INF = INT_MAX >> 1;

int n, m, a;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		int ax2 = INF, ax3, ay2, ay3;
		scanf("%d%d%d", &n, &m, &a);
		
		for(int y2 = -m; y2 <= m; ++y2) {
			if (ax2 != INF) break;
			for(int x2 = 0; x2 <= n; ++x2) {
				if (ax2 != INF) break;
				for(int y3 = y2; max(0, y3) - min(0, y2) <= m; ++y3)
					for(int x3 = 0; x3 <= n; ++x3) {
						if (abs(x2 * y3 - x3 * y2) == a) {
							ax2 = x2, ax3 = x3, ay2 = y2, ay3 = y3;
							break;
						}
					}
			}
		}

		if (ax2 == INF) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		} else {
			int mn = min(min(0, ay2), ay3);
			int ax1 = 0, ay1 = 0 - mn;
			ay2 -= mn;
			ay3 -= mn;
			printf("Case #%d: %d %d %d %d %d %d\n", tc, ax1, ay1, ax2, ay2, ax3, ay3);
		}

		
		
	}

	return 0;
}