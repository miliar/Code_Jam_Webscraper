#include <cstdio>
#include <cstring>

using namespace std;

const int MXN = 110;
const int INF = 1<<20;

int N, M;
int polje[MXN][MXN];
char sink[MXN][MXN];
char sto;

struct point{
	int r, s;

	point( void ){ r = s = 0; }
	point( int r_, int s_){ r = r_; s = s_; }

	bool ok( void ){ return r >= 0 && s >= 0 && r < N && s < M; }

};
inline point operator +( const point &a, const point &b ){ return point( a.r+b.r, a.s+b.s ); }

const point delta[4] = { point(-1,0), point(0,-1), point(0,1), point(1,0) };


void nadji( point x ){

	point koji;
	int mn = INF;

	for( int i = 0; i < 4; i++ ){
		point now = x + delta[i];
		if( !now.ok() ) continue;

		if( polje[now.r][now.s] < mn ){
			mn = polje[now.r][now.s];
			koji = now;
		}

	}

	if( mn >= polje[x.r][x.s] ){ //znaci da sam SINK
		sink[x.r][x.s] = sto;
		sto++;
		return;
	}

	if( sink[koji.r][koji.s] == 0 )
		nadji( koji );
	sink[x.r][x.s] = sink[koji.r][koji.s];
}

void solve( void ){
	memset( sink, 0, sizeof(sink) );

	scanf( "%d %d", &N, &M );
	for( int i = 0; i < N; i++ )
		for( int j = 0; j < M; j++ )
			scanf( "%d", &polje[i][j] );

	sto = 'a';
	for( int i = 0; i < N; i++ ){
		for( int j = 0; j < M; j++ ){
			if( sink[i][j] == 0 )
				nadji( point(i,j) );
		}
	}

	for( int i = 0; i < N; i++, printf( "\n" ) )
		for( int j = 0; j < M; j++ )
			printf( "%c ", sink[i][j] );

}

int main( void ){
	int T;
	scanf( "%d", &T );

	for( int i = 1; i <= T; i++ ){
		printf( "Case #%d:\n", i );
		solve();
	}

	return 0;
}
