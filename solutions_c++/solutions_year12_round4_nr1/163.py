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
		int n, D;
		cin >> n;
		VI d(n), len(n);
		for (int i=0; i<n; i++)
		{
			cin >> d[i] >> len[i];
		}
		cin >> D;
		vector<int> max_swing(n);
		max_swing[0] = min(len[0], d[0]);
		priority_queue<PII> pq;
		pq.push(PII(min(len[0], d[0]), 0));
		while (!pq.empty())
		{
			PII act = pq.top();
			pq.pop();
			int ix = act.second;
			int l = act.first;
			if (l < max_swing[ix])
				continue;
			for (int i=0; i<n; i++)
			{
				if (abs(d[i] - d[ix]) > l)
					continue;
				int nl = min(len[i], abs(d[i] - d[ix]));
				if (nl > max_swing[i])
				{
					max_swing[i] = nl;
					pq.push(PII(nl, i));
				}
			}
		}
		bool good = false;
		for (int i=0; i<n; i++)
			if (abs(d[i] - D) <= max_swing[i])
			{
				good = true;
				break;
			}
		printf("Case #%d: ", tkase+1);
		cout << (good ? "YES" : "NO") << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
