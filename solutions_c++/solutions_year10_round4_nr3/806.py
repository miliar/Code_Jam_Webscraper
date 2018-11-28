#include <iostream>

using namespace std;

const int N = 110;

int a[N][N];
int b[N][N];

int main(){

	int Tc;
	
	freopen( "C-small-attempt1.in.txt", "r", stdin );
	freopen( "c-small-out.txt", "w", stdout );

	scanf( "%d", &Tc );

	for( int tc = 1; tc <= Tc; tc++ ){

		int q;

		scanf( "%d", &q );

		for( int i = 0; i < N; i++ ){
			for( int j = 0; j < N; j++ ){
				a[i][j] = 0;
			}
		}

		while( q-- ){

			int x1, x2, y1, y2;

			scanf( "%d%d%d%d", &x1, &y1, &x2, &y2 );

			for( int i = y1; i <= y2; i++ ){
				for( int j = x1; j <= x2; j++ ){
					a[i - 1][j - 1] = 1;
				}
			}
		}

		int ans = 0;

		while( true ){

			int sum = 0;

			for( int i = 0; i < N; i++ ){
				for( int j = 0; j < N; j++ ){
					sum += a[i][j];
				}
			}

			if( sum == 0 ){
				break;
			}

			ans++;

			for( int i = 0; i < N; i++ ){
				for( int j = 0; j < N; j++ ){
					b[i][j] = a[i][j];
				}
			}

			for( int i = 0; i < N; i++ ){
				for( int j = 0; j < N; j++ ){
					if( a[i][j] == 0 ){
						if( i > 0 && j > 0 && b[i - 1][j] == 1 && b[i][j - 1] == 1 ){
							a[i][j] = 1;
						}
						else{
							a[i][j] = 0;
						}
					}
					else{
						if( i > 0 && b[i - 1][j] == 1 || j > 0 && b[i][j - 1] == 1 ){
							a[i][j] = 1;
						}
						else{
							a[i][j] = 0;
						}
					}
				}
			}
		}

		printf( "Case #%d: %d\n", tc, ans );
	}

	return 0;
}
		


