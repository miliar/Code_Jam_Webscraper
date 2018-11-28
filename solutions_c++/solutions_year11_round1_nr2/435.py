#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std ;
 
#define fv(i, s, n) for ( int i = s ; i < n ; i++ )
#define fb(i, n) fv (i, 0, n)
#define fe(i, n) fb (i, n.size())
#define pb push_back
#define all(n) n.begin(), n.end()
#define fi(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++) 

typedef pair <int, int> pii ;
#define y first
#define x second

const int lm = 150 ;
string T[lm] ;
bool B[lm] ;

string f ;

typedef vector <bool> vb ;

vb st(int a, int b)
{
	vb r( T[a].size() ) ;
	fe (i, T[a]) if ( T[a][i] == f[b] ) r[i] = true ;
	return r ;
}

int P(int n, int m)
{
	pii r ;
	fb (i, n)
	{
		memset (B, 0, sizeof B) ;

		int c = n ;
		int p = 0 ;
		fe (u, f)
		{
			if ( c == 1 ) { r = max( r, pii(p, -i) ) ; break ; }

			bool e = false ;
			for ( ; !e ; u++ ) fb (j, n) if ( !B[j] )
			{
				if ( T[j].size() != T[i].size() ) continue ;
				fe (k, T[j]) if ( T[j][k] == f[u] ) e = true ;
			}
			u-- ;

			if ( T[i].find ( f[u] ) == -1 ) p++ ;

			vb g = st( i, u ) ;
			fb (j, n) if ( !B[j] && ( T[j].size() != T[i].size() || st( j, u ) != g ) )
			{
				B[j] = true ;
				c-- ;
			}
		}
	}

	return -r.x ;
}

int main()
{
	int t ; cin >> t ;

	fb (i, t)
	{
		int n, m ; cin >> n >> m ;
		fb (u, n) cin >> T[u] ;
		
		printf ("Case #%d: ", i + 1) ;
		fb (u, m)
		{
			cin >> f ;
			//vector <int> l(30) ;
			//fe (i, f) l[ f[i] - 'a' ] = i ;

			printf ("%s%c", T[ P(n, m) ].c_str(), u == m - 1 ? '\n' : ' ' ) ;
		}
	}

	return 0 ;
}

