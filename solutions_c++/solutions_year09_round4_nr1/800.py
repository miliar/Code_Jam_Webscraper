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

int solve()
{
	int n ;
	cin >> n ;
	
	vector <int> k(n, 0) ;
	fb (i, n)
	{
		string h ;
		cin >> h ;
		
		fe (u, h) if ( h[u] == '1' ) k[i] = u ;
	}

	int r = 0 ;
	fe (i, k) fv (u, i, k.size()) if ( k[u] <= i )
	{
		int p = k[u] ;
		r += u - i ;
		k.erase ( k.begin() + u ) ;
		k.insert ( k.begin() + i, p ) ;
		
		break ;
	}
	
	return r ;
}
	
int main()
{
	int t ;
	cin >> t ;
	
	fb (i, t) cout << "Case #" << i + 1 << ": " << solve() << endl ;
	return 0 ;
}
