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

typedef vector <int> vi ;
typedef vector <vi> vii ;
typedef vector <string> vs ;

const int big = 2000000000 ;

int z[][2] = {-1, 0, 0, -1, 0, 1, 1, 0} ;
char ls = 'a' ;

inline int vl ( int y, int x, vii &a )
{
	if ( y >= 0 && x >= 0 && y < a.size() && x < a[0].size() ) return a[y][x] ;
	return big ;
}

char ff ( vii &a, vs &n, int y, int x )
{
	/*cout << "Fue a " << y << ' ' << x ;
	getchar() ;*/

	if ( n[y][x] ) return n[y][x] ;
	
	int p = 0 ;
	int c = big ;
	
	fb (i, 4) if ( vl( y + z[i][0], x + z[i][1], a ) < c ) { c = vl( y + z[i][0], x + z[i][1], a ), p = i ; }
	
	if ( c >= a[y][x] ) n[y][x] = ls++ ;
	else n[y][x] = ff(a, n, y + z[p][0], x + z[p][1]) ;
	
	return n[y][x] ;
}

void wts()
{
	int h, w ;
	cin >> h >> w ;
	
	ls = 'a' ;
	
	vii a(h, vi(w)) ;
	vs n (h, string(w, 0)) ;
	
	fb (i, h) fb (u, w) cin >> a[i][u] ;
	fb (i, h) fb (u, w) ff(a, n, i, u) ;
	
	fb (i, h)
	{
		fb (u, w) cout << n[i][u] << ' ' ;
		cout << endl ;
	}
}	

int main()
{
	int t ;
	cin >> t ;
	
	fb (i, t)
	{
		cout << "Case #" << i + 1 << ":" << endl ;
		wts() ;
	}
	
	return 0 ;
}
