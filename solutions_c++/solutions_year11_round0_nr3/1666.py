#include<cstdio>
#include<cstring>
#define min(x,y) ((x)<(y)?(x):(y))
#define INF 10000000 
using namespace std;
int main(){
	int T, _case = 0;
	scanf( "%d", &T );
	while( T -- ){
		int add_sum = 0, xor_sum = 0, _min = INF;
		int N;
		scanf( "%d", &N );
		for( int i = 0; i < N; i ++ ){
			int c;
			scanf( "%d", &c );
			xor_sum ^= c;
			add_sum += c;
			_min = min( _min, c );
		}
		printf( "Case #%d: ", ++ _case );
		if( xor_sum != 0 ){
			printf( "NO\n");
		}else{
			printf( "%d\n", add_sum - _min );
		}
	}
	return 0;
}
