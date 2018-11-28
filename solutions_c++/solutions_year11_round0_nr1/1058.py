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

// for loops
#define FOR(i, b, e) for (int i = (b), _e = e; i < _e; i ++)
#define REP(i, n) FOR(i, 0, (n))
#define FOR_REV(i, rb, b) for (int i = (rb), _b = (b); i >= _b; i --)

// for each
#define sz size()
template<class T> inline int size(const T &c) { return c.sz; }
#define FOR_EACH(i, c) REP(i, size(c))

// iterating stl containers
#define itype(c) __typeof((c).begin())
#define ITER(it, c) for(itype(c) it = (c).begin(); it != (c).end(); it ++)

// sort and reverse containers
#define pb push_back
#define pf push_front
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define REVERSE(c) reverse(all(c))

// vectors and string streams
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i >> x; return x; }
template <class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

// special values
#define PI acos(-1.)
#define EPS 1e-308
#define INT_INF static_cast<int>((1LL << (sizeof(int) * 8 - 1)) - 1)

int main() {
	int T, case_num = 0;
	cin >> T;
	while (T != case_num ++) {
		int B_pos_last_push = 1;
		int B_time_last_push = 0;
		int O_pos_last_push = 1;
		int O_time_last_push = 0;
		int ans = 0;
		int N;
		cin >> N;
		char ID;
		int pos;
		REP(i, N) {
			cin >> ID >> pos;
			if (ID == 'B') {
				// need extra time to move and push
				if (abs(pos - B_pos_last_push) + 1 > ans - B_time_last_push) {
					ans = abs(pos - B_pos_last_push) + 1 + B_time_last_push;
					B_time_last_push += abs(pos - B_pos_last_push) + 1;
				} else {
					ans = B_time_last_push = ans + 1;
				}
				B_pos_last_push = pos;
			} else {
				// need extra time to move and push
				if (abs(pos - O_pos_last_push) + 1 > ans - O_time_last_push) {
					ans = abs(pos - O_pos_last_push) + 1 + O_time_last_push;
					O_time_last_push += abs(pos - O_pos_last_push) + 1;
				} else {
					ans = O_time_last_push = ans + 1;
				}
				O_pos_last_push = pos;
			}
		}
		cout << "Case #" << case_num << ": " << ans << "\n";
	}
	return 0;
}
