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

char a[60][60], b[60][60];
int n, k;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d", &tk);
    for(int tc = 1; tc <= tk; ++tc) {
		scanf("%d %d\n", &n, &k);
		forn(i, n)
			gets(b[i]);

		forn(i, n)
			forn(j, n)
				a[j][n - i - 1] = b[i][j];

		forn(j, n) {
			int p = n - 1;
			ford(i, n)
				if (a[i][j] != '.') a[p--][j] = a[i][j];
			while (p >= 0) a[p--][j] = '.';
		}

		bool wasR = false, wasB = false;
		forn(i, n)
			forn(j, n)
				if (a[i][j] != '.')
					for(int dx = -1; dx <= 1; ++dx)
						for(int dy = -1; dy <= 1; ++dy)
							if (dx != 0 || dy != 0) {
								bool ok = true;
								for(int len = 1; len < k && ok; ++len) {
									int tx = j + dx * len, ty = i + dy * len;
									if (!(0 <= tx && tx < n && 0 <= ty && ty < n
										&& a[ty][tx] == a[i][j])) ok = false;
								}
								if (ok) (a[i][j] == 'R' ? wasR : wasB) = true;
							}
				

        printf("Case #%d: ", tc);
		puts(wasR ? (wasB ? "Both" : "Red") : (wasB ? "Blue" : "Neither"));
        cerr << "Case #" << tc << " is solved." << endl;
    }
    return 0;
}
