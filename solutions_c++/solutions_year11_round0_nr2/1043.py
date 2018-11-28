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

int P[30][30] ;
bool T[30][30] ;

void go(int q)
{
	int c, d, n ;
	string f ;

	cin >> c ;
	fb (i, c)
	{
		string s ; cin >> s ;
		int a = s[0] - 'A', b = s[1] - 'A', c = s[2] - 'A' ;
		
		P[a][b] = P[b][a] = c ;
	}

	cin >> d ;
	fb (i, d)
	{
		string s ; cin >> s ;
		int a = s[0] - 'A', b = s[1] - 'A' ;

		T[a][b] = T[b][a] = true ;
	}

	list <int> s ;

	cin >> n >> f ;
	fe (i, f)
	{
		int c = f[i] - 'A' ;

		while ( true )
		{
			if ( !s.empty() )
			{
				bool x = false ;

				if ( P[c][ s.back() ] != -1 ) { c = P[c][ s.back() ] ; s.pop_back() ; continue ; }

				fi (i, s) if ( T[c][*i] ) { s.clear() ; x = true ; break ; }
				if (x) break ;
			}

			s.push_back(c) ;
			break ;
		}
	}

	int l = s.size() ;

	printf ("Case #%d: [", q) ;
	fi (i, s) printf ("%c%s", *i + 'A', !--l ? "" : ", ") ;
	printf ("]\n") ;
}

int main()
{
	int t ; cin >> t ;
	fb (i, t)
	{
		memset ( P, -1, sizeof P ) ;
		memset ( T, 0, sizeof T ) ;

		go(i + 1) ;
	}

	return 0 ;
}

