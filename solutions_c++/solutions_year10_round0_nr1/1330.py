

#include <cstdio>


int main(){

	//printf( "1<<30 = %d\n" , 1 << 30 ); return 0;
		
	int T , N , K;
	
	scanf( "%d" , &T );
	
	for ( int tc = 1 ; tc <= T ; tc++ ){
	
		scanf( "%d %d" , &N , &K );
		
		int pow2 = 1 << N;
		
		printf( "Case #%d: " , tc );
		
		if ( K % pow2 == pow2 - 1 ) printf( "ON\n" );
					else printf( "OFF\n" );	
	
	}


	return 0;
}
