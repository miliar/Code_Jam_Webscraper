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

const int INF = INT_MAX >> 1;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1E-8;

#define N 1001

int64 d[N];
int c[N];
int n, m, cap;
int a[N];

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d", &tk);
    for(int tc = 1; tc <= tk; ++tc) {
		scanf("%d%d%d", &m, &cap, &n);
		forn(i, n)
			scanf("%d", &a[i]);

		forn(i, n)
			c[i] = -1, d[i] = -1;

		int64 ans = 0;
		int ride = 0, p = 0;
		bool cycFound = false;
		while (ride < m)
			if (cycFound || c[p] == -1) {
				c[p] = ride;
				d[p] = ans;
				int cur = 0;
				int oldP = p;
				do {
					if (cur + a[p] > cap) break;
					cur += a[p];
					ans += a[p];
					p = (p + 1) % n;
				} while (p != oldP);
				++ride;
			} else {
				cycFound = true;
				int cycLen = ride - c[p];
				int64 profit = ans - d[p];
				int cycRides = (m - ride) / cycLen;
				ans += profit * cycRides;
				ride += cycRides * cycLen;
			}

        printf("Case #%d: %I64d\n", tc, ans);
		cerr << "Case #" << tc << " is solved." << endl;
    }
    return 0;
}
