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
#define PB push_back
#define SIZE(x) (int)((x).size())

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define RESET(a,c) memset(a,(c),sizeof(a))
#define SORT(x) sort( (x).begin(), (x).end() ) 


typedef long long LL;
typedef vector<int> VI;
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/


void solve(void)
{
	int N;
	scanf("%d", &N);
	VI plus[2], minus[2];
	int zero[2];
	RESET(zero, 0);

	REP(x, 2) REP(i, N) {
		int a;
		scanf("%d", &a);
		if(a == 0) ++zero[x];
		else if(a < 0) minus[x].PB(-a);
		else plus[x].PB(a);
	}
	
	REP(x,2) {
		SORT(minus[x]); SORT(plus[x]);
	}
	
	LL ret = 0;

	REP(x, 2) 
	while(SIZE(minus[x]) && SIZE(plus[1-x])) {
		ret -= (LL)minus[x].back() * plus[1-x].back();
		minus[x].pop_back();
		plus[1-x].pop_back();
	}
	
	
	REP(x, 2) {
		while(zero[x] && SIZE(plus[1-x])) { --zero[x]; plus[1-x].pop_back(); }
		while(zero[x] && SIZE(minus[1-x])) { --zero[x]; minus[1-x].pop_back(); }
	}
	

//	printf("plus[0] = %d plus[1] = %d\n", SIZE(plus[0]), SIZE(plus[1]));
	REP(i, min(SIZE(plus[0]), SIZE(plus[1])))
		ret += (LL)plus[0][i] * plus[1][SIZE(plus[1])-1-i];
	
//	printf("minus[0] = %d  minus[1] = %d\n", 
	REP(i, min(SIZE(minus[0]), SIZE(minus[1])))
		ret += (LL)minus[0][i] * minus[1][SIZE(minus[1])-1-i];
	
	printf("%lld\n", ret);
}
int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
