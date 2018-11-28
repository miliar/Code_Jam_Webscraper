#include "stdio.h"

int main()
{
FILE *in_ptr, *out_ptr;
int i;

in_ptr = fopen( "A-large.in", "r+" );
out_ptr = fopen( "A-small.out", "w+" );

int T, N, K;

fscanf( in_ptr, "%d", &T );

for( i=1; i<=T; i++ )
 {
	fscanf( in_ptr, "%d", &N );
	fscanf( in_ptr, "%d", &K );

	if( (K & (1<<N)-1) == (1<<N)-1 )
		fprintf( out_ptr, "Case #%d: ON\n", i );
	else
		fprintf( out_ptr, "Case #%d: OFF\n", i );

 }

fclose( in_ptr );
fclose( out_ptr );
}
