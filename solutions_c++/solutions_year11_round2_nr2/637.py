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

int const max_c = 256;
int p[max_c], v[max_c];

int tc = 0;
int c, d;

bool can(int t) {
	int w = p[0] - t;
	rep (i, 0, c) {
		rep (j, 0, v[i]) {
			if (i == 0 && j == 0) {
				continue;
			}
			
			if (p[i] + t - w < d) {
				return false;
			}

			w = max(w + d, p[i] - t);
		}
	}

	return true;
}

void doit() {
	cin >> c >> d;
	ld ans;
	d *= 2;
	rep (i, 0, c) {
		cin >> p[i] >> v[i];
		p[i] *= 2;
	}

	if (can(0)) {
		ans = 0.0l;
	}
	else if (can(1)) {
		ans = 0.5l;
	}
	else {
		int t = 1;
		while (!can(t)) {
			t *= 2;
		}
		int l = 1, r = t, m;
		while (l + 1 != r) {
			m = (l + r) / 2;
			if (can(m)) {
				r = m;
			}
			else {
				l = m;
			}
		}

		ans = ld(r) * 0.5l;
	}

	cout << "Case #" << ++tc << ": " << ans << endl; 
}

int main() {
	int t; cin >> t;
	while (t--) doit();
}
