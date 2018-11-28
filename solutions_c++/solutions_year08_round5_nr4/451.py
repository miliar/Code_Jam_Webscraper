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

int BASE=10007;

typedef vector<int> VI;
typedef vector<VI> VVI;

int main(void)
{
	int cas;cin>>cas;
	REP(ca,cas)
	{
		int H, W, R; cin>>H>>W>>R;
		VVI M(H,VI(W,-1));

		REP(i,R)
		{
			int r, s; cin>>r>>s; M[r-1][s-1]=0;
		}

		REP(r,H) REP(s,W) if (M[r][s]==-1)
		{
			if (r==0 && s==0) M[r][s]=1; else M[r][s]=0;

			int r2=r-1, s2=s-2;
			if (r2>=0 && s2>=0) M[r][s] = (M[r][s]+M[r2][s2])%BASE;

			r2=r-2, s2=s-1;
			if (r2>=0 && s2>=0) M[r][s] = (M[r][s]+M[r2][s2])%BASE;
		}

		printf("Case #%d: %d\n", ca+1, M[H-1][W-1]);
	}

	return 0;
}
