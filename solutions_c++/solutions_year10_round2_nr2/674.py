/*
 * main.cpp
 *
 *  Created on: 2010-5-23
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

int main() {
	int C, case_num = 0;
	cin >> C;
	while (C != case_num ++) {
		int N, K, B, T;
		cin >> N >> K >> B>> T;
		VI X(N, 0), V(N, 0);
		REP(i, N) {
			cin >> X[i];
		}
		REP(i, N) {
			cin >> V[i];
		}
		int ans = 0;
		int delta = 0;
		int finish = 0;
		FOR_REV(i, N - 1, 0) {
			if (B <= X[i] + V[i] * T) {
				finish ++;
				ans += delta;
				if (finish >= K) {
					break;
				}
			}
			else {
				delta ++;
			}
		}
		if (finish < K) {
			cout << "Case #" << case_num << ": IMPOSSIBLE\n";
		}
		else {
			cout << "Case #" << case_num << ": " << ans << "\n";
		}
	}
	return 0;
}
