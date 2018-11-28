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

vector <string> T ;

bool go()
{
	fe (i, T) fe (u, T[i]) if ( T[i][u] == '#' )
	{
		if ( i + 1 >= T.size() || u + 1 >= T[i].size() ) return false ;
		if ( T[i + 1][u] != '#' || T[i][u + 1] != '#' || T[i + 1][u + 1] != '#' ) return false ;
		T[i][u] = T[i + 1][u + 1] = '/' ;
		T[i + 1][u] = T[i][u + 1] = '\\' ;
	}

	return true ;
}

int main()
{
	int t ; cin >> t ;

	fb (i, t)
	{
		int n, m ; cin >> n >> m ;
		T = vector < string > (n) ;

		fe (u, T) cin >> T[u] ;
		
		if ( !go() ) printf ("Case #%d:\nImpossible\n", i + 1) ;
		else
		{
			printf ("Case #%d:\n", i + 1) ;
			fb (u, n) { fb (j, m) cout << T[u][j] ; cout << endl ; }
		}
	}

	return 0 ;
}

