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

bool check_last_n(int N, int K) {
	while(N--) {
		if(!(K & 1)) return false;
		K >>= 1;
	}

	return true;
}
int main()
{
	int	T,cs;
	int	N,K;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d",&N,&K);

		printf("Case #%d: %s\n",cs,check_last_n(N,K) ? "ON" : "OFF");
	}
	return 0;
}
