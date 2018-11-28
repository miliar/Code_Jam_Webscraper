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

typedef complex<ll> point;

int const max_n = 512;


int R, C, D;
ll a[max_n][max_n];

point gmass(int i, int j, int k, ll& mass) {
	point r = 0;
	mass = 0;

	rep (ii, 0, k) rep (jj, 0, k) {
		r += point(i + ii, j + jj) * a[i + ii][j + jj];
		mass += a[i + ii][j + jj];
	}

	r -= point(i, j) * a[i][j] + point(i + k-1, j) * a[i + k-1][j] + point(i, j + k-1) * a[i][j + k-1] + point(i + k-1, j + k-1) * a[i + k-1][j + k-1]; 
	mass -= a[i][j] + a[i + k-1][j] + a[i][j + k-1] + a[i + k-1][j + k-1];

	return r;
}

int tc = 0;

void doit() {
	cin >> R >> C >> D;
	rep (i, 0, R) {
		rep (j, 0, C) {
			char c; cin >> c;
			a[i][j] = 1 + c - '0';
		}
	}

	for (int k = min(R, C); k >= 3; -- k) {
		for (int i = 0; i + k <= R; ++ i) {
			for (int j = 0; j + k <= C; ++ j) {
				ll mass;
				point p = gmass(i, j, k, mass);

				if (mass * point(i * 2 + (k - 1), j * 2 + (k - 1)) == ll(2) * p) {
					printf("Case #%d: %d\n", ++ tc, k);
					return;
				}
			}
		}
	}

	printf("Case #%d: IMPOSSIBLE\n", ++ tc);
}

int main() {
	int t; scanf("%d", &t);
	while(t--) doit();
	return 0;
}