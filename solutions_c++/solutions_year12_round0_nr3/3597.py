#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
int get_i() { int a; scanf( "%d", &a ); return a; }

int n, m;

int main() {
	int t=0, tt=0;

	
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );

	for( t=1; t<=tt; t++ ) {
	
		int i=0, j=0, k=0, c=0, o=0, l=0;
	
		printf( "Case #%d:", t );
		
        int n_a = get_i();
        int n_b = get_i();
		
		int n = n_b-n_a;
		bool *res_set = (bool*) malloc( n * sizeof( bool ) ) ;

		
		int final_ans = 0;
		
		c=1;
		int tmp = n_a;
		while( (tmp/=10) ) c ++ ;
		
		int *history = (int *) malloc( c * sizeof( int ) );
		
		for( i=0; i<n; i++ ) {
			res_set[i] = true;
		}	
							
		for( i=0; i<n; i++ ) {
		
			int num = n_a + i + 1;
			//printf("working on num: %d\n", num );
			
			int mup = 1;
			for( j=0; j<c-1; j++ ) {
				mup *= 10;
			}
	
			//printf("| mup %d |\n", mup );
	
			int v = num;		
			
			for( j=0; j<c; j++ ) {
			
						
				v = (v/10) + ( ( v % 10) * mup );
				history[j] = v;
		
				bool is_found = false;
				for( k=0; k<j; k++ ) {
					if( v == history[k] ) {
						is_found = true;
						break;
					}
				}
				if( is_found ) continue;
												
			
				for( k=0; k<i; k++ ) {
				
					if( k+n_a == v ) {
						final_ans++;
						is_found = true;
					}	
				}
			}

						
		}
		
		printf(" %d\n", final_ans );	
				
		for( i=0; i<c; i++ ) {
			res_set[i] = -1;
		}	
	}

	return 0;
}
