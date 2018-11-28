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
namespace __gnu_cxx {
template<> struct hash<std::string>  {
	size_t operator()(const std::string& s) const {
		return __stl_hash_string(s.c_str());
	}
};
}
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
		int N;
		cin >> N;
		VS M;
		vector<double> ans;
		vector<double> WP;
		vector<double> OWP;
		vector<double> OOWP;
		vector<double> N_OPPO;
		M.resize(N);
		ans.resize(N, 0);
		WP.resize(N, 0);
		OWP.resize(N, 0);
		OOWP.resize(N, 0);
		N_OPPO.resize(N, 0);
		REP(i, N) {
			cin >> M[i];
			double n0 = 0;
			double n1 = 0;
			N_OPPO[i] = N;
			REP(pos, N) {
				if (M[i][pos] == '1') { n1 ++; }
				else if (M[i][pos] == '0') { n0 ++; }
				else { N_OPPO[i] --; }
			}
			WP[i] = n1 / (n0 + n1);
		}
		REP(i, N) {
			REP(j, N) {
				if (M[i][j] == '.') { continue; }
				double n0 = 0;
				double n1 = 0;
				REP(pos, N) {
					if (pos == i) { continue; }
					if (M[j][pos] == '1') { n1 ++; }
					else if (M[j][pos] == '0') { n0 ++; }
				}
				OWP[i] += n1 / (n0 + n1);
			}
			OWP[i] /= N_OPPO[i];
		}
		REP(i, N) {
			REP(pos, N) {
				if (M[i][pos] != '.') {
					OOWP[i] += OWP[pos];
				}
			}
			OOWP[i] /= N_OPPO[i];
		}
		REP(i, N) {
			ans[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		}
		cout << "Case #" << case_num << ":\n";
		REP(i, N) {
			cout << ans[i] << endl;
//			cout << WP[i] << endl;
//			cout << OWP[i] << endl;
//			cout << OOWP[i] << endl;
		}
	}
	return 0;
}
