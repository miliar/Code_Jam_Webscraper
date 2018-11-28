#include <string>
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
#define CT(mask,k) ( ((mask) >> (k)) & 1 )


template<class T> inline int BC(T x) {
	int ret = 0;
	for( ; x ; x &= x-1) ++ret;
	return ret;
}
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

int N, M;
const int MAX = 11;
int mem[MAX][1<<MAX];
int banned[MAX][MAX];
int go(int n, int mask)
{
 	if(n < 0) return 0;
	int &ret = mem[n][mask];
	if(ret != -1) return ret;
	ret = 0;
	REP(mask2, 1<<M) {
		
		REP(i,M) if(CT(mask2, i) && banned[n][i]) goto hell;

		FOR(i,1, M-1) if( CT(mask2,i-1) && CT(mask2, i)) goto hell;
		REP(i, M) if( CT(mask2, i)) {
			if(i && CT(mask,i-1)) goto hell;
			if(i<M-1 && CT(mask,i+1)) goto hell;
		}
			
		ret = max(ret, go(n-1, mask2) + BC(mask2));	
		hell:
		continue;
	}

	return ret;
}
void solve(void)
{
	scanf("%d %d\n", &N, &M);
	RESET(banned, 0);
	char buff[2000];
	REP(i,N){
		gets(buff);
		REP(j,M) if(buff[j] == 'x') banned[i][j] = 1;
	}
	RESET(mem,-1);
	printf("%d\n", go(N-1, 0));
}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
