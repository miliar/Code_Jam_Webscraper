#include <cstdio>
#include <cstdlib>
#include <string>

const int N = 'z' - 'a' + 1;

using namespace std;

struct Node {
	int kraj, inited;
	Node *child;
	
	Node( void ) { kraj = 0; inited = 0; child = NULL;}
	~Node( void ) { if( child != NULL ) delete []child; }
	void Init( void ) { inited = 1; if( child == NULL ) child = new Node[ N ]; }
};

Node node[ N ];
char buff[ 10005 ];
char cons[ 10005 ];
int l, d, n;

void ubaci( char *st ) {
	Node *tren; tren = &( node[ st[ 0 ] - 'a' ] );
	
	for( int i = 1; st[ i ] != 0; ++i ) {
		tren->Init();
		tren = &( tren->child[ st[ i ] - 'a' ] );
	}
	
	tren->Init(); tren->kraj = 1;
}

Node *dalje( Node *tren, char znak ) {
	if( tren == NULL ) return( &( node[ znak - 'a' ] ) );
	return( &( tren->child[ znak - 'a' ] ) );
}

int solve( char *st, Node *tren ) {
	if( st[ 0 ] == 0 ) return( tren->kraj );
	
	int rez = 0; Node *tmp;
	if( st[ 0 ] == '(' ) {
		int t = 0; while( st[ t++ ] != ')' );
		for( int i = 1; st[ i ] != ')'; ++i ) {
			tmp = dalje( tren, st[ i ] );
			if( !tmp->inited ) continue;
			rez += solve( st + t, tmp );
		}
	} else {
		rez += solve( st + 1, dalje( tren, st[ 0 ] ) );
	}
	
	return( rez );
}

void printout( Node *tren, int lev ) {
	if( !tren->inited ) return;
	if( tren->kraj ) { cons[ lev ] = 0; printf( "  %s\n", cons ); }
	
	for( int i = 0; i < N; ++i ) {
		cons[ lev ] = 'a' + i;
		printout( &( tren->child[ i ] ), lev + 1 );
	}
}

int main( void ) {
	scanf( "%d %d %d", &l, &d, &n );
	for( int i = 0; i < d; ++i ) {
		scanf( "%s", buff );
		ubaci( buff );
	}
	
	// DEBUG
	/*for( int i = 0; i < N; ++i ) {
		cons[ 0 ] = 'a' + i;
		printout( node + i, 1 );
	}*/
	
	for( int i = 0; i < n; ++i ) {
		scanf( "%s", buff );
		printf( "Case #%d: %d\n", i + 1, solve( buff, NULL ) );
	}
	return( 0 );
}
