#include <stdio.h>
#include <stdlib.h>

// T : ( 1, 100 )
// N : ( 1, 10 ) / ( 1, 1000 )

int process( int *input, int N, int sum, int xorA, int xorB, int nA, int nB );

void main(){

	// file open
	FILE *fp = fopen( "input.txt", "r" );
	FILE *fp2 = fopen( "output.txt", "w" );

	int T;
	int N;
	int input[ 1000 ];

	fscanf( fp, "%d", &T );

	int i, j;

	for ( i = 0; i < T; i++ ) {

		fscanf( fp, "%d", &N );

		for ( j = 0; j < N; j++ ) 
			fscanf( fp, "%d ", &input[ j ] );

		int ret = process( input, N, 0, 0, 0, 0, 0 );

		if( ret > 0 ) fprintf( fp2, "Case #%d: %d\n", i+1, ret );
		else		  fprintf( fp2, "Case #%d: NO\n", i+1 );
	}
}


int process( int *input, int N, int sum, int xorA, int xorB, int nA, int nB ){

	if( N > 0 ) {

		int last = input[ N -1 ];

		int a = process( input, N -1, sum + last, xorA ^ last, xorB, nA + 1, nB );

		int b = process( input, N -1, sum, xorA, xorB ^ last, nA, nB + 1 );

		if( a >= b ) return a;
		else		 return b;
	}
	else{

		if( xorA == xorB &&
			nA > 0 &&
			nB > 0 ){
			return sum;
		}
		else{
			return 0;
		}
	}
}