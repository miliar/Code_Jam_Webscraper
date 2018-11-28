#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define rep(i,n) for( int i = 0, _n = (n); i < _n; i++ )
#define forn(i,a,b) for( int i = (a), _n = (b); i <= _n; i++ )
#define ford(i,a,b) for( int i = (a), _n = (b); i >= _n; i-- )
#define foreach(it,c) for( typeof((c).begin()) it = (c).begin(); it != (c).end(); it++ )

#define debug(x) cout << ">>" << #x << " = " << x << endl;

#define two(x) (1<<(x))
#define contain(S,x) (((S)&two(x)) > 0)
#define twoll(x) (1LL<<(x))
#define containll(S,x) (((S)&twoll(x))>0)

#define pb push_back
#define mp make_pair

void open()
{
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "C0.out", "w", stdout );
}

int a[105][105];
int b[105][105];
int nx, ny;

int allzero( int a[105][105] )
{
	rep( i, ny+1 ) rep( j, nx+1 )
		if( a[i][j] != 0 ) return 0;
	return 1;	
}

int main()
{
	open();
	
	int ntc; scanf( "%d", &ntc );
	rep( T, ntc )
	{
		int R; scanf( "%d", &R );
		memset( a, 0, sizeof(a) );
		nx = ny = 0;
		
		rep( i, R )
		{
			int x1, x2, y1, y2;
			scanf( "%d %d %d %d", &x1, &y1, &x2, &y2 );
			x1--; x2--; y1--; y2--;
			if( x1 > x2 ) swap( x1, x2 );
			if( y1 > y2 ) swap( y1, y2 );
			
			forn( j, y1, y2 )
				forn( k, x1, x2 )
					a[j][k] = 1;
					
			nx = max( nx, x2 );
			ny = max( ny, y2 );
		}	

		memset( b, 0 ,sizeof(b) );
		int t = 0;
		while( !allzero( a ) )
		{
			
			forn( i, 1, ny ) forn( j, 1, nx )
			{
				if( a[i][j] == 1 )
				{
					if( a[i-1][j] == 0 && a[i][j-1] == 0 )
						b[i][j] = 0;
					else b[i][j] = a[i][j];
				}
				else
				{
					if( a[i-1][j] == 1 && a[i][j-1] == 1 )
						b[i][j] = 1;
					else b[i][j] = a[i][j];
				}
			} 
			
			rep( i, ny+1 ) rep( j, nx+1 ) a[i][j] = b[i][j];
			t++;
		}
		printf( "Case #%d: %d\n", T+1, t );
	}
	return 0;
}
