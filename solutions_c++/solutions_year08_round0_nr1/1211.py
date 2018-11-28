#include <cstdio>

#include <map>
#include <string>

using namespace std;

int n, m;
int A[1005];
map<string, int> lab;

int dp[1005][105];

inline void better( int &a, int b )
{ if( a < 0 || a > b ) a = b; }

int main( void )
{
	freopen( "pA.in", "r", stdin );
	freopen( "pA.out", "w", stdout );

	int nround; scanf( "%d", &nround );

	char S[105];

	for( int round = 0; round < nround; ) {
		lab.clear();

		scanf( "%d", &n );
		gets( S );
		for( int i = 0; i < n; ++i ) {
			gets( S );
			lab[S] = i;
		}

		scanf( "%d", &m );
		gets( S );
		for( int i = 0; i < m; ++i ) {
			gets( S );
			A[i] = lab[S];
		}

		memset( dp, -1, sizeof dp );

		for( int i = 0; i < n; ++i )
			if( *A != i ) dp[0][i] = 0;

		for( int i = 1; i < m; ++i )
			for( int j = 0; j < n; ++j ) {
				if( dp[i - 1][j] < 0 ) continue;

				for( int k = 0; k < n; ++k )
					if( k != A[i] ) better( dp[i][k], dp[i - 1][j] + (j != k) );
			}

		int best = -1;

		for( int i = 0; i < n; ++i )
			if( dp[m - 1][i] >= 0 ) better( best, dp[m - 1][i] );

		printf( "Case #%d: %d\n", ++round, best );
	}

	return 0;
}
