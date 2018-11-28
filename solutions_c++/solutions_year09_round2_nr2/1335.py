#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef long long LL;

LL toint(vector <int> &v) {
	LL ret = 0;
	REP(i,v.size()) ret = ret * 10 + v[i];
	return ret;
}

int main()
{
	int T;
	scanf( "%d", &T );

	FOR(tcase,1,T) {
		LL n, m;
		scanf( "%I64d", &n ); m = n;

		vector <int> v;
		while ( n != 0 ) {
			v.push_back(n%10);
			n /= 10;
		}
		
		printf( "Case #%d: ", tcase );

		reverse(v.begin(),v.end());
		
		next_permutation(v.begin(),v.end());
		if ( m >= toint(v) ) {
			sort(v.begin(),v.end());
			int k = 0, tk = 10;
			REP(i,v.size()) if ( v[i] != 0 && v[i] < tk ) k = i, tk = v[i];
			
			printf( "%d", v[k] ); putchar( '0' );
			REP(i,v.size()) if ( i != k )  printf( "%d", v[i] );
			puts("");
		}
		else {
			REP(i,v.size()) printf( "%d", v[i] ); puts("");
		}

	}

	return 0;
}
