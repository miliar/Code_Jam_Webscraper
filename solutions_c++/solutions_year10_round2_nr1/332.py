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

typedef vector <string> vs ;
typedef pair < vs, bool > pss ;

#define y first
#define x second

vs upars ( string &n )
{
	vs r ;
	int d, a = 1 ;
	
	while ( ( d = n.find('/', a) ) != -1 )
	{
		string h = n.substr( a, d - a ) ;
		a = d + 1 ;
		
		r.pb(h) ;
	}
	
	r.pb ( n.substr(a) ) ;
	
	return r ;
}

int mc ( vs &a, vs &b )
{
	int r = 0 ;
	fb (i, min(a.size(), b.size()) )
		if ( a[i] == b[i] ) r++ ;
		else break ;
	
	return r ;
}

int te()
{
	int n, m ;
	cin >> n >> m ;
	
	int r = 0 ;
	
	vector <pss> p ( n + m ) ;
	fb (i, n) { string h ; cin >> h ; p[i    ] = pss( upars(h), false ) ; }
	fb (i, m) { string h ; cin >> h ; p[i + n] = pss( upars(h), true  ) ; }

	sort ( all ( p ) ) ;
	
	fe (i, p)
	{
		//fe (u, p[i].y) cout << p[i].y[u] << ' ' ;
		//cout << endl ;
	}

	fe (i, p) if ( p[i].x )
	{
		if ( i == 0 ) r += p[i].y.size() ;
		else r += p[i].y.size() - mc( p[i].y, p[i - 1].y ) ;
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

