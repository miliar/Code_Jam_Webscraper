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

bool win(int a,int b) {
	if(b > a) return win(b,a);

	if(b <= 0) return true;
	else if(a / b == 1) return !win(b,a % b);
	else return true;
}

int main()
{
	int	A1,A2,B1,B2;
	int	T,cs;
	int	i,j;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d %d %d",&A1,&A2,&B1,&B2);

		int	w = 0;

		rab(i,A1,A2) rab(j,B1,B2) if(win(i,j))w++;

		printf("Case #%d: %d\n",cs,w);
	}
	return 0;
}
