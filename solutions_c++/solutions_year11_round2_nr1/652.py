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

int const max_n = 128;
char mat[max_n][max_n];
int played[max_n], won[max_n];
ld wp[max_n], owp[max_n], oowp[max_n];
int tc = 0;
void doit() {
	int n; cin >> n;
	rep (i, 0, n) rep (j, 0, n) cin >> mat[i][j];
	rep (i, 0, n) {
		played[i] = won[i] = 0;
		rep (j, 0, n) {
			if (mat[i][j] != '.') {
				++ played[i];
				if (mat[i][j] == '1') {
					++ won[i];
				}
			}
		}

		if (played[i]) {
			wp[i] = ld(won[i]) / played[i];
		}
		else {
			wp[i] = 0.0l;
		}
	}

	rep (i, 0, n) {
		owp[i] = 0.0l;
		int against = 0;
		rep (j, 0, n) {
			if (mat[i][j] != '.') {
				if (mat[i][j] == '1') {
					if (played[j] > 1) {
						owp[i] += ld(won[j]) / (played[j] - 1);
					}
				}
				else {
					if (played[j] > 1) {
						owp[i] += ld(won[j] - 1) / (played[j] - 1);
					}
				}
				++ against;
			}
		}
		
		if (against) {
			owp[i] /= against;
		}
	}

	rep (i, 0, n) {
		oowp[i] = 0.0l;
		int opponents = 0;
		rep (j, 0, n) {
			if (mat[i][j] != '.') {
				oowp[i] += owp[j];
				++ opponents;
			}
		}

		if (opponents) {
			oowp[i] /= opponents;
		}
	}

	cout << "Case #" << ++tc << ":" << endl;

	rep (i, 0, n) {
		cout << fixed << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
	}
}

int main() {
	cout.precision(10);
	int t; cin >> t;
	while (t--) doit();
	return 0;
}
