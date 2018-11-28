#define _CRT_SECURE_NO_DEPRECATE

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



void solve() {
	int r;
	scanf("%d", &r);

	vector<pair<int, int> > v;
	forn(i, r) {
		int xl, xr, yl, yr;
		scanf("%d%d%d%d", &xl, &yl, &xr, &yr);
		if (xl > xr)
			swap(xl, xr);
		if (yl > yr)
			swap(yl, yr);

		for (int x = xl; x <= xr; x++)
			for (int y = yl; y <= yr; y++)
				v.pb(mp(x, y));
	}
	
	int ans = 0;
	while (!v.empty()) {
		sort(all(v));
		v.erase(unique(all(v)), v.end());

		ans++;

		vector<pair<int, int> > ne;
		forn(i, v.size()) {
			if (binary_search(all(v), mp(v[i].fs + 1, v[i].sc - 1)))
				ne.pb(mp(v[i].fs + 1, v[i].sc));
			if (binary_search(all(v), mp(v[i].fs - 1, v[i].sc + 1)))
				ne.pb(mp(v[i].fs, v[i].sc + 1));
			if (binary_search(all(v), mp(v[i].fs - 1, v[i].sc)) || binary_search(all(v), mp(v[i].fs, v[i].sc - 1)))
				ne.pb(v[i]);
		}

		v.swap(ne);
	}

	cout << ans;
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		cerr << ii << endl;

		printf("Case #%d: ", ii + 1);

		solve();

		puts("");
	}
	
	return 0;
}