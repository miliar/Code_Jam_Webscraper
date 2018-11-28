#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)

const int max_n = 20000;
const int inf   = 2000000;

int m, v;
int g[max_n], c[max_n];
int memo[max_n][2];

int parent(int x) { return x >> 1; }
int left(int x) { return x << 1; }
int right(int x) { return left(x) + 1; }
bool leaf(int x) { return x * 2 > m; }

int f(int x, int t) {
	if ( memo[x][t] != -1 ) return memo[x][t];
	int &ret = memo[x][t] = inf;
	if ( leaf(x) ) ret = g[x] == t ? 0 : inf;
	else {
		if ( c[x] == 1 || g[x] ==  t ) ret = min(ret, (g[x] !=  t) + f(left(x), t) + f(right(x), t));
		if ( c[x] == 1 || g[x] == !t ) ret = min(ret, (g[x] != !t) + f(left(x), t) + f(right(x),!t));
		if ( c[x] == 1 || g[x] == !t ) ret = min(ret, (g[x] != !t) + f(left(x),!t) + f(right(x), t));
		if ( c[x] == 1 || g[x] == !t ) ret = min(ret, (g[x] != !t) + f(left(x), t) + f(right(x), t));
	}
	return ret;
}

int main()
{
	int ncase;
	scanf( "%d", &ncase );

	FOR(tcase,1,ncase) {
		scanf( "%d %d", &m, &v );
		FOR(i,1,(m-1)/2) scanf( "%d %d", &g[i], &c[i] );
		FOR(i,(m+1)/2,m) scanf( "%d", &g[i] );
		

		memset(memo,-1,sizeof(memo));
		int ans = f(1,v);
		printf( "Case #%d: ", tcase );
		if ( ans == inf ) puts( "IMPOSSIBLE" );
		else printf( "%d\n", ans );
	}
	
	return 0;
}
