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
		int P, K, L;
		scanf("%d %d %d ", &P, &K, &L);

		vector<int> p(L,0);
		REP(i,L) scanf("%d ", &p[i]);
		sort(p.begin(), p.end(), greater<int>());

		long long r=0, a=0;
		REP(i,L)
		{
			if (i%K==0) a++;
			if (a>P) { r=-1; break; }
			r+=a*p[i];
		}

		printf("Case #%d: ", ca+1);
		if (r<0) printf("Impossible\n");
		else printf("%lld\n", r);
	}

	return 0;
}
