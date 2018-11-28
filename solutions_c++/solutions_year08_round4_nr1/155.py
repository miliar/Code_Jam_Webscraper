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
		int M, V, VELA=100000;
		scanf("%d %d ", &M, &V);
		int m=(M-1)/2;

		vector<int> p(M), c(M), v0(M), v1(M);

		REP(i,m)
		{
			scanf("%d %d ", &p[i], &c[i]);
		}
		REP(i,m+1)
		{
			int t;
			scanf("%d ", &t);
			v0[m+i]=VELA; v1[m+i]=VELA;
			if (t==1) v1[m+i]=0; else v0[m+i]=0;
		}
		FORD(i,m-1,0)
		{
			int l=2*i+1, r=2*i+2;
			v1[i]=VELA; v0[i]=VELA;

			if (p[i]==1 || c[i]==1) // and
			{
				v1[i] = min(v1[i], v1[l]+v1[r]+(p[i]!=1));
				v0[i] = min(v0[i], v0[l]+v1[r]+(p[i]!=1));
				v0[i] = min(v0[i], v1[l]+v0[r]+(p[i]!=1));
				v0[i] = min(v0[i], v0[l]+v0[r]+(p[i]!=1));
			}
			if (p[i]==0 || c[i]==1)
			{
				v1[i] = min(v1[i], v1[l]+v1[r]+(p[i]!=0));
				v1[i] = min(v1[i], v0[l]+v1[r]+(p[i]!=0));
				v1[i] = min(v1[i], v1[l]+v0[r]+(p[i]!=0));
				v0[i] = min(v0[i], v0[l]+v0[r]+(p[i]!=0));
			}
		}

//		REP(i,M) printf("v0[%d]: %d, v1[%d]: %d\n", i, v0[i], i, v1[i]);

		int res = (V==0 ? v0[0] : v1[0]);
		if (res != VELA) printf("Case #%d: %d\n", ca+1, res);
		else printf("Case #%d: IMPOSSIBLE\n", ca+1);
	}

	return 0;
}
