#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std ;

#define fv(i, s, n) for ( int i = s ; i < n ; i++ )
#define fb(i, n) fv (i, 0, n)
#define fe(i, n) fb (i, n.size())
#define pb push_back
#define all(n) n.begin(), n.end()
#define fi(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)

const int md = 100003 ;

typedef vector <int> vi ;

int n ;

vi gt ( int b )
{
	vi g ;
	for ( int h = b, i = 2 ; h ; h /= 2, i++ ) if ( h % 2 ) g.pb ( i ) ;
	g.pb( n ) ;
	return g ;
}

bool val ( vi g )
{
	for ( int i = 0 ; i < g.size() ; i = g[i] - 1 ) if ( g[i] == n ) return true ;
	return false ;
}

int te()
{
	int r = 0 ;
	cin >> n ;
	
	
	for ( int b = 0 ; b < ( 1 << ( n - 2 ) ) ; b++ ) if ( val( gt( b ) ) )
	{
		//vi f = gt(b) ;
		//fe (i, f) cout << f[i] << ' ' ; cout << endl ;
		r = ( r + 1 ) % md ;
	}
	
	return r ;
}

int main()
{
	int t ;
	cin >> t ;
	
	fb (i, t) cout << "Case #" << i + 1 << ": " << te() << endl ;
	return 0 ;
}

