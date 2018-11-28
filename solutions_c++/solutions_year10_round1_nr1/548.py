#include <iostream>

using namespace std;

const int N = 52;

char s[N][N], ch[N][N];

int move[8][2] = { { -1, -1 }, { -1, 0 }, { -1, 1 }, { 0, -1 }, { 0, 1 }, { 1, -1 }, { 1, 0 }, { 1, 1 } };

int main(){


	int Tc, tc;
	
	freopen( "A-large.in", "r", stdin );
	freopen( "a.large.out.txt", "w", stdout );

	scanf( "%d", &Tc );
	
	int n, K;

	for( tc = 1; tc <= Tc; tc++ ){

		scanf( "%d%d", &n, &K );

		for( int i = 0; i < n; i++ ){
			scanf( "%s", s[i] );
		}

		for( int i = 0; i < n; i++ ){
			for( int j = 0; j < n; j++ ){
				ch[i][j] = s[n - j - 1][i];
			}
		}
		
		for( int j = 0; j < n; j++ ){
			int cnt = n - 1;
			for( int i = n - 1; i >= 0; i-- ){
				if( ch[i][j] != '.' ){
					char tmp = ch[i][j];
					ch[i][j] = '.';
					ch[cnt--][j] = tmp;
				}
			}
		}
/*			
		for( int i = 0; i < n; i++ ){
			cout<<ch[i]<<endl;
		}
*/
		bool flagr = false, flagb = false;

		for( int i = 0; i < n; i++ ){
			for( int j = 0; j < n; j++ ){
				if( ch[i][j] != '.' ){
					for( int k = 0; k < 8; k++ ){
						int cnt = 0;
						for( int p = 1; ; p++ ){
							int x = i + p * move[k][0];
							int y = j + p * move[k][1];
							if( x >= 0 && y >= 0 && x < n && y < n && ch[x][y] == ch[i][j] ){
								cnt++;
							}
							else{
								break;
							}
						}

						if( cnt >= K - 1 ){
							if( ch[i][j] == 'R' ){
								flagr = true;
							}
							else{
								flagb = true;
							}
//							cout<<i<<" "<<j<<" "<<k<<endl;
						}
					}
				}
			}
		}
		
		printf( "Case #%d: ", tc );
		
		if( flagr == true && flagb == true ){
			printf( "Both\n" );
		}
		else if( flagr == true ){
			printf( "Red\n" );
		}
		else if( flagb == true ){
			printf( "Blue\n" );
		}
		else{
			printf( "Neither\n" );
		}
	}

	return 0;
}








