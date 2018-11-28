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

#define N 10001

int const INF = INT_MAX >> 1;

int d[N][2];
int v[N], c[N];
int n;


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		printf("Case #%d: ", tc);
		int vv;
		scanf("%d%d", &n, &vv);
		for(int i = 1; i <= (n - 1) / 2; ++i) {
			scanf("%d %d", &v[i], &c[i]);
			d[i][0] = INF;
			d[i][1] = INF;
		}
		for(int i = (n - 1) / 2 + 1; i <= n; ++i) {
			scanf("%d", &v[i]);
			d[i][v[i]] = 0;
			d[i][v[i] ^ 1] = INF;
		}

		for(int i = (n - 1) / 2; i >= 1; --i) {
			if (v[i] == 1) {
				d[i][0] = min(d[i][0], min(d[i * 2][0], d[i * 2 + 1][0]));
				d[i][1] = min(d[i][1], d[i * 2][1] + d[i * 2 + 1][1]);
				if (c[i]) {
					d[i][0] = min(d[i][0], 1 + d[2 * i][0] + d[2 * i + 1][0]);
					d[i][1] = min(d[i][1], 1 + min(d[2 * i][1], d[2 * i + 1][1]));
				}
			} else {
				d[i][1] = min(d[i][1], min(d[i * 2][1], d[i * 2 + 1][1]));
				d[i][0] = min(d[i][0], d[i * 2][0] + d[i * 2 + 1][0]);
				if (c[i]) {
					d[i][1] = min(d[i][1], 1 + d[2 * i][1] + d[2 * i + 1][1]);
					d[i][0] = min(d[i][0], 1 + min(d[2 * i][0], d[2 * i + 1][0]));
				}
			}
		}
		if (d[1][vv] >= INF) printf("IMPOSSIBLE\n");
		else printf("%d\n", d[1][vv]);
	}

	return 0;
}