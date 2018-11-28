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

typedef vector <int> vi ;
typedef pair <int, int> pii ;
typedef vector < pii > vpi ;

#define y first
#define x second

int nb(int n)
{
	while ( n > 1 ) n /= 2 ;
	return n ;
}

int dg ( int n, int u )
{
	fb (i, u) n /= 2 ;
	return n % 2 ;
}

int te()
{
	int n ; cin >> n ;
	int r = 0 ;
	
	vi g( 1 << n ) ;
	vpi m( 1 << n ) ;
	
	fe (i, m)
	{
		cin >> m[i].y ;
		m[i].x = ( 1 << n ) + i ;
	}
	
	int ig ;
	fb (i, n) fb (u, ( 1 << i ) ) cin >> ig ;
	
	sort ( all ( m ) ) ;
	
	//fe (i, m) cout << m[i].y << ' ' << m[i].x << ", " ; cout << endl << endl ;
	
	fe (i, m)
	{
		int t = n - m[i].y ;
		int s = 0, j = m[i].x ;
		
		//cout << "Hay " << t << " en " << m[i].x << endl ;
		for ( int h = m[i].x / 2 ; h > 0 ; h /= 2 ) if ( g[h] ) t-- ;
		//cout << "Quedan " << t << endl ;
		
		for ( int w = 1, u = n - 1 ; t > 0 && w < m[i].x ; w *= 2, w += dg(j, u), u-- )
		{
			if ( !g[w] )
			{
				g[w] = true ;
				t-- ;
				r++ ;
			}
		}
		
		//fe (i, g) cout << g[i] << ' ' ; cout << "(" << r << ")" << endl ;
		//cout << endl ;
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

