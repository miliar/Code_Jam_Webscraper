#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

template< class T>
void swap( T &a, T &b ) {
	T t = b;
	b = a;
	a = t;
}

const unsigned k_max_num_t = 1000;

FILE *file, *out_file;

void print_arr( long long *p, int n ) {
	int i;
	for( i=0; i<n; i++ ) {
		printf("%lld ", p[i] );
	}
	printf("\n");
}

long long hcf( long long* p, int n ) {
//	printf("-- hcf ---\n");
	if( n == 0 ) return 1;
	
	int i;
	
	long long hcf = 1;
	long long f;
	for( f=2; f<=p[0]; f++ ) {
		long long r = 0;
		for( i=0; i<n; i++ ) {
			r = p[i] % f;
			if( r ) break;
		}
		if( r ) continue;
		
//		printf("f = %lld hcf =%lld, ", f, hcf );
//		print_arr( p,n );

		hcf *= f;		
		
		for( i=0; i<n; i++ ){
			p[i] /= f;
		}
		
		f = 1;
	}
	
	return hcf;
}

void do_record( int record, long long* t, int n ) {
	int i,j;
	for( i=n; i>0; i-- ) {
		for( j=1; j<i; j++ ) {
			if( t[j-1] > t[j] ) 
				swap( t[j-1], t[j] );
		}
	}

	long long td[ k_max_num_t ];

	int n_td = 0;
	for( i=0; i<n-1; i++ ) {
		long long d = t[i+1] - t[i];
		if( d ) {
			td[ n_td ] = d;
			n_td++;
		}
	}
	
	print_arr( td, n_td );
	
	long long T = hcf( td, n_td );
	
	long long m = 0;
	long long y = 0;
	if( T ) {
		m = t[0] / T;
		if( t[0] % T ) m++;
		y = (T*m) - t[0];
	}
	
	printf("T = %lld  y=%lld \n", T, y );
	
	fprintf( out_file, "Case #%u: %lld\n", record+1, y );
}

int main (int argc, const char * argv[]) {	
	file = fopen( "../../../B-small-attempt3.in", "r" );
	out_file = fopen( "../../../out2.txt", "w" );
		
	char buf[200];
	
	fgets( buf, 200, file );
	
	unsigned num = atoi( buf );
	printf("num %u\n", num );
	
	int n;
	long long t[ k_max_num_t ];
	
	unsigned i;
	for( i=0; i<num; i++ ) {
		fgets( buf, 200, file );
		
		printf("----- %d ------\n", i );
		
		char* p = strchr( buf, ' ' );
		*p = 0;
		p++;		
		n = atoi( buf );

		int j;
		for( j=0; j<n; j++ ) {
			char* next = strchr( p, ' ' );
			if( next ) *next = 0;
			
			t[j] = atoll( p );
						
			printf("%lld ", t[j]);
			p = next+1;
		}		
		printf("\n");
		
		do_record( i, t, n );		
	}
	

	fclose( file );
	fclose( out_file );
	return 0;
	
}
