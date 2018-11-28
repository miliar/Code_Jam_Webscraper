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

bitset <100000>	comp;
vector <int>	primes;
int	S[20];
int	K;

int main()
{
	int	i,j,min_prime,A,B;
	int	k;
	int	D,ulimit;
	int	T,cs;

	for(i = 2; i <= 10000; i++) {
		if(comp[i]) continue;

		for(j = i * i; j <= 10000; j += i)
			comp[j] = true;
	}

	for(i = 2; i <= 10000; i++) if(comp[i] == false) primes.push_back(i);

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d",&D,&K);
		 ulimit = 1;

		 Fi(D) ulimit *= 10;

		min_prime = 0;
		Fi(K) {
			scanf("%d",&S[i]);
			min_prime = max(S[i] + 1,min_prime);
		}

		int	next = -1;

		if(K > 1) {
			Fi(sz(primes)) {
				if(primes[i] < min_prime) continue;
				if(primes[i] > ulimit) break;

				for(A = 0; A < primes[i]; A++) {
					B = (S[1] - A * S[0]) % primes[i];
					B = (B + primes[i]) % primes[i];

					//printf("P = %d, A = %d B = %d\n",primes[i],A,B);

					for(k = 0; k < K - 1; k++) {
						int	s1;

						s1 = (A * S[k] + B) % primes[i];
						//printf("s1 = %d, or = %d\n",s1,S[k+1]);
						if(s1 != S[k+1]) break;
					}

					if(k >= K - 1) {
						//printf("k = %d\n",k);
						int	w = (A * S[K - 1] + B) % primes[i];

						if(next == -1)
							next = w;
						else if(next != w) {
							next = -1;
							goto print_here;
						}
					}
					//printf("next = %d\n",next);
				}
			}
		}

print_here:
		printf("Case #%d: ",cs);

		if(next == -1)
			printf("I don't know.\n");
		else
			printf("%d\n",next);
	}
	return 0;
}
