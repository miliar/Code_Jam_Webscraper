#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
#include <memory.h>
#include <ctype.h>

#include <iostream>

#include <string>
#include <complex>
#include <numeric>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>

//#pragma comment(linker, "/stack:64000000")

using namespace std;

template<typename TYPE> inline TYPE sqr(const TYPE& a) { return (a) * (a); }

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))

typedef long long li;
typedef double ld;
typedef pair<int, int> pt;

const int INF = 1000 * 1000 * 1000;
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 1020;

pair<int, int> seg[N];

void solve(int it) {
	int X, S, R, t, n;
	scanf("%d%d%d%d%d\n", &X, &S, &R, &t, &n);
	int norm = X;
	forn(i, n) {
		int b, e, w;
		scanf("%d%d%d\n", &b, &e, &w);
		seg[i] = mp(w, e - b);
		norm -= e - b;
	}
	seg[n++] = mp(0, norm);
	sort(seg, seg + n);

	ld ans = 0;
	ld rt = t;
	forn(i, n) {
		ld v0 = (S + seg[i].first);
		if(rt > EPS) {
			ld v = (R + seg[i].first);
			ld len = rt * v;
			if(len >= seg[i].second) {
				len = seg[i].second;
				ld add = len / v;
				rt -= add;
				ans += add;
			} else {
				ld add = len / v;
				//rt -= add;
				rt = -1;
				ans += add;
				add = (seg[i].second - len) / v0;
				ans += add;
			}
		} else {
			ld add = seg[i].second / v0;
			ans += add;
		}
	}
	
	printf("Case #%d: %.9lf\n", it, ans);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

  	int test;
  	scanf("%d\n", &test);
  	for1(it, test) {
  		solve(it);
  	}

	return 0;
}
