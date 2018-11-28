#define _CRT_SECURE_NO_DEPRECATE

#include <conio.h>
#include <stdio.h>
#include <memory.h>
#include <assert.h>
#include <math.h>

int ni() { int a; scanf( "%d", &a ); return a; }

int min( int a, int b ) { if(a>b) return a; return b; }
int min( int a, int b, int c) { return min( a, min(b,c) ); }


int max( int a, int b ) { if(a>b) return a; return b; }
int max( int a, int b, int c) { return max( a, max(b,c) ); }

void do_case() {

	//printf("\n");
	
	int N = ni();
	int S = ni();
	int p = ni();

	int i,j,k;

	int p_low = p-2;
	if( p_low <=0 ) p_low=0;
	int p3 = p+ p_low + p_low;

	int r = 0;
	for( i=0; i<N; i++ ) {

		int gs = ni();

		int m=0;
	
		int gs_r = gs%3;
		if( gs_r == 0 ) {
			m  = gs/3;
		}else {
			m = gs/3+1;
		}

		if( m >= p ) { 
			//printf("> gs %d\n", gs );
			r++;
		}else {
			
			if( S > 0 ) {
				if( gs >= p3 ) {
					r++;
					S--;
				}
			}

		}
		
	}

	printf("%d", r) ;

}

int main(int argc, char* argv[]) {


	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int i,n=0;
	scanf( "%d\n", &n );

	for( i=1; i<=n; i++ ) {

		printf( "Case #%d: ", i );
		do_case();
		printf("\n");
	}


	getch();

	return 0;
}

