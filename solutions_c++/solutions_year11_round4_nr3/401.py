// GCJ Round 2 - Problem C
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
	const int M = 2000000;
	VI c(M+1);
	VI primes;
	for (int i=2; i<M; i++)
		if (!c[i])
		{
			primes.push_back(i);
			for (int j=2*i; j<M; j+=i)
				c[j] = 1;
		}
	int kase;
	scanf("%d\n", &kase);
	for (int tkase=0; tkase<kase; tkase++)
	{
		LL n;
		cin >> n;
		LL total = 1;
		FORIT(it, primes)
		{
			LL p = *it;
			LL q = p * p;
			if (q > n)
				break;
			LL m = n;
			while (m >= p)
			{
				m /= p;
				total++;
			}
			total--;
		}
		printf("Case #%d: ", tkase+1);
		if (n == 1)
			total = 0;
		cout << total << endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
