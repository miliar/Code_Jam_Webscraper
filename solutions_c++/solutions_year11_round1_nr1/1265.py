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

bool P(int n, int pd, int pg)
{
	if ( pg == 100 && pd != 100 || pg == 0 && pd != 0 ) return false ;

	int f = __gcd(pd, 100) ;
	if ( 100 / f > n ) return false ;
	return true ;
}

int main()
{
	int t ; cin >> t ;

	fb (i, t)
	{
		int n, pd, pg ;
		cin >> n >> pd >> pg ;

		printf ("Case #%d: %s\n", i + 1, P(n, pd, pg) ? "Possible" : "Broken" ) ;
	}

	return 0 ;
}
