#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)

int flag[2000005];

int f(int n) { return n >= 10 ? 10 * f(n/10) : 1; }
int g(int n) { return n >= 10 ? 1  + g(n/10) : 1; }

int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		int a, b;
		scanf( "%d %d", &a, &b );
		memset(flag,0,sizeof(flag));
		int ans = 0;
		FOR(n,a,b) {
			int p = f(n);
			int m = n;
			REP(_,g(n)) {
				m = m / 10 + m % 10 * p;
				if ( m % p != 0 && m <= b && n < m && flag[m] != n ) ans++, flag[m] = n;
			}
		}
		fprintf( stderr, "Case #%d: %d\n", tcase, ans );
		printf( "Case #%d: %d\n", tcase, ans );
	}
	return 0;
}
