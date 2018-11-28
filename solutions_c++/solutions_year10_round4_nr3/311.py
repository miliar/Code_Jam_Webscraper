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

#define N 110

bool a[N][N], a1[N][N];

int n;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d", &tk);
    for(int tc = 1; tc <= tk; ++tc) {
		memset(a, 0, sizeof a);
		int n;
		bool was = false;
		int ans = 0;
		scanf("%d", &n);
		while (n --> 0) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int i = x1; i <= x2; ++i)
				for(int j = y1; j <= y2; ++j)
					a[i][j] = was = true;
		}

		while (was) {
			was = false;
			++ans;
			memcpy(a1, a, sizeof a);
			for(int i = 1; i <= 100; ++i)
				for(int j = 1; j <= 100; ++j)
					if (a1[i][j]) {
						a[i][j] = a1[i - 1][j] || a1[i][j - 1];
						was |= a[i][j];
					} else {
						a[i][j] = a1[i - 1][j] && a1[i][j - 1];
						was |= a[i][j];
					}
		}

        printf("Case #%d: %d\n", tc, ans);
        cerr << "Case #" << tc << " is solved." << endl;
    }
    return 0;
}
