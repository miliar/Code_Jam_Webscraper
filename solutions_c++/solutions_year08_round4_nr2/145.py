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
	scanf("%d ", &cas);

	REP(ca,cas)
	{
		int N, M, A;
		scanf("%d %d %d ", &N, &M, &A);

		printf("Case #%d: ", ca+1);
		if (A>N*M) printf("IMPOSSIBLE");
		else if (A==M*N) printf("%d %d %d %d %d %d", 0,0, N,0, 0,M);
		else if (A<=N) printf("%d %d %d %d %d %d", 0,0, A,0, 0,1);
		else if (A<=M) printf("%d %d %d %d %d %d", 0,0, 1,0, 0,A);
		else
		{
			int l=A/N, k=A%N;
			printf("%d %d %d %d %d %d", 0,1, N,0, k,l+1);
		}

		printf("\n");
	}

	return 0;
}
