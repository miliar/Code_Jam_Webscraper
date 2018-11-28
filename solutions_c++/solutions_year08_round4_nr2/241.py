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
#define RESET(a,c) memset(a,(c),sizeof(a))


typedef long long LL;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/

void solve(void)
{
	int N, M, A;
	scanf("%d %d %d",&N, &M, &A);
	
	int xx[2], yy[2];
	RESET(xx,-1); RESET(yy, -1);
	REP(x0, N+1) REP(y0, M+1) REP(x1, N+1) REP(y1, M+1){
		LL area = (LL)x0 * y1 - (LL)x1 * y0;
		if(area < 0) area = -area;
		if(area == A) { xx[0] = x0; xx[1] = x1; yy[0] = y0; yy[1] = y1; break; }
	}

	if(xx[0] == -1) {printf("IMPOSSIBLE\n"); return ;}
	
	printf("0 0 %d %d %d %d\n", xx[0], yy[0], xx[1], yy[1]);
}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
