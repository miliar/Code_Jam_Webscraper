#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)

int main()
{
	int ncase, n, k;
	scanf( "%d", &ncase );
	FOR(tcase,1,ncase) {
		scanf( "%d %d", &n, &k );
		printf( "Case #%d: %s\n", tcase, __builtin_popcount(k&((1<<n)-1)) == n ? "ON" : "OFF" );
	}
	return 0;
}
