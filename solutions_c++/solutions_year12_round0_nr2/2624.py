#include <stdio.h>
#include <memory.h>

int f[107][17] ;
int n, s, p ;
int good[107][2] ; // 0-no surprise

int solve( int depth, int s )
{
	if ( f[depth][s] != -1 )
		return f[depth][s] ;
	if ( depth >= n )
		return 0 ;
	int tmp, tmps ;
	// no surprise
	tmp = good[depth][0] + solve( depth + 1, s ) ;
	
	if ( s > 0 )
		tmps = good[depth][1] + solve( depth + 1, s - 1 ) ;
	else
		tmps = -1 ;
		
	f[depth][s] = tmp > tmps ? tmp : tmps ;
	return f[depth][s] ;
}

int main()
{
	int t, tt ;
	int i, x ;
	scanf( "%d", &tt ) ;
	for ( t = 1 ; t <= tt ; ++t )
	{
		memset( f, -1, sizeof( f ) ) ;
		memset( good, 0, sizeof( good ) ) ;
		
		scanf( "%d %d %d", &n, &s, &p ) ;
		for ( i = 0 ; i < n ; ++i )
		{
			scanf( "%d", &x ) ;

			if ( x % 3 == 0 )
			{
				if ( x / 3 >= p )
					good[i][0] = 1 ;
				if ( x / 3 + 1 >= p && x >= 3 )
					good[i][1] = 1 ;
			}
			else if ( x % 3 == 1 )
			{
				if ( x / 3 + 1 >= p )
					good[i][0] = 1 ;
				if ( x / 3 + 1 >= p )
					good[i][1] = 1 ; 
			}
			else if ( x % 3 == 2 )
			{
				if ( x / 3 + 1 >= p )
					good[i][0] = 1 ;
				if ( x / 3 + 2 >= p )
					good[i][1] = 1 ;
			}
		}
		
		solve( 0, s ) ;
		printf( "Case #%d: %d\n", t, f[0][s] ) ;
	}
	return 0 ;
}
