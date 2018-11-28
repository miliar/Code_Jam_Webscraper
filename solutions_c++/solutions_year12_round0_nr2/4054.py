#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

char M[1000];

int solve(){
	int ans = 0;

	int N, S, p;
	scanf( "%d%d%d", &N, &S, &p );

	for( int i = 0; i < N; ++i ){
		int res;
		scanf("%d", &res);
		
		if( res % 3 == 0 ){
			// check good
			if( res / 3 >= p ){
				ans ++;
			}
			// check surprising
			else{
				if( S && (  ( res / 3 ) - 1 >= 0 ) ){
					if( ( res / 3 ) + 1 >= p ){
						ans ++;
						S--;
					}
				}
			}
		}

		if( res % 3 == 1 ){
			// only check good
			if( ( res / 3 ) + 1 >= p ){
				ans ++;
			}
		}

		if( res % 3 == 2 ){
			// check good
			if( ( res / 3 ) + 1 >= p ){
				ans ++;
			}
			// check surprising
			else{
				if( S ){
					if( ( res / 3 ) + 2 >= p ){
						ans ++;
						S--;
					}
				}
			}
		}

	}

	return ans;
}

void input_output(){
	int T;
	scanf( "%d\n", &T );
	for( int t = 1; t <= T; ++t ){
		printf("Case #%d: %d\n", t, solve() );
	}
}

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	input_output();

	return 0;
}