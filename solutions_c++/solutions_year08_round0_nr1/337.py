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
	char s[1000];
	fgets(s, 1000, stdin);

	int cas;
	sscanf(s, "%d", &cas);

	REP(ca,cas)
	{
		int N, Q;
		vector<string> pS;

		fgets(s, 1000, stdin);
		sscanf(s, "%d", &N);

		REP(i,N)
		{
			fgets(s, 1000, stdin);
			pS.push_back(string(s));
		}

		fgets(s, 1000, stdin);
		sscanf(s, "%d", &Q);

		vector<int> P(N,0);

		REP(i,Q)
		{
			fgets(s, 1000, stdin);
			string ss(s);

			int j=0;
			while (j<N) if (pS[j]==ss) break; else j++;

			int m=P[j]+2;
			REP(k,N) if (k!=j) m = min(m, P[k]+1);
			P[j]=m;
		}

		int m=P[0];
		REP(j,N) m=min(m,P[j]);
		printf("Case #%d: %d\n", ca+1, m);
	}

	return 0;
}
