#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>

using namespace std;

int t, n, m;
char buff[ 105 ];

struct Node {
	map< string, Node * > mapa;
	
	int Exists( string st ) { return( mapa.find( st ) != mapa.end() ); }
	
	Node *Enter( string st ) {
		if( !Exists( st ) ) {
			Node *node = new Node();
			mapa.insert( make_pair( st, node ) );
		}
		return( mapa[ st ] );
	}
	
	void Destroy( void ) {
		for( map< string, Node * >::iterator it = mapa.begin(); it != mapa.end(); ++it )
			it->second->Destroy();
		mapa.clear();
	}
	
} root;

int procesiraj( string st ) {
	Node *tren = &root;
	st.push_back( '/' );
	
	int poz = 1, cnt = 0;
	int len = ( int )st.size();
	
	for( int i = 1; i < len; ++i )
		if( st[ i ] == '/' ) {
			string tmp = st.substr( poz, i - poz );
			cnt += !tren->Exists( tmp );
			tren = tren->Enter( tmp );
			poz = i + 1;
		}
	
	return( cnt );
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d %d", &n, &m );
		root.Destroy();
		
		for( int j = 0; j < n; ++j ) {
			scanf( "%s", buff );
			procesiraj( string( buff ) );
		}
		
		int rez = 0;
		for( int j = 0; j < m; ++j ) {
			scanf( "%s", buff );
			rez += procesiraj( string( buff ) );
		}
		
		printf( "Case #%d: %d\n", i+1, rez );
	}
	return( 0 );
}
