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

int	freq[2500000];
bool	flag[2500000];

int main()
{
	int	T,cs;
	int	P,V;
	int	C;

	scanf("%d",&T);

	rab(cs,1,T) {
		memset(freq,0,sizeof(freq));
		memset(flag,0,sizeof(flag));

		scanf("%d",&C);
		queue <int>	Q;

		while(C--) {
			scanf("%d %d",&P,&V);

			P += 1200000;

			freq[P] += V;

			if(freq[P] >= 2 && flag[P] == false) {
				flag[P] = true;
				Q.push(P);
			}
		}
		
		int	f = 0;

		while(!Q.empty()) {
			int	u = Q.front();
			Q.pop();
			int	w = freq[u] / 2;
			f += w;
			flag[u] = false;

			//gprintf(1,"in position: %d - %d hot -  %d moves\n",u,freq[u],w);

			freq[u-1] += w;
			if(!flag[u-1] && freq[u-1] > 1) {
				flag[u-1] = true;
				Q.push(u-1);
			}
			freq[u+1] += w;
			if(!flag[u+1] && freq[u+1] > 1) {
				flag[u+1] = true;
				Q.push(u+1);
			}
			freq[u] = freq[u] % 2;
		}

		printf("Case #%d: %d\n",cs,f);
	}
	return 0;
}
