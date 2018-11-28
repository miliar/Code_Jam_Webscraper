#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

#define forn(i,n) for( int i=0 ; i<(n) ; ++i )
#define forall(i,c) for( typeof( (c).begin() ) i = (c).begin() ; i != (c).end() ; ++i )
#define all(c) (c).begin() , (c).end()
#define debug(x) cout << __LINE__ << " => " << __func__/*__PRETTY_FUNCTION__*/ << " => " << #x << " = " << (x); cin.get() 
using namespace std;

template <class T> ostream& operator<<( ostream& o , vector<T>& v ){
	o << '[';
	for( int i=0 ; i < v.size() ; ++i )
		o << v[i] << ',';
	o << "\b]\n";
	return o;
}

template <class U, class V> ostream& operator<<( ostream& o , pair<U,V>& p ){
	o << '(' << p.first << ',' << p.second << ')';
	return o;
}

int L, D, N;
vector< string > words;
string s;

int main(){
	cin >> L >> D >> N;
	words.resize( D );
	forall( i, words )
		cin >> (*i);
	forn( i, N ){
		vector< vector< bool > > tab( L, vector<bool>( 27, false ) );
		int k = -1, count = 0;
		cin >> s;
		forn( j, L )
			if( s[++k] !=  '(' )
				tab[ j ][ s[k]-'a' ] = true;
			else
				while( s[++k] != ')' )
					tab[ j ][ s[k]-'a' ] = true;
		forall( j, words ){
			++count;
			forn( l, j->size() )
				if( !tab[ l ][ (*j)[l]-'a' ] ){
					--count;
					break;
				}
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
}