#include <cstdio>
#include <cstring>

using namespace std;

const int MXN = 510;
const char what[30] = "welcome to code jam";
const int K = 19;
const int MOD = 10000;

char niz[MXN];
int N;
int mem[MXN][K+2];

int f( int i, int j ){ //i je u niz-u index
	if( j == K ) return 1;
	if( i == N ) return 0;

	int &ref = mem[i][j];
	if( ref != -1 ) return ref;

	int ret = 0;

	if( niz[i] == what[j] ) ret += f( i+1, j+1 );
	ret += f( i+1, j );

	return ref = ret % MOD;

}

int main( void ){

	int T;
	scanf( "%d\n", &T );
	for( int i = 1; i <= T; i++ ){

		fgets( niz, 1000, stdin );
		N = strlen( niz );

		memset( mem, -1, sizeof(mem) );
		printf( "Case #%d: %.4d\n", i, f( 0, 0 ) );
	}

	return 0;
}
