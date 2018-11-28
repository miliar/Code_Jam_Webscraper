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

int main()
{
	int	T,cs;
	long long	R,k,N;
	deque <long long>	g;
	long long	p,e;
	int	i,j;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%lld %lld %lld",&R,&k,&N);

		g.clear();

		Fi(N) {
			scanf("%lld",&p);
			g.push_back(p);
		}

		e = 0;

		Fi(R) {
			p = 0;

			Fj(sz(g)) {
				if(p + g.front() > k) break;

				long long	c = g.front();
				g.pop_front();
				p += c;
				g.push_back(c);
			}

			Fj(sz(g)) {
				gprintf(1,"%lld ",g[j]);
			}
			gprintf(1,"\n");

			e += p;
		}

		printf("Case #%d: %lld\n",cs,e);
	}
	return 0;
}
