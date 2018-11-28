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
#define N 105

int d[N][270];
int a[N];
int n, I, D, m;

bool isOK(int x, int y) {
	if (x == 256 || y == 256) return true;
	return abs(x - y) <= m;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d", &tk);
    for(int tc = 1; tc <= tk; ++tc) {
		cin >> D >> I >> m >> n;
		forn(i, n)
			cin >> a[i];
		forn(i, n + 1)
			forn(j, 257)
				d[i][j] = INF;
		d[0][256] = 0;

		forn(i, n) {
			forn(j, 257)
				forn(k, 256)
					if (isOK(j, k))
						d[i][k] = min(d[i][k], d[i][j] + I);

			ford(j, 257)
				ford(k, 256)
					if (isOK(j, k))
						d[i][k] = min(d[i][k], d[i][j] + I);

			forn(j, 257) {
				d[i + 1][j] = min(d[i + 1][j], d[i][j] + D);
				if (isOK(j, a[i]))
					d[i + 1][a[i]] = min(d[i + 1][a[i]], d[i][j]);
				forn(k, 256)
					if (isOK(j, k)) {
						int cost = min(I + D, abs(a[i] - k));
						d[i + 1][k] = min(d[i + 1][k], d[i][j] + cost);
					}
			}
		}

        printf("Case #%d: %d\n", tc, *min_element(d[n], d[n] + 257));
        cerr << "Case #" << tc << " is solved." << endl;
    }
    return 0;
}
