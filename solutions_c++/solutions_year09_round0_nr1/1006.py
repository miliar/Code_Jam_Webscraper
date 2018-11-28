#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <bitset>
#include <limits>
#include <iterator>
#include <sstream>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i != _b; ++i)
#define REP(i, N) FOR(i, 0, N)
#define REPK(K) REP(_crazyName, K)

#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()

template<typename CType, typename VType>
inline void REMOVE(CType &container, const VType &value) {
	container.erase(remove(ALL(container), value), container.end());
}

#define sz() size()
#define len() length()
#define mp(a, b) make_pair(a, b)
#define pb(x) push_back(x)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef long long LL;

bool match(const string &str, const vector< vector<char> > &pattern) {
	if (str.len() != pattern.sz())
		return false;

	REP (i, str.len())
		if (find(ALL(pattern[i]), str[i]) == pattern[i].end())
			return false;
	return true;
}

int main() {
	int L, D, N;
	cin >> L >> D >> N;

	vector<string> dictionary;

	REP (i, D) {
		string str;
		cin >> str;
		dictionary.pb(str);
	}

	FOR (kase, 1, N + 1) {
		string str;
		cin >> str;

		vector< vector<char> > pattern;

		bool inParens = false;
		REP (j, str.len()) {
			if (str[j] == '(') {
				pattern.pb(vector<char>());
				inParens = true;
			}
			else if (str[j] == ')') {
				inParens = false;
			}
			else {
				if (inParens)
					pattern.back().pb(str[j]);
				else
					pattern.pb(vector<char>(1, str[j]));
			}
		}

		int ret = 0;
		REP (i, dictionary.sz())
			ret += match(dictionary[i], pattern);

		cout << "Case #" << kase << ": " << ret << endl;
	}
}






























