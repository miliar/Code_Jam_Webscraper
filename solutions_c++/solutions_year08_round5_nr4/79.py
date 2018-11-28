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

const int MAX = 110, MOD = 10007;
int pole[MAX][MAX];
LL mem[MAX][MAX];
int N, M;

int dx[] = { 1, 2, 1, 2 }, dy[] = { 2, 1, 2, 1 };
LL go(int x, int y)
{
	if(pole[x][y]) return 0;
	if(x == N-1 && y == M-1) return 1LL;
	
	LL &ret = mem[x][y];
	if(ret != -1) return ret;
	ret = 0;
	
	REP(k, 2) {
		int nx = x + dx[k], ny = y + dy[k];
		if(nx >= N || ny >= M) continue;
		if(pole[nx][ny]) continue;
		ret += go(nx,ny);
		ret %= MOD;
	}
	return ret;

}
void solve(void)
{
	int H, W, R;

	scanf("%d %d %d", &H, &W, &R);
	N = H; M = W; 
	RESET(pole, 0);
	REP(i, R) {
		int a, b;
		scanf("%d %d", &a, &b);
		pole[a-1][b-1] = 1;
	}
	RESET(mem,-1);
	printf("%lld\n", go(0,0));
}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d: ",C++); solve(); }
	return (0);
}
