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

int	pixels[1000];
int	N;
int	D,I,M;

int	min_cost[200][256];

int memo(int pos,int last) {
	if(pos >= N) return 0;

	int	&r = min_cost[pos][last];
	int	c;
	int	i;
	if(r >= 0) return r;

	r = 1000000000;

	// delete;
	c = memo(pos+1,last) + D;
	r = min(r,c);

	rab(i,0,255) {
		if(labs(i - last) > M) continue;
		// insert
		c = I + memo(pos,i);
		r = min(r,c);

		// change
		c = labs(pixels[pos] - i) + memo(pos + 1,i);
		r = min(r,c);
	}

	return r;
}

int main()
{
	int	T,cs;
	int	i;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d %d %d",&D,&I,&M,&N);

		Fi(N) scanf("%d",&pixels[i]);

		memset(min_cost,-1,sizeof(min_cost));

		int	r = 1000000000,c;
		int	i;

		rab(i,0,255) {
			c = memo(0,i);
			r = min(r,c);
		}

		printf("Case #%d: %d\n",cs,r);
	}
	return 0;
}
