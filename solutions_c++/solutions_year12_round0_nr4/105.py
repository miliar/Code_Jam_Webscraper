#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

int n, m, d;
string s[110];

void read() {
	cin >> n >> m >> d;
	forn(i, n)
		cin >> s[i];
}

int gcd(int a, int b) {
	return a == 0 ? b : gcd(b % a, a);
}

void solve() {
	int x, y;
	forn(i, n)
		forn(j, m)
			if (s[i][j] == 'X') {
				x = i - 1;
				y = j - 1;
			}
	n -= 2;
	m -= 2;

	set<pair<int, int> > used;
	int ans = 0;
	for (int i = -100; i <= 100; i++)
		for (int j = -100; j <= 100; j++) {
			if (i == 0 && j == 0)
				continue;

			int nx = n * i;
			int ny = m * j;
			if (abs(i) % 2 == 1)
				nx += n - 1 - x;
			else
				nx += x;
			if (abs(j) % 2 == 1)
				ny += m - 1 - y;
			else
				ny += y;

			int xx = nx - x;
			int yy = ny - y;
			int g = gcd(abs(xx), abs(yy));
			xx /= g;
			yy /= g;

			if ((x - nx) * (x - nx) + (y - ny) * (y - ny) <= d * d) {
				if (used.count(mp(xx, yy)))
					continue;
				used.insert(mp(xx, yy));
				ans++;
			}
		}

	cout << ans << endl;
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
	
	int tt;
	cin >> tt;
	forn(ii, tt) {
		read();
		printf("Case #%d: ", ii + 1);
		solve();
	}
	
	return 0;
}