#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <functional>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>

#define FOR(i, a, b) for (int (i) = (a), _b = (b); (i) < _b; ++(i))
#define REP(i, N) FOR(i, 0, N)
#define ALL(x) (x).begin(), (x).end()
#define sz() size()
#define pb(x) push_back(x)
#define mp(a, b) make_pair(a, b)

using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<bool> VB;

typedef long long LL;
typedef unsigned long long ULL;

int calc(int a, int b) {
	if (b < a) return calc(b, a);
	if (a == b) return 0;
	if (a == 1) return 1;
	if (b % a == 0) return 1;

	bool ret = false;
	if (a + b % a != b) ret = ret || !calc(a + b % a, a);
	ret = ret || !calc(b % a, a);
	return ret;
}

int main() {
	int T;
	cin >> T;

	FOR (kase, 1, T + 1) {
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;

		int ret = 0;
		FOR (i, A1, A2 + 1)
			FOR (j, B1, B2 + 1)
				ret += calc(i, j);

		cout << "Case #" << kase << ": " << ret << endl;
	}
}
