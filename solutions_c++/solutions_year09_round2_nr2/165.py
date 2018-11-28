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

int main() {
	int T;
	scanf("%d", &T);

	REP (kase, T) {
		string str;
		cin >> str;
		string str2 = str;

		if (!next_permutation(ALL(str))) {
			str2 += '0';
			sort(ALL(str2));

			REP (i, str2.len()) {
				if (str2[i] != '0') {
					swap(str2[i], str2[0]);
					break;
				}
			}

			str = str2;
		}

		cout << "Case #" << (kase + 1) << ": " << str << endl;
	}
}
