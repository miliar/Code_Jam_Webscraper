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

int get(int x, int y) {
	if (x == y) return 0;
	if (x > y) swap(x, y);
	if (y >= 2 * x) return 1;
	return 1 - get(y - x, x);
}

int64 gans(int x, int y) {
	int64 ans = (int64) x * y;
	int l = x, r = x;
	while (get(x, r + 1) == 0) ++r;
	while (x >= 1) {
		while (l - 1 >= 1 && get(x, l - 1) == 0) --l;
		while (get(x, r) == 1) --r;
		int bl = l, br = min(r, y);
		if (bl <= br) ans -= br - bl + 1;
		--x;
	}
	return ans;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d", &tk);
    for(int tc = 1; tc <= tk; ++tc) {
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int64 ans = gans(a2, b2) - gans(a1 - 1, b2) - gans(a2, b1 - 1) + gans(a1 - 1, b1 - 1);
        printf("Case #%d: %I64d\n", tc, ans);
        cerr << "Case #" << tc << " is solved." << endl;
    }
    return 0;
}
