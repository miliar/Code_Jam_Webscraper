#include <iostream>

using namespace std;

const int N = 102;
const int M = 256;
const int INF = M * N;

int dp[N][M];

int v[N];

int D, I, S, n;

int main(){

	int Tc;
	
	freopen( "B-small-attempt0.in", "r", stdin );
	freopen( "b.small.out.txt", "w", stdout );

	scanf( "%d", &Tc );

	for( int tc = 1; tc <= Tc; tc++ ){

		scanf( "%d%d%d%d", &D, &I, &S, &n );

		for( int i = 1; i <= n; i++ ){
			scanf( "%d", v + i );
		}

		for( int i = 0; i <= n; i++ ){
			for( int j = 0; j < M; j++ ){
				dp[i][j] = INF;
			}
		}

		for( int j = 0; j < M; j++ ){
			dp[0][j] = 0;
		}
		
		for( int i = 1; i <= n; i++ ){

			for( int j = 0; j < M; j++ ){
				if( dp[i - 1][j] + D < dp[i][j] ){
					dp[i][j] = dp[i - 1][j] + D;
				}
			}

			for( int j = 0; j < M; j++ ){
				int dif = j > v[i] ? j - v[i] : v[i] - j;
				for( int k = 0; k < M; k++ ){
					int dic = j > k ? j - k : k - j;
					if( dic <= S ){
//						cout<<j<<" "<<dif<<endl;

						if( dp[i - 1][k] + dif < dp[i][j] ){
							dp[i][j] = dp[i - 1][k] + dif;
						}
					}
				}
			}

			for( int j = 0; j < M; j++ ){
				for( int k = 1; k <= S; k++ ){
					if( dp[i][j] + I < dp[i][j + k] ){
						dp[i][j + k] = dp[i][j] + I;
					}
				}
			}

			for( int j = M - 1; j >= 0; j-- ){
				for( int k = 1; k <= S; k++ ){
					if( j - k >= 0 ){
						if( dp[i][j] + I < dp[i][j - k] ){
							dp[i][j - k] = dp[i][j] + I;
						}
					}
				}
			}
/*
			for( int j = 0; j < 52; j++ ){
				cout<<dp[i][j]<<" ";
			}
			cout<<endl;
*/
		}
		
		int min = INF;

		for( int j = 0; j < M; j++ ){
			if( dp[n][j] < min ){
				min = dp[n][j];
			}
		}

		printf( "Case #%d: %d\n", tc, min );
	}

	return 0;
}






