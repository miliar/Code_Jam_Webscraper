// GCJ Round 2 - Problem A
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
int main()
{
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		double x, s, r, t;
		int n;
		cin >> x >> s >> r >> t >> n;
		r -= s;
		vector<pair<double, double> > v;
		for (int i=0; i<n; i++)
		{
			double b, e, w;
			cin >> b >> e >> w;
			v.push_back(make_pair(w + s, e - b));
			x -= e-b;
		}
		if (x > 0)
		{
			v.push_back(make_pair(s, x));
			n++;
		}
		sort(v.begin(), v.end());
		double total = 0.0;
		for (int i=0; i<n; i++)
		{
			double t0 = v[i].second / v[i].first;
			double tmax = min(t0, t);
			tmax = min(tmax, v[i].second / (v[i].first + r));
			t -= tmax;
			total += tmax;
			total += (v[i].second - (v[i].first + r) * tmax) / v[i].first;
		}
		printf("Case #%d: %.9lf\n", tkase+1, total);
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
