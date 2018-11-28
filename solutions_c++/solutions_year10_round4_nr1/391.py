/*
 * main.cpp
 *
 *  Created on: 2010-6-5
 *      Author: haying
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i, b, e) for (int i = (b), _e = e; i < _e; i ++)
#define REP(i, n) FOR(i, 0, (n))
#define FOR_REV(i, rb, b) for (int i = (rb), _b = (b); i >= _b; i --)

#define sz size()
template<class T> inline int size(const T &c) { return c.sz; }
#define FOR_EACH(i, c) REP(i, size(c))

#define itype(c) __typeof((c).begin())
#define ITER(it, c) for(itype(c) it = (c).begin(); it != (c).end(); it ++)

#define pb push_back
#define pf push_front
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define REVERSE(c) reverse(all(c))

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i >> x; return x; }
template <class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define PI acos(-1.)
#define EPS 1e-308
#define INT_INF static_cast<int>((1LL << (sizeof(int) * 8 - 1)) - 1)
int A[60][60];
int B[60][60];
int k;
bool test1(int ans) {
	FOR(i, 0, k - ans) {
		FOR(j, ans + i, k) {
			if (A[i][j] != A[j - ans][i + ans]) {
				return false;
			}
		}
	}
	return true;
}
bool test2(int ans) {
	FOR(i, ans, k) {
		FOR(j, 0, k - ans) {
			if (A[i][j] != A[j + ans][i - ans]) {
				return false;
			}
		}
	}
	return true;
}
bool test3(int ans) {
	FOR(i, 0, k - ans) {
		FOR(j, ans + i, k) {
			if (B[i][j] != B[j - ans][i + ans]) {
				return false;
			}
		}
	}
	return true;
}
bool test4(int ans) {
	FOR(i, ans, k) {
		FOR(j, 0, k - ans) {
			if (B[i][j] != B[j + ans][i - ans]) {
				return false;
			}
		}
	}
	return true;
}
int main() {
	int T, case_num = 0;
	cin >> T;
	while (T != case_num ++) {
		cin >> k;
		REP(i, k) {
			REP(j, i + 1) {
				int a;
				cin >> a;
				A[i - j][j] = a;
			}
		}
		FOR(i, k, 2 * k - 1) {
			REP(j, k - 1 - (i - k)) {
				int a;
				cin >> a;
				A[k - 1 - j][i + j - k + 1] = a;
			}
		}
		REP(i, k) {
			REP(j, k) {
				B[k - 1 - j][i] = A[i][j];
			}
		}
		int ans;
		int ans1 = 0;
		int ans2 = 0;
		REP(i, k) {
			ans1 = i;
			if (test1(i) || test2(i)) {
				break;
			}
		}
		REP(i, k) {
			ans2 = i;
			if (test3(i) || test4(i)) {
				break;
			}
		}
		ans = ans1 + ans2;
		ans = (ans + k) * (ans + k) - k * k;
		cout << "Case #" << case_num << ": " << ans << "\n";
	}
	return 0;
}
