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

int main()
{
	int t ; cin >> t ;
	fb (i, t)
	{
		int n ; cin >> n ;

		int g = 0, s = 0, m = big ;
		fb (u, n)
		{
			int a ; cin >> a ;
			g ^= a ; s += a ; m = min(m, a) ;
		}

		printf("Case #%d: ", i + 1) ;
		if ( g == 0 ) cout << s - m << endl ;
		else cout << "NO" << endl ;
	}

	return 0 ;
}

