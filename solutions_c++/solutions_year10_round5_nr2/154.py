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

#define	INF		(1LL<<62)

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

struct State {
	long long	min_board[101];
};

int	B[100];
int	N;

bool	available[101];

State get(long long L) {
	State	r;
	int	i,j,k;

	if(L == 0) {

		for(i = 0; i < 100; i++) r.min_board[i] = INF;
		r.min_board[0] = 0;
		return r;
	} else if(L == 1) {
		for(i = 0; i < 100; i++) r.min_board[i] = INF;
		r.min_board[1] = 0;

		for(i = 0; i < N; i++) {
			if(B[i] == 1)
				r.min_board[0] = 1;
		}

		return r;
	}

	State	p1,p2;
	long long	u,v,w;

	if(L % 2 == 0) {
		u = v = L / 2;
	} else {
		u = L - 1;
		v = 1;
	}

	p1 = get(u);
	if(u != v) p2 = get(v);
	else p2 = p1;

	for(i = 0; i < 100; i++) r.min_board[i] = INF;
	if(L < 100) r.min_board[L] = 0;

	for(i = 0; i < min(100LL,u+1); i++) for(j = 0; j < min(100LL,v+1); j++) {
		if(p1.min_board[i] >= INF) continue;
		if(p2.min_board[j] >= INF) continue;

		if(i + j < 100) r.min_board[i + j] = min(r.min_board[i + j],p1.min_board[i] + p2.min_board[j]);

		Fk(N) {
			w =  i + j - B[k];
			if(w < 0 || w >= 100) continue;

			r.min_board[w] = min(r.min_board[w],p1.min_board[i] + p2.min_board[j] + 1);
		}
	}

/*	printf("%lld - ",L);
	for(i = 0; i <= 5; i++) printf(" %lld",r.min_board[0]);
	printf("\n");*/

	return r;
}
int main()
{
	int	T,cs;
	long long	L;
	int	i;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%lld %d",&L,&N);

		Fi(N) scanf("%d",&B[i]);

		State	s = get(L);

		printf("Case #%d:",cs);

		if(s.min_board[0] >= INF)
			printf(" IMPOSSIBLE\n");
		else
			printf(" %lld\n",s.min_board[0]);
	}
	return 0;
}
