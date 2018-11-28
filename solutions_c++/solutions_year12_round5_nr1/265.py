// GCJ Round 3 - Problem A
// -- strapahuulius

// pre-written code follows
// #includes {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// }}}
// constants, typedefs, macros {{{
typedef long long LL;
typedef unsigned long long ULL;
const int oo = 1000000000;
const LL OO = 1000000000000000000LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef queue<int> QI;
typedef queue<PII> QPII;
typedef complex<double> tComp;
const double PI = 2.0 * acos(0.0);
const double EPS = 1e-9;
#define FORIT(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define CERR(x) cerr << (#x) << " = " << (x) << endl
#define COUT(x) cout << (#x) << " = " << (x) << endl
// }}}

// code written during the competition follows
struct Level
{
	int ix;
	LL p, len;
	Level() {}
	bool operator<(const Level &l) const
	{
		LL a = (100 - p) * (l.len + len) + p * len;
		LL b = 10000 - p - (100 - l.p);
		LL c = (100 - l.p) * (l.len + len) + p * l.len;
		LL d = 10000 - l.p - (100 - p);
//		if (a / b < c / d)
		if (a * d == c * b)
			return ix < l.ix;
		return a * d < c * b;
	}
};
int main(int argc, char **argv)
{
	int kase;
	int n_read = scanf("%d\n", &kase);
	assert(n_read == 1);
	int kase_a = 0, kase_b = oo;
	if (argc > 1)
	{
		assert(argc == 3);
		int n_read = sscanf(argv[1], "%d", &kase_a);
		assert(n_read == 1);
		n_read = sscanf(argv[1], "%d", &kase_b);
		assert(n_read == 1);
		if (kase_a >= kase)
			return 0;
	}
	for (int tkase=0; tkase<kase; tkase++)
	{
		// read case
		int n;
		cin >> n;
		vector<Level> level(n);
		for (int i=0; i<n; i++)
		{
			level[i].ix = i;
			cin >> level[i].len;
		}
		for (int i=0; i<n; i++)
		{
			cin >> level[i].p;
		}
		if (tkase < kase_a || tkase >= kase_b)
			continue;
		// process case
		sort(level.begin(), level.end());
		printf("Case #%d:", tkase+1);
		for (int i=0; i<n; i++)
			cout << " " << level[i].ix;
		cout << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
