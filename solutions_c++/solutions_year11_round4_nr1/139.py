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

vector<pair<pair<int, int>, int> > a;
int l[1100], r[1100], w[1100];

double cmp(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b) {
	return a.sc < b.sc;
}

void solve() {
	int x, s, R, n, t;
	a.clear();
	scanf("%d%d%d%d%d", &x, &s, &R, &t, &n);

	forn(i, n)
		scanf("%d%d%d", &l[i], &r[i], &w[i]);

	int la = 0;
	forn(i, n) {
		if (la != l[i])
			a.pb(mp(mp(la, l[i]), 0));
		a.pb(mp(mp(l[i], r[i]), w[i]));
		la = r[i];
	}

	if (la != x)
		a.pb(mp(mp(la, x), 0));

	sort(all(a), cmp);

	double ost = t;

	double ans = 0;
	forn(i, a.size()) {
		double take = min(ost, double(a[i].fs.sc - a[i].fs.fs) / (R + a[i].sc));
		ost -= take;
		ans += take + (double(a[i].fs.sc - a[i].fs.fs - take * (R + a[i].sc)) / (s + a[i].sc));
	}

	printf("%.6lf", ans);
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		printf("Case #%d: ", ii + 1);

		solve();

		puts("");
	}
	
	return 0;
}