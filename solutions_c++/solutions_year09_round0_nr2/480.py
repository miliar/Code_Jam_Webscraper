#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

#define forn(i,n) for( int i=0 ; i<(n) ; ++i )
#define forall(i,c) for( typeof( (c).begin() ) i = (c).begin() ; i != (c).end() ; ++i )
#define all(c) (c).begin() , (c).end()
#define entre(a,b,c) (((a)<=(b))&&((b)<(c)))
#define debug(x) cout << __LINE__ << " => " << __func__/*__PRETTY_FUNCTION__*/ << " => " << #x << " = " << (x) 
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

vector< vector<int> > height, sol;
int T, H, W, next = 0;
int my[] = { -1 , 0 , 0 , 1 };
int mx[] = { 0 , -1 , 1 , 0 };
typedef pair<int,int> punto;
vector< punto > side;
vector< vector< vector<punto> > > comp;
vector<punto> bfs(10000);

void llena( int y , int x){
	side.resize(0);
	forn(i,4)
		if( entre( 0, y+my[i], height.size() ) &&
			entre( 0, x+mx[i], height[0].size() ) )
				side.push_back( punto ( height[ y+my[i] ][ x+mx[i] ] , i ) );
	sort( all(side) );

	if( !side.size() || side[0].first >= height[y][x] ){
		sol[y][x] = next++;
		bfs.push_back( punto(y,x) );
	}else
		comp[ y+my[ side[0].second ] ][ x+mx[ side[0].second ] ].push_back (punto(y,x));
}

int main(){
	cin >> T;
	forn( a, T ){
		cin >> H >> W ;

		height = sol = vector< vector<int> >( H, vector<int>( W, -1 ) );
		comp = vector< vector< vector<punto> > >( H, vector< vector< punto > >(W));
		bfs.resize(0);

		forall( i, height )
			forall( j, *i )
				cin >> (*j);

		forn( i, H )
			forn( j, W )
				llena( i, j );

		int lee=-1;
		while( ++lee < bfs.size() )
			forall( i, comp[ bfs[lee].first ][ bfs[lee].second ] ){
				bfs.push_back( *i );
				sol[ i->first ][ i->second ] = sol[ bfs[lee].first ][ bfs[lee].second ];
			}

		map<int,int> L;
		map<int,int>::iterator iter;
		int letter = 'a';

		cout << "Case #" << a+1 << ':' << endl;

		forall( i, sol ){
			forn( j, i->size()-1 )
				if( ( iter = L.find( (*i)[j] ) ) != L.end() )
					cout << (char) iter->second << ' ';//(*j) = iter->second;
				else{
					L.insert( pair<int,int>( (*i)[j] , letter ));
					cout << (char) letter++ << ' ';//(*j) = letter++ ;
				}
			if( ( iter = L.find( i->back() ) ) != L.end() )
				cout << (char) iter->second << endl;//(*j) = iter->second;
			else{
				L.insert( pair<int,int>( i->back() , letter ));
				cout << (char) letter++ << endl;//(*j) = letter++ ;
			}
		}
	}
}