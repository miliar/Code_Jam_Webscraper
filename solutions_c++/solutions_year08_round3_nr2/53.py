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

typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VLL;
typedef vector<VI> VVI;
typedef vector<VLL> VVLL;

int main(void)
{
	int cas;
	cin>>cas;

	REP(ca,cas)
	{
		int N;
		string S;

		cin>>S; N=SIZE(S);

		VVI Z(N+1,VI(N+1,0));
		REP(j,N)
		{
			int z=0, i=j;
			while (i<N)
			{
				z=(10*z+(S[i]-'0'))%210;
				i++;
				Z[j][i]=z;
			}
		}

		VVLL P(N+1,VLL(210,0));

		FOR(i,1,N)
		{
			REP(j,i)
			{
				int z=Z[j][i];
				REP(k,210)
				{
					P[i][(k+210+z)%210] += P[j][k];
					P[i][(k+210-z)%210] += P[j][k];
				}
			}

			int z=Z[0][i];
			P[i][z] += 1;
		}

		ll r=0;
		REP(i,210) if (i%2==0 || i%3==0 || i%5==0 || i%7==0) r+=P[N][i];
		printf("Case #%d: %lld\n", ca+1, r);
	}

	return 0;
}
