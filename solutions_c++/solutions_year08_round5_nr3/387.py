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
	int cas; cin>>cas;
	REP(ca,cas)
	{
		int M, N; cin>>M>>N;
		vector<string> S(M);
		REP(i,M) cin>>S[i];

		vector<int> P(1<<N,0);
		REP(zz,M)
		{
			vector<int> Q(1<<N,0);

			REP(m,(1<<N)) REP(k,(1<<N))
			{
				int c=0, t=1;
				REP(i,N) if (m&(1<<i))
				{
					c++;
					if (S[zz][i]=='x') t=0;
					if (i+1<N) if (m&(1<<(i+1))) t=0;
					if (i+1<N) if (k&(1<<(i+1))) t=0;
					if (i-1>=0) if (m&(1<<(i-1))) t=0;
					if (i-1>=0) if (k&(1<<(i-1))) t=0;
				}
				if (t) Q[m] >?= P[k]+c;
			}
			P=Q;
		}

		int res=0;
		REP(m,(1<<N)) res>?=P[m];
		printf("Case #%d: %d\n", ca+1, res);
	}

	return 0;
}
