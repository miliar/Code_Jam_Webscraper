#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)


int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		int n, lo = 1000000000, sum = 0, x, bit = 0;
		scanf( "%d", &n );
		REP(_,n) {
			scanf( "%d", &x );
			bit ^= x;
			lo = min(lo,x);
			sum += x;
		}
		if ( bit == 0 ) printf( "Case #%d: %d\n", tcase, sum - lo );
		else printf( "Case #%d: NO\n", tcase );
	}
	return 0;
}
