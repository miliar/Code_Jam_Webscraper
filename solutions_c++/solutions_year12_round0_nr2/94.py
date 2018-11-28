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

int n, s, p, t[1100];

void read() {
	cin >> n >> s >> p;
	forn(i, n)
		cin >> t[i];
}

void solve() {
	int ans = 0;
	forn(ii, n) {
		int val = t[ii];
		bool free = false, nonfree = false;
		forn(i1, 11)
			forn(i2, 11)
				forn(i3, 11) {
					if (i1 + i2 + i3 != val)
						continue;

					int ma = max(max(i1, i2), i3);
					int mi = min(min(i1, i2), i3);

					if (ma > mi + 2)
						continue;

					if (ma < p)
						continue;

					if (ma < mi + 2)
						free = true;
					else
						nonfree = true;
				}

		if (free)
			ans++;
		else
		if (nonfree && s) {
			s--;
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