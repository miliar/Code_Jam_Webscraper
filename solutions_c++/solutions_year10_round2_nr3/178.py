#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <list>
#include <stack>
#include <set>
#include <map>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof( V.begin() ) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

const int modulo = 100003LL;
const int MAXN = 505;
LL T[MAXN][MAXN]; // koles, dlugosc

LL DP[MAXN][MAXN];

LL newton(int n, int k) {
	if(n == k) return 1;
	if(n < k) return 0;
	if(k == 0) return 1;
	if(DP[n][k] != -1) return DP[n][k];
	DP[n][k] = newton(n-1,k-1) + newton(n-1,k);
	DP[n][k] %= modulo;
	return DP[n][k];
}

void testcase(int v) {
	printf("Case #%d: ", v);
	int n;
	scanf("%d", &n);
	FOR(i,0,n) FOR(j,0,n) T[i][j] = 0;
	T[1][0] = 1;
	FOR(i,2,n) FOR(j,1,i-1) { // do i-tego kolesia skladajace sie z j bitow
		if(j == 1) T[i][1] = 1;
		else if(j == i-1) T[i][i-1] = 1;
		else FOR(k,1,j-1) T[i][j] = (T[i][j] + (T[j][k] * newton(i-j-1, j-k-1)))%modulo;
	}
	LL res = 0;
	FOR(i,1,n-1) res = (res + T[n][i])%modulo;
	FOR(i,1,n) FOR(j,1,i) printf("T[%d][%d]: %lld\n", i, j, T[i][j]);
	printf("%lld\n", res);
}

int main() {
	int t;
	REP(i,MAXN) REP(j,MAXN) DP[i][j] = -1;
	scanf("%d", &t);
	REP(i,t) testcase(i+1);
	return 0;
}

