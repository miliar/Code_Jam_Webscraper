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

// "combine pairs", stored both XY->Z and YX->Z for an input like XYZ
// (# of elements in map) = 2C, (# of searches) = roughly N
// TODO: to compare with only storing XY->Z
hash_map<string, char> combine;

// "pairs of opposed elements", stored both X->Y and Y->X for XY
// (# of elements in map) = 2D, (# of searches) <= (N - 1)
// TODO: to compare with many different implementations
multimap<char, char> opposed;

// a counter of base elements that are in the current element list
hash_map<char, int> counter;

// base elements
const int N_BASE = 8;
char base[N_BASE] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

int main() {
	// init counter
	counter.clear();

	int T, case_num = 0;
	cin >> T;
	while (T != case_num ++) {
		string ans = "";
		int C, D, N;
		string to_parsed;

		// --------------------------------------
		// combine pairs
		// --------------------------------------
		combine.clear();
		cin >> C;
		REP(i, C) {
			cin >> to_parsed;
			string key = to_parsed.substr(0, 2);
			char value = to_parsed[2];
			combine[key] = value;
			REVERSE(key);
			combine[key] = value;
		}

		// --------------------------------------
		// pairs of opposed elements
		// --------------------------------------
		opposed.clear();
		cin >> D;
		REP(i, D) {
			char l, r;
			cin >> to_parsed;
			l = to_parsed[0];
			r = to_parsed[1];
			opposed.insert(pair<char, char>(l, r));
			opposed.insert(pair<char, char>(r, l));
		}

		// --------------------------------------
		// element list
		// --------------------------------------
		char curr, last;
		// not to clear counter because we don't want to delete and insert
		REP(i, N_BASE) {
			counter[base[i]] = 0;
		}
		cin >> N;
		cin >> to_parsed;
		// first element
		curr = to_parsed[0];
		ans += curr;
		counter[curr] ++;
		// other elements
		FOR(i, 1, N) {
			curr = to_parsed[i];
			// skip if the list has just been cleared to nothing
			if (ans.size() == 0) {
				ans += curr;
				counter[curr] ++;
				continue;
			}
			// first, check if last is a base element
			last = *(ans.rbegin());
			if (counter.find(last) != counter.end()) {
				// if so, check combine
				string combine_key = "";
				combine_key += curr;
				combine_key += last;
				hash_map<string, char>::iterator combine_it =
						combine.find(combine_key);
				// replace "last" by a non-base element
				if (combine_it != combine.end()) {
					counter[last] --;
					*(ans.rbegin()) = combine_it->second;
					continue;
				}
			}
			// check opposed
			bool to_clear = false;
			typedef multimap<char, char>::iterator MMIT;
			pair<MMIT, MMIT> opposed_to_curr =
					opposed.equal_range(curr);
			// iterating each element that is opposed to "curr"
			for (MMIT opposed_it = opposed_to_curr.first;
					opposed_it != opposed_to_curr.second; opposed_it ++) {
				if (counter[opposed_it->second] != 0) {
					to_clear = true;
					break;
				}
			}
			if (to_clear) {
				ans = "";
				REP(i, N_BASE) {
					counter[base[i]] = 0;
				}
				continue;
			}
			// nothing happened, updating counter
			ans += curr;
			counter[curr] ++;
		}

		// --------------------------------------
		// formatting
		// --------------------------------------
		string formatted_ans = "[";
		if (ans.size() != 0) { formatted_ans += ans[0]; }
		FOR(i, 1, ans.size()) {
			formatted_ans += ", ";
			formatted_ans += ans[i];
		}
		formatted_ans += "]";

		// --------------------------------------
		// final output
		// --------------------------------------
		cout << "Case #" << case_num << ": " << formatted_ans << "\n";
	}
	return 0;
}
