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
#define PB push_back

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define VAR(a,b) __typeof (b) a=b
#define FORE(i,a)  for(VAR(i,(a).begin()); i!=(a).end(); ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))


typedef long long LL;
typedef vector<int> VI;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

#define LLINF 1000000000000000LL

const int MAX = 1<<13;
LL mem[MAX][13];
int can_miss[MAX];
int val[MAX];

LL go(int v, int missed)
{
	
	LL &ret = mem[v][missed];
	if(ret != -1) return ret;
	
	if(val[v] == -1) { // lisc
		if(can_miss[v] >= missed) ret = 0LL;
		else  ret = LLINF;

		//printf("lisc, v: %d  can_miss = %d  missed = %d ret = %lld\n", v, can_miss[v], missed, ret); 
		return ret;
	}

	LL v1 = go(v*2, missed+1) + go(v*2+1, missed+1);
	LL v2 = go(v*2, missed) + go(v*2 + 1, missed) + val[v];
	//assert(v2 < LLINF);
	if(v1 >= LLINF) {
		ret = v2;
		return ret;
	}
	ret = min(v1, v2);
	//printf("v = %d missed = %d ret = %lld v1: %lld v2: %lld val[v] = %d can_miss[v] = %d\n", v, missed, ret,v1, v2, val[v], can_miss[v]);
	return ret;
}
VI poz[13];
int N;
void solve()
{
	int P;
	scanf("%d", &P);
	N = 1<<P;
   	 REP(i, N) scanf("%d", &can_miss[N+i]);
	RESET(val, -1);
	RESET(mem,-1);


	int ile = N/2;
	REP(i, P) {
		poz[i].clear();
		int a;
		REP(j, ile) { scanf("%d", &a); poz[i].PB(a); }
		ile /= 2;
	}
	assert(ile == 0);
	
	int cnt = 1;
	FORD(i, P-1, 0) {
		FORE(j, poz[i]) val[cnt++] = *j;
	}
	
	printf("%lld\n", go(1,0));
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
