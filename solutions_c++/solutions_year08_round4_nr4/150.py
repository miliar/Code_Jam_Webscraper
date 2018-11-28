/* #define DBG {{{ */
#ifdef D
#undef D
#define DBG if (1)
#else
#define DBG if (0)
#endif
/* }}} */

/* standard includes {{{ */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cmath>
#include <complex>

#include <iostream>
#include <sstream>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/* }}} */

/* defines: REP, FOR, FORD, FORE, FORER, CLEAR, SIZE {{{ */
#define REP(i,n) for (__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for (__typeof(b) i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (__typeof(a) i=(a); i>=(b); --i)
#define FORE(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define FORER(it,c) for (__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define CLEAR(t,v) memset((t),v,sizeof(t))
#define SIZE(c) ((int)((c).size()))
/* }}} */

int main(void)
{
	int cas;
	cin>>cas;

	REP(ca,cas)
	{
		int k;
		cin>>k;

		string s;
		cin>>s;

		vector<int> P(k);
		REP(i,k) P[i]=i;

		int mc=100000;
		do {
			int c=0;
			char l=' ';
			REP(i,SIZE(s))
			{
				int j=(i/k)*k+P[i%k];
				if (s[j]!=l) l=s[j], c++;
			}
			mc = min(c,mc);
		}
		while (next_permutation(P.begin(), P.end()));

		printf("Case #%d: %d\n", ca+1, mc);
	}

	return 0;
}
