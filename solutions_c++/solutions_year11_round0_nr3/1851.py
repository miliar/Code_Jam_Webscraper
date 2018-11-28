#include <string>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))


/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

const int MAX = (1<<21) + 100;
int val[2000], N;
int t[20][MAX];
void solve()
{
	scanf("%d", &N);
	REP(i, N) scanf("%d", &val[i]);
	int sum = 0, mn = INF, xo  = 0;
	REP(i, N) {
		sum += val[i];
		mn = min(mn, val[i]);
		xo ^= val[i];
	}
	
	if(xo != 0) printf("NO\n");
	else printf("%d\n", sum - mn);
}

int main(void)
{
	int T = RI();
	FOR(i,1,T) {
		printf("Case #%d: ", i);
        solve();
	}
	return (0);
}
