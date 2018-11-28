#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>

#include <cassert>
#include <cmath>
#include <ctime>

#include <map>
#include <set>
#include <bitset>
#include <queue>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()

#define N 10

const int INF = 1000 * 1000 * 1000 + 5;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1E-8;

int d[1 << N][N + 2], d1[1 << N][N + 2];
int n;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d", &tk);
    for(int tc = 1; tc <= tk; ++tc) {
		scanf("%d", &n);

		forn(i, 1 << n) {
			int m;
			scanf("%d", &m);
			for(int j = 0; j <= m; ++j)
				d[i][j] = 0;
			for(int j = m + 1; j < N + 2; ++j)
				d[i][j] = INF;
		}

		ford(it, n) {
			memcpy(d1, d, sizeof d);
			forn(i, 1 << n)
				forn(j, N + 2)
					d[i][j] = INF;
			for(int i = 0; i < 1 << it; ++i)  {
				int x;
				scanf("%d", &x);
				int l = i << 1, r = l + 1;
				for(int j = 0; j <= n; ++j) {
					d[i][j] = min(d[i][j], d1[l][j] + d1[r][j] + x);
					d[i][j] = min(d[i][j], d1[l][j + 1] + d1[r][j + 1]);
				}
			}
		}

		int ans = INF;
		for(int j = 0; j < N + 2; ++j)
			ans = min(ans, d[0][j]);
		printf("Case #%d: %d\n", tc, ans);
        cerr << "Case #" << tc << " is solved." << endl;
    }
    return 0;
}
