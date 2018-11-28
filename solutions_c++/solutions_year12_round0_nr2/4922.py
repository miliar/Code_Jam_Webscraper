#include <algorithm>
#include <bitset>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
 
using namespace std ;

#define all(n) n.begin(), n.end()
#define fb(i, n) fv (i, 0, n)
#define fe(i, n) fb (i, n.size())
#define fi(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)
#define fv(i, s, n) for ( int i = s ; i < n ; i++ )
#define LOG cerr << "[" << __LINE__ << "] "
#define pb push_back

int main()
{
	int t ; cin >> t ;

	fb (i, t)
	{
		int n, s, p ; cin >> n >> s >> p ;
		
		int r = 0 ;
		fb (u, n)
		{
			int q ; cin >> q ;
			if (q >= p * 3 - 2) r++ ;
			else if (p > 1 && q >= p * 3 - 4 && s > 0)
			{
				r++ ;
				s-- ;
			}
		}

		printf ("Case #%d: %d\n", i + 1, r) ;
	}

	return 0 ;
}

