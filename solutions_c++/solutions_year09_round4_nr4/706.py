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

typedef pair <int, int> pii ;
typedef pair <pii, int> ppi ;
#define Y first
#define X second

#define y Y.Y
#define x Y.X
#define r X

double ds ( ppi a, ppi b )
{
	double p = sqrt ( pow(a.y - b.y, 2.) + pow( a.x - b.x, 2. ) ) ;
	return (p + a.r + b.r) / 2 ;
}

double solve()
{
	int n ;
	cin >> n ;
	
	vector <ppi> k (n) ;
	fb (i, n) cin >> k[i].y >> k[i].x >> k[i].r ;
	
	if ( n == 1 ) return k[0].r ;
	if ( n == 2 ) return min( ds(k[0], k[1]), (double)max(k[0].r, k[1].r) ) ;
	
	double r = min( ds( k[0], k[1] ), min( ds ( k[1], k[2] ), ds( k[2], k[0] ) ) ) ;
	return r ;
}

int main()
{
	int c ;
	cin >> c ;
	
	fb (i, c) cout << "Case #" << i + 1 << ": " << solve() << endl ;
	return 0 ;
}

