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

typedef pair <int, int> pii ;
#define y first
#define x second

int te()
{
	int n, k, b, t ;
	cin >> n >> k >> b >> t ;
	
	vector <pii> p(n) ;
	int r = 0, v = 0, c = 0 ;
	
	fb (i, n) cin >> p[i].y ;
	fb (i, n) cin >> p[i].x ;
	
	for ( int i = p.size() - 1 ; i >= 0 && v < k ; i-- )
	{
		if ( t >= (int)ceil( double( b - p[i].y ) / p[i].x ) ) { r += c ; v++ ; }
		else c++ ;
	}
	
	if ( v >= k ) return r ;
	else return -1 ;
}

int main()
{
	int t ;
	cin >> t ;
	
	fb (i, t)
	{
		int g = te() ;
		cout << "Case #" << i + 1 << ": " ;
		
		if ( g == -1 ) cout << "IMPOSSIBLE" << endl ;
		else cout << g << endl ;
	}
	
	return 0 ;
}

