#include<cstdio>
#include<cstring>
#define MAX_N 100
using namespace std;
char schedule[ MAX_N ][ MAX_N ];
int wins[ MAX_N ], games[ MAX_N ];
double WP[ MAX_N ], OWP[ MAX_N ], OOWP[ MAX_N ];
int main(){
	int T, _case = 0;
	scanf( "%d", &T );
	while( _case < T ){
		int n;
		scanf( "%d", &n );
		for( int i = 0; i < n; i ++ ){
			scanf( "%s", schedule[ i ] );
		}
		for( int i = 0; i < n; i ++ ){
			int won_sum = 0.0, game_sum = 0.0;
			for( int j = 0; j < n; j ++ ){
				if( schedule[ i ][ j ] != '.' ){
					game_sum += 1;
					if( schedule[ i ][ j ] == '1' ){
						won_sum += 1;
					}
				}
			}
			WP[ i ] = (double)won_sum / (double)game_sum;
			wins[ i ] = won_sum;
			games[ i ] = game_sum;
		}

		for( int i = 0; i < n; i ++ ){
			double cal_sum = 0.0, game_sum = 0.0;
			for( int j = 0; j < n; j ++ ){
				if( schedule[ i ][ j ] != '.' ){
					game_sum += 1.0;
					if( schedule[ i ][ j ] == '1' ){
						cal_sum += (double)( wins[ j ] ) / (double)( games[ j ]-1);
					}else{
						cal_sum += (double)( wins[ j ]-1 ) / (double)( games[ j ]-1 );
					}
				}
			}
			OWP[ i ] = cal_sum / game_sum;
		}

		for( int i = 0; i < n; i ++ ){
			double cal_sum = 0.0, game_sum = 0.0;
			for( int j = 0; j < n; j ++ ){
				if( schedule[ i ][ j ] != '.' ){
					game_sum += 1.0;
					cal_sum += OWP[ j ];
				}
			}
			OOWP[ i ] = cal_sum / game_sum;
		}
		printf( "Case #%d:\n", ++ _case );
		for( int i = 0; i < n; i ++ ){
			printf( "%.12lf\n", 0.25 *  WP[ i ] + 0.50 * OWP[ i ] + 0.25 * OOWP[ i ] );
		}
	}
	return 0;
}
