#include<cstdio>
using namespace std;
#define abs(x) ((x)>0?(x):-(x))
int main(){
	
	int T, _case = 0;
	scanf( "%d", &T );
	while( T -- ){
		int N;
		int oc = 0, op = 1;
		int bc = 0, bp = 1;
		int time = 0;

		scanf( "%d", &N );
		for( int i = 0; i < N; i ++ ){
			int p;
			char r;
			scanf( "%s %d", &r, &p );
			if( r == 'O' ){
				int dt;
				dt = abs( p - op );
				time += 1;
				bc += 1;
				if( oc < dt ){
					dt -= oc;
					time += dt;
					bc += dt;
				}
				op = p;
				oc = 0;
			}else{
				int dt;
				dt = abs( p - bp );
				time += 1;
				oc += 1;
				if( bc < dt ){
					dt -= bc;
					time += dt;
					oc += dt;
				}
				bp = p;
				bc = 0;	
			}
		}

		printf( "Case #%d: %d\n", ++_case, time );
	}
	
	return 0;
}
