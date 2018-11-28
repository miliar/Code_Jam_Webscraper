#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std ;

bool g[40][40] ;
int d[40][40] ;
int res ;
bool v[40], s[40] ;
int p, w ; 

void solve( int x ) 
{	
	if ( x==1 ) 
	{
		memset( s, 0, sizeof s ) ;
		for ( int i = 0 ; i < p ; ++i ) 
			if ( v[i] ) 
				for ( int j = 0 ; j < p ; ++j ) 
					if ( g[i][j] ) 
						s[j] = true ;
		int tmp = 0 ; 
		for ( int i = 0 ; i < p ; ++i ) 
			if ( s[i] && !v[i] ) 
				++tmp ;
		res = max( res, tmp ) ;
	}
	v[x] = true ;
	for ( int i = 0 ; i < p ; ++i ) if ( g[x][i] ) 
		if ( d[1][i] == d[1][x] - 1 )
			solve(i) ;
	v[x] = false ;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int tt  ;
	cin >> tt ;
	for ( int tests = 1 ; tests <= tt ; ++tests )
	{
		cin >> p >> w ;
		memset( d, 0, sizeof d ) ;
		memset( g, 0, sizeof g ) ;
		for ( int i = 0 ; i < p ; ++i ) 
			for ( int j = 0 ; j < p ; ++j ) 
				d[i][j] = (i==j)?0:10000 ;
		for ( int i = 0 ; i < w ; ++i ) 
		{
			string st ;
			cin >> st ;
			replace( st.begin(), st.end(), ',', ' ' ) ;
			istringstream sin(st);
			int a, b ;
			sin >> a >> b ;
			d[a][b] = d[b][a] = 1 ;
			g[a][b] = g[b][a] = 1 ;
		}
		for ( int k = 0 ; k < p ; ++k ) 
			for ( int i = 0 ; i < p ; ++i )
				for ( int j = 0 ; j < p ; ++j )
					d[i][j] = min( d[i][j], d[i][k] + d[k][j] ) ;

		res = 0 ; 
		memset( v, 0, sizeof v ) ;
		solve( 0 ) ;

		cout << "Case #" << tests << ": " << d[0][1]-1 << ' ' << res << endl ;
	}
}