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

typedef long long ll ;
typedef vector <int> vi ;

ll te()
{
	ll r, k, n ;
	cin >> r >> k >> n ;
	
	vi s(n), ne(n), pt(n) ;
	fe (i, s) cin >> s[i] ;
	
	fe (i, s)
	{
		ll u, p = s[i] ;
		for ( u = ( i + 1 ) % n ; u != i && p + s[u] <= k ; u++, u %= n ) p += s[u] ;
		
		ne[i] = u ;
		pt[i] = p ;
	}
	
	ll p = 0 ;
	ll w = 0 ;
	
	fb (i, r)
	{
		w += pt[p] ;
		p = ne[p] ;
	}
	
	return w ;
}		

int main()
{
	int t ; cin >> t ;
	
	fb (i, t)
	{
		printf ("Case #%d: %lld\n", i + 1, te()) ;
	}
	
	return 0 ;
}
