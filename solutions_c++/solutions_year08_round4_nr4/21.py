#include <cstdio>
#include <cstring>

int N, K;
char S[50005];

int dp[16][16][1 << 16];

int cntA[16][16];
int cntB[16][16][16];
int cntC[16][16][16][16];

int solve( int l, int r, int state )
{
	int &ref = dp[l][r][state];
	if( ref >= 0 ) return ref;

	int n_slot = K - __builtin_popcount( state );

	if( n_slot == 0 ) {
		ref = cntA[l][r];
	} else if( n_slot == 1 ) {
		int x = 0;
		while( (state>>x) & 1 ) ++x;

		ref = cntB[l][r][x];
	} else {
		ref = 1000000000;

		for( int nl = 0; nl < K; ++nl ) {
			if( (state>>nl) & 1 ) continue;

			for( int nr = 0; nr < K; ++nr ) {
				if( (state>>nr) & 1 ) continue;
				if( nl == nr ) continue;

				int cnt = cntC[l][r][nl][nr] + solve( nl, nr, state | (1<<nl) | (1<<nr) );

				ref <?= cnt;
			}
		}
	}

	return ref;
}

int main( void )
{
	freopen( "Dlarge.in", "r", stdin );
	freopen( "Dlarge.out", "w", stdout );

	int nround; scanf( "%d", &nround );

	for( int round = 0; round < nround; ) {
		scanf( "%d", &K );
		scanf( "%s", &S );
		N = strlen( S );

		int best = 1000000000;

		memset( dp, -1, sizeof dp );
		memset( cntA, 0, sizeof cntA );
		memset( cntB, 0, sizeof cntB );
		memset( cntC, 0, sizeof cntC );

		for( int i = 0; i < K; ++i )
			for( int j = 0; j < K; ++j ) {
				if( i == j ) continue;

				for( int k = 0; k < N / K; ++k )
					if( S[k * K + i] != S[k * K + j] ) ++cntA[i][j];

				for( int k = 0; k < K; ++k ) {
					if( i == k || j == k ) continue;

					for( int l = 0; l < N / K; ++l ) {
						if( S[l * K + i] != S[l * K + k] ) ++cntB[i][j][k];
						if( S[l * K + j] != S[l * K + k] ) ++cntB[i][j][k];
					}

					for( int l = 0; l < K; ++l ) {
						if( i == l || j == l || k == l ) continue;

						for( int m = 0; m < N / K; ++m ) {
							if( S[m * K + i] != S[m * K + k] ) ++cntC[i][j][k][l];
							if( S[m * K + j] != S[m * K + l] ) ++cntC[i][j][k][l];
						}
					}
				}
			}

		for( int i = 0; i < K; ++i )
			for( int j = 0; j < K; ++j )
				if( i != j ) {
					int len = 1 + solve( i, j, (1 << i) | (1 << j) );
					for( int k = 1; k < N / K; ++k )
						if( S[(k - 1) * K + j] != S[k * K + i] ) ++len;

					best <?= len;
				}

		printf( "Case #%d: %d\n", ++round, best );
	}

	return 0;
}
