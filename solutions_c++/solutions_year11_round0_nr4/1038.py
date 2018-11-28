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

int main()
{
	int t ; cin >> t ;
	fb (i, t)
	{
		int n ; cin >> n ;
		vector <int> g(n), h(n) ;

		fb (u, n)
		{
			cin >> g[u] ;
			h[u] = g[u] ;
		}

		sort ( all ( g ) ) ;

		int f = 0 ;
		fe (u, g) if ( g[u] != h[u] ) f++ ;

		printf ("Case #%d: %d.000000\n", i + 1, f) ;
	}

	return 0 ;
}

