#include <cstdio>
#include <cstring>
#define INF 0x3f3f3f3f

int tree[10001];
int changeable[10001];
int memo[10001][2];
int M;

int min( int a, int b ){ return a < b? a : b; }

int oper( int a, int b, int op ){
	if( op == 0 ) return a || b;
	else return a && b;
}

int solve( int s, int v ){
	int &sol = memo[s][v];

	if( sol != -1 ) return sol;

	if( s > (M-1)/2 ) {
		if( v == tree[s] ) return sol = 0;
		else return sol = INF;
	}else{
		sol = INF;
		for( int a = 0; a <= 1; ++a ){
			for( int b = 0; b <= 1; ++b ){
				if( oper( a, b, tree[s] ) == v ) sol = min( sol, solve( s*2, a )+solve( s*2+1, b ) );
				if( changeable[s] && oper( a, b, !tree[s] ) == v ) sol = min( sol, solve( s*2, a )+solve( s*2+1, b )+1 );
			}
		}
	}
	return sol;
}

int main(){
	int tp;

	scanf( "%d", &tp );

	for( int tt = 1; tt <= tp; ++tt ){
		memset( memo, -1, sizeof memo );
		int V;
		scanf( "%d%d", &M, &V );
		for( int i = 0; i < (M-1)/2; ++i ) scanf( "%d%d", &tree[i+1], &changeable[i+1] );
		for( int i = (M-1)/2; i < M; ++i ) scanf( "%d", &tree[i+1] );

		int sol = solve( 1, V );

		if( sol == INF ) printf( "Case #%d: IMPOSSIBLE\n", tt );
		else printf( "Case #%d: %d\n", tt, sol );
	}

	return 0;
}
