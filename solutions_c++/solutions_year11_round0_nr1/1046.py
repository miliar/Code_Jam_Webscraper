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

const int big = 2000000000 ;

bool T[110] ;
int F[110] ;
int N ;

int G[110][110][110] ;
int P(int n, int a, int b)
{
	if ( n >= N ) return 0 ;
	if ( a > 100 || b > 100 || a < 1 || b < 1 ) return big ;

	int &g = G[n][a][b] ;
	if ( g != -1 ) return g ;
	g = big ;

	if ( !T[n] )
	{
		int v = abs(a - F[n]) + 1 ;
		fv (i, -v, v + 1) g = min(g, P(n + 1, F[n], b + i) + v ) ;
	}
	else
	{
		int v = abs(b - F[n]) + 1 ;
		fv (i, -v, v + 1) g = min(g, P(n + 1, a + i, F[n]) + v ) ;
	}

	return g ;
}

int main()
{
	int t ; cin >> t ;
	fb (i, t)
	{
		cin >> N ;
		fb (u, N)
		{
			char a ; cin >> a ;
			T[u] = ( a == 'B' ) ;
			cin >> F[u] ;
		}

		memset (G, -1, sizeof G) ;
		printf ("Case #%d: %d\n", i + 1, P(0, 1, 1) ) ;

		//cout << P(0, 1, 1) << ' ' << P(1, 2, 1) << ' ' << P(2, 3, 1) << ' ' << P(3, 4, 2) << endl ;
	}

	return 0 ;
}

