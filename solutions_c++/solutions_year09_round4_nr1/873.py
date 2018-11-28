#include <iostream>

using namespace std;

int t, T;
char str[ 100 ];
__int64 dp[ 100 ];
__int64 F[ 42 ];
int n;
int hash[ 100 ];


int main() {

	freopen ( "A-large.in", "r", stdin );
	freopen ( "A-large.out", "w", stdout );
	int i, j; 
	F[0] = 1;
	for(i = 1; i < 42; i ++ )
		F[i] = F[i-1] * 2;

	scanf("%d", &t);
	T = t;
	while( t-- ) {

		memset( hash, 0, sizeof( hash ));
		scanf("%d", &n);
		for(i = 0; i < n; i++) {
			scanf("%s", str);
			dp[i] = 0;
			for( j = 0; str[j]; j ++ ) {
				dp[i] = (__int64)( dp[i] * 2 + (int)(str[j] - '0') );
			}
		}

		int x = 0;
		int S = 0;

		while( x < n ) {

			for(i = x; i < n; i++) {
				for( j = 0; j < n; j++) {
					if( dp[i] & F[j] )
						break;
				}

				if( n - 1 - j > i ) {
					break;
				}
			}

			if( i == n )
				break;


			int u = -1;
			int Max = -1;

			for(i = x; i < n; i++) {
				for(j = 0; j < n; j++) {
					if( dp[i] & F[j] )
						break;
				}
				if( n - 1 - j <= x ) {
					u = i;
					break;
				}
			}

			__int64 R = dp[u];

			for( i = u; i > x; i-- ) {
				dp[i] = dp[i-1];
				S ++;
			}
			dp[x] = R;

			x ++;
		}
		printf("Case #%d: %d\n", T - t, S );
	} 
	return 0;
}

/*
Case #1: 0
Case #2: 2
Case #3: 4
Case #4: 0
Case #5: 0
Case #6: 0
Case #7: 1
Case #8: 1
Case #9: 0
Case #10: 0
Case #11: 0
Case #12: 0
Case #13: 0
Case #14: 0
*/