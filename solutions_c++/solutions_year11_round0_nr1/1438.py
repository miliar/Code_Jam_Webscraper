#include <cstdio>
#include <algorithm>
using namespace std;


int robo[ 200 ];
int butao[ 200 ];

int main(){
	int casos, n;
	int acco, accb, temp;
	char r[ 10 ];
	
	scanf( "%d", &casos );
	
	for( int c = 1; c <= casos; ++c ){
		printf( "Case #%d: ", c );
		
		scanf( "%d", &n );
		for( int i = 0; i < n; ++i ){
			scanf( "%s %d", r, &temp );
			if( r[ 0 ] == 'B' )
				robo[ i ] = 'B';
			else
				robo[ i ] = 'O';
			butao[ i ] = temp;
		}
		
		int tempo = 0;
		int ato = 1, atb = 1;
		acco = accb = 0;
//		O 5 O 8 B 100
//		5
//		4
		
		for( int i = 0; i < n; ++i ){
			if( robo[ i ] == 'B' ){
				int dist = abs( butao[ i ] - atb );
				atb = butao[ i ];

				if( dist > acco ){
					tempo += dist - acco + 1;
					
					if( i && robo[ i - 1 ] == 'B' )
						accb += dist - acco + 1;
					else
						accb = dist - acco + 1;
					acco = 0;  
				}else{
					acco = 0;
					if( i && robo[ i - 1 ] == 'B' )
						++accb;
					else
						accb = 1;
					++tempo;
				}
			}else{
				int dist = abs( butao[ i ] - ato );
				ato = butao[ i ];
				if( dist > accb ){
					tempo += dist - accb + 1;
					
					if( i && robo[ i - 1 ] == 'O' )
						acco += dist - accb + 1;
					else
						acco = dist - accb + 1;
					accb = 0;
				}else{
					if( i && robo[ i - 1 ] == 'O' )
						++acco;
					else
						acco = 1;
					accb = 0;
					++tempo;
				}
			}
		}
		
		printf( "%d\n", tempo );
	}
}




