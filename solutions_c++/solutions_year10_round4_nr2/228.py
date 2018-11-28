#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <cstdarg>

#ifndef DBG
#define	DBG	0
#endif

//#define	DBG(f,x)	if(_____debug & f) { x; }
using namespace std;

#define	rep(i,n)	for((i) = 0; (i) < (n); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define all(v)		(v).begin(),(v).end()
#define	Fi(n)		rep(i,n)
#define	Fj(n)		rep(j,n)
#define	Fk(n)		rep(k,n)
#define	sz(v)		(v).size()

#define	INF	1000000000

// {{{ gprintf for debugging
bool gprintf(int debug,const char *format,...) {
	if(DBG & debug) {
		va_list	listpointer;

		va_start(listpointer, format);
		vfprintf(stderr,format,listpointer);
		va_end(listpointer);

		return true;
	}
	else
		return false;
}
// }}}

long long	tree[15][1 << 15];
long long	M[1 << 15];
int		P;

long long	cache[11][1 << 10][11];

long long memo(int level,int node,int missed) {
	long long	&r = cache[level][node][missed];

	if(r >= 0) return r;

	if(level == P) {
		return (missed > M[node]) ? INF : 0;
	}

	r = INF;

	long long	c;

	c = memo(level + 1,2 * node,missed + 1) + memo(level + 1,2 * node + 1,missed + 1);
	r = min(r,c);

	c = tree[level][node] + memo(level + 1,2 * node,missed) + memo(level + 1,2 * node + 1,missed);
	r = min(r,c);

	return r;
}
int main()
{
	int	T,cs;
	int	i,j,k;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d",&P);

		Fi(1 << P) scanf("%lld",&M[i]);

		for(i = P - 1; i >= 0; i--) {
			k = 1 << i;

			Fj(k) scanf("%lld",&tree[i][j]);
		}

		memset(cache,-1,sizeof(cache));

		printf("Case #%d: %lld\n",cs,memo(0,0,0));
	}
	return 0;
}
