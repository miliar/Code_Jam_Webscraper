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
		int n, l, h ; cin >> n >> l >> h ;
		vector <int> p(n) ;

		fe (u, p) cin >> p[u] ;

		bool e = true ;
		fv (u, l, h + 1)
		{
			e = true ;
			fe (j, p) if ( u % p[j] != 0 && p[j] % u != 0 ) e = false ;

			if (e)
			{
				printf ("Case #%d: %d\n", i + 1, u) ;
				break ;
			}
		}

		if ( !e ) printf ("Case #%d: NO\n", i + 1) ;
	}

	return 0 ;
}

