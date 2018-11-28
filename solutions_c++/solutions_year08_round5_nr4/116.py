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

const int MOD = 10007;

const int dx[2] = {1, 2};
const int dy[2] = {2, 1};

int d[104][104];
bool bad[101][101];
int n, m;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		memset(d, 0, sizeof d);
		memset(bad, false, sizeof bad);
		int k;
		scanf("%d%d%d", &n, &m, &k);
		while (k --> 0) {
			int u, v;
			scanf("%d%d", &u, &v);
			bad[u - 1][v - 1] = true;
		}
		d[0][0] = 1;
		forn(i, n)
			forn(j, m)
				forn(l, 2) {
					int ty = i + dy[l];
					int tx = j + dx[l];
					if (!bad[ty][tx]) {
						d[ty][tx] = (d[ty][tx] + d[i][j]) % MOD;
					}
				}
					
		printf("Case #%d: %d\n", tc, d[n - 1][m - 1]);
	}

	return 0;
}