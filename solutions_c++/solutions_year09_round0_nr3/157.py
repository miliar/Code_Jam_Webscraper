#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_n=(b);i<=_n;i++)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n;i--)
#define REP(i,n) FOR(i,0,n-1)
typedef long long int64;
#define two(X) (1<<(X))
#define two64(X) (((int64)1)<<(X))
#define contain(S,x) (((S)&two(x))>0)
#define MOD 10000

char wel[] = "welcome to code jam";

char str[505];
int f[505][25];

int solve( int n, int m ) {
	int &ret = f[n][m];
	if ( ret!=-1 ) return ret;
	ret = 0;

	if ( m==0 ) return 1;
	if ( n==0 ) return 0;
	if ( str[n-1] == wel[m-1] ) 
		ret = (ret%MOD+solve( n-1, m-1 )%MOD)%MOD;
	ret = (ret%MOD+solve( n-1, m )%MOD)%MOD;
	return ret%MOD;
}

int main() {
	int ntc;
	scanf( "%d",&ntc );
	getchar();
	REP(tc,ntc) {
		gets(str);
		memset( f,-1,sizeof(f) );
		printf( "Case #%d: %04d\n", tc+1, solve(strlen(str),strlen(wel)) );
	}
	return 0;
}
