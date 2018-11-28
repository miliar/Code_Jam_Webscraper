
#include <cstdio>

const int
	MAXN = 55,
	mov[][2] = {{1,0},{0,1},{1,-1},{1,1}};

int T, tc , N , K;
char map[MAXN][MAXN] , rot[MAXN][MAXN];

int main(){

	scanf( "%d" , &T );

	for ( tc = 1 ; tc <= T ; tc++ ){
	
		scanf( "%d %d" , &N , &K );	
	
		for ( int i = 0 ; i < N ; i++ )
			scanf( "%s" , &map[i] );
			
		// rotate
		
		for ( int i = 0 ; i < N ; i++ )
			for ( int j = 0 ; j < N ; j++ ) 
				rot[i][j] = map[N-j-1][i];
			
		// debug
		/*
		printf( "DEBUG\n" );
			
		for ( int i = 0 ; i < N ; i++ )
			printf( "%s\n" , map[i] );
			
		printf( "\n" );
		*/		
			
		// gravity
		
		for ( int j = 0 ; j < N ; j++ )
			for ( int i = N-1 ; i >= 0 ; i-- )
				if ( rot[i][j] != '.' ){
				
					// falls
					
					char tmp = rot[i][j];
					rot[i][j] = '.';
					
					int k = i;
					while ( k < N-1 && rot[k+1][j] == '.' ) k++;
					
					rot[k][j] = tmp;	
					
				}

		//for ( int i = 0 ; i < N ; i++ )
		//	printf( "%s\n" , rot[i] );

				
		// K in a row
		
		bool winR = false, winB = false;
		
		for ( int i = 0 ; i < N ; i++ )
			for ( int j = 0 ; j < N ; j++ ) if ( rot[i][j] != '.' )
				for ( int k = 0 ; k < 4 ; k++ ){
				
					int nr = i;
					int nc = j;
					int cant = 0;
					
					while ( nr >= 0 && nr < N && nc >= 0 && nc < N && rot[nr][nc] == rot[i][j] ){
						cant++;
						nr += mov[k][0];
						nc += mov[k][1];
					}	
					
					if ( cant >= K ){
						if ( rot[i][j] == 'B' ) winB = true;
						else winR = true;
						break;
					}
					
				}
		
		// sol
		
		printf( "Case #%d: " , tc );
		
		if ( winB && winR ) printf( "Both\n" );
		else if ( winB ) printf( "Blue\n" );
		else if ( winR ) printf( "Red\n" );
		else printf( "Neither\n" );
 		
	}

	return 0;
}
