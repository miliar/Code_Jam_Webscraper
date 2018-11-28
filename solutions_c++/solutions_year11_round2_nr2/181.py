// GCJ Round 1B - Problem B
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
bool can(LL t, LL d, VI v)
{
	LL pos = v[0] - t;
	int n = v.size();
	for (int i=1; i<n; i++)
	{
		pos = max(pos + d, v[i] - t);
		if (abs(pos - v[i]) > t)
			return false;
	}
	return true;
}
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		printf("Case #%d: ", tkase+1);
		int c, d;
		cin >> c >> d;
		vector<int> v;
		for (int i=0; i<c; i++)
		{
			int a, b;
			cin >> a >> b;
			for (int i=0; i<b; i++)
				v.push_back(2*a);
		}
		sort(v.begin(), v.end());
		LL lower = 0, upper = OO;
		while (lower < upper)
		{
			LL mid = (lower + upper) / 2;
			if (can(mid, 2 * d, v))
				upper = mid;
			else
				lower = mid + 1;
		}
		printf("%Lf\n", (long double)lower*0.5);
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
