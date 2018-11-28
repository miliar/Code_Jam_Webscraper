#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <complex>
#include <utility>
#include <limits>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
using namespace std;

#define rep(i,a,b) for(int i=(a);i<(b);++i)
#define clr(a,v) memset((a),(v),sizeof(a))
#define all(a) (a).begin(), (a).end()
#define siz(a) ((int)(a).size())
#define pub push_back
#define puf push_front
#define pob pop_back
#define pof pop_front

template <typename T> inline T sqr(T const& t) { return t * t; }
template <typename T> inline bool setmin(T& a, T const& b) { if (b < a) { a = b; return true; } else return false; }
template <typename T> inline bool setmax(T& a, T const& b) { if (a < b) { a = b; return true; } else return false; }

template <typename A, typename B> inline A _0(pair<A, B> const& p) { return p.first; }
template <typename A, typename B> inline B _1(pair<A, B> const& p) { return p.second; }
template <typename A> inline A _0(complex<A> const& z) { return z.real(); }
template <typename A> inline A _1(complex<A> const& z) { return z.imag(); }
template <typename A> inline A _0(A* a) { return a[0]; }
template <typename A> inline A _1(A* a) { return a[1]; }

typedef pair <int, int> pii;
typedef vector <int> vint;
typedef set <int> sint;
typedef map <int, int> mint;
typedef long long ll;
typedef long long unsigned ull;
typedef long double ld;

int const inf = 0x7f7f7f7f;
ll const llinf = 0x7f7f7f7f7f7f7f7fll;
ld const pi = acos(-1.0l);

int const max_n = 1024;
int id[max_n];

bool by_speed(pair<ld, ld> const& a, pair<ld, ld> const& b) {
	return _1(a) < _1(b);
}
int ts = 0;
void doit() {
	ts++;
	int x, s, r, t, n;
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	int st, bi, ei, wi;
	vector<pair<ld, ld> > segments;
	st = 0;
	rep (i, 0, n) {
		scanf("%d%d%d", &bi, &ei, &wi);
		if (bi - st) {
			segments.pub(pii(bi - st, 0));
		}
		segments.pub(pii(ei - bi, wi));
		st = ei;
	}
	if (st != x) {
		segments.pub(pii(x - st, 0));
	}

	sort(all(segments), by_speed);
	ld res = 0;

	ld tt = t;
	rep (i, 0, siz(segments)) {
		start:
		if (tt <= 0.0l) {
			res += segments[i].first / (segments[i].second + s);
		}
		else {
			ld dt = segments[i].first / (segments[i].second + r);
			if (dt <= tt) {
				res += dt;
				tt -= dt;
			}
			else {
				res += tt;
				segments[i].first -= tt * (segments[i].second + r);
				tt = 0.0;
				goto start;
			}
		}
	}

	printf("Case #%d: %.7lf\n", ts, double(res)); 
}

int main() {
	int t; cin >> t;
	while(t--) doit();
	return 0;
}