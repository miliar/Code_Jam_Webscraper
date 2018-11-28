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

const int big = 1000000000 ;
const int lm = 1010 ;

typedef long long ll ;

int T[lm] ;
int V[lm] ;
int H[lm] ;

ll K(ll n, ll h, ll t)
{
	if ( t < h ) return T[n] ;
	//return 2 * max(t - h, 0) + T[n] - t + h ;
	return T[n] + max(t - h, 0ll) / 2 ;
}

ll go(ll n, ll t, ll l)
{
	ll s = 0 ;

	fb (i, n)
	{
		V[i] = 2 * T[i] ;
		H[i] = 2 * T[i] + ( i ? H[i - 1] : 0 ) ;
		s += 2 * T[i] ;
	}

	ll r = big ;

	if ( l == 0 ) return s ;
	if ( l == 1 ) fb (i, n) r = min(r, s - V[i] + K( i, H[i - 1], t ) ) ;

	if ( l == 2 )
	{
		fb (i, n) fv (u, i + 1, n)
		{
			ll c = 0 ;

			fb (j, n)
			{
				if ( j == i || j == u ) c += K(j, c, t) ;
				else c += 2 * T[j] ;
			}

			r = min(r, c) ;
		}
	}

	return r ;
}

int main()
{
	int t ; cin >> t ;

	fb (i, t)
	{
		ll l, t, n, c ; cin >> l >> t >> n >> c ;
		vector <int> g(c) ;
		fe (u, g) cin >> g[u] ;

		fb (u, n) T[u] = g[u % c] ;

		printf ("Case #%d: %lld\n", i + 1, go(n, t, l)) ;
	}

	return 0 ;
}

