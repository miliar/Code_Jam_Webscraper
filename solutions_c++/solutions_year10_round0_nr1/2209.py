#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, const char * argv[]) {
	FILE *file, *out_file;
	
//	file = fopen( "../../../test.txt", "r" );
	file = fopen( "../../../A-large.in", "r" );
	
	out_file = fopen( "../../../out.txt", "w" );
	
	if( !file ) return -1;
	
	char buf[200];
	
	fgets( buf, 200, file );
	
	unsigned num = atoi( buf );
	printf("num %u\n", num );

	
	
	unsigned i;
	for( i=0; i<num; i++ ) {
		fgets( buf, 200, file );
		unsigned n,k;
		
		sscanf( buf, "%u %u", &n, &k );

		fprintf( out_file, "Case #%u: ", i+1 );
		
		unsigned t = ( 1 << n ) - 1;

		printf("%u, %u  t=%u  ", n, k, t);

		
		if( (k & t) == t ) {
			fprintf( out_file, "ON\n");
			printf("On\n");
		}else{
			fprintf( out_file, "OFF\n");
			printf("Off\n");
		}
	}
	
	return 0;
	
}
