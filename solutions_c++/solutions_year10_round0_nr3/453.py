#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <string>
#include <sstream>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<string> VS;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
#define ALL(A) (A).begin(),(A).end()
#define SIZE(A) (int)(A).size()
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define MMAX(X,Y) ((X) = max((X),(typeof(X))(Y)))
#define MMIN(X,Y) ((X) = min((X),(typeof(X))(Y)))
#define BITCNT(X) (__builtin_popcount(X))
#define BIT(X,Y) ((X)&(1<<(Y)))
#define FBIT(X) (__builtin_ctz(X))
#define LBIT(X) (31 - __builtin_clz(X))

int g[1009];
LL dp[1009];
LL dp_sum[1009];
LL total_sum;

int rounds, cap, n;

pair<int,LL> find_next(int start) {
	LL cur_cap = cap;
	FOR(i,0,n-1) {
		if( cur_cap >= g[start] ) cur_cap -= LL(g[start]);
		else break;	
		start = (start + 1) % n;		
	}
	return MP(start,cap-cur_cap);
}

void solve(int test_num) {
	scanf("%d %d %d",&rounds,&cap,&n);
	REP(i,n) 
		scanf("%d",&g[i]);
	REP(i,n) {
		dp[i] = -1;
		dp_sum[i] = 0;
	}
	dp[0] = 0;
	int i = 0, round = 1;
	LL res = 0;
	while( round <= rounds ) {
		pair<int,LL> p = find_next(i);
		i = p.first;
		res += p.second;
		if( dp[i] != -1 ) {
			int r = round - dp[i];
			int wr = (rounds - round) / r;
			round += wr * r;
			res += LL(wr) * (res - dp_sum[i]);
		}
		dp[i] = round;
		dp_sum[i] = res;
		++round;
	}
	printf("Case #%d: %lld\n",test_num,res);
}

int main() {
	int tests;
	scanf("%d",&tests);
	FOR(test,1,tests)
		solve(test);
	return 0;
}
























