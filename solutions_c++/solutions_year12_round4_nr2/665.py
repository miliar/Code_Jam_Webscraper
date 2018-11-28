#include <stdio.h>
#include <string.h>

int s[101] ;
int n, w, l ;
int r[101] ;
int result[101][2] ;

bool Verify() 
{
	int cw, cl ;
	int i ;
	int max = 0 ;
	cw = cl = -r[ s[0] ] ;
	//for ( i = 0 ; i < n ; ++i )
	//	if ( r[i] > w )
	//		return false ;
			
	for ( i = 0 ; i < n ; ++i )
	{
		if ( cw + r[ s[i] ] < w )
		{
			if ( cl + r[ s[i] ] > l )
				return false ;
			result[ s[i] ][0] = cw + r[ s[i] ] ;
			result[ s[i] ][1] = cl + r[ s[i] ] ;
			if ( result[ s[i] ][1] < 0 )
				result[ s[i] ][1] = 0 ;
				
			//printf( "%d %d %d\n", s[i], cw + r[ s[i] ], cl + r[ s[i] ] ) ;
			cw += 2 * r[ s[i] ] ;
			if ( r[ s[i] ] > max )
				max = r[ s[i] ] ;
		}
		else // new line
		{	
			cw = -r[ s[i] ] ;
			cl += 2 * max ;
			max = 0 ;
			--i ;
		}
	}
	
	return true ;
}

bool solve( int depth )
{
	int tmp, i ;
	
	if ( depth == n )
	{
		return Verify() ;
	}
	
	for ( i = depth ; i < n ; ++i )
	{
		tmp = s[i] ;
		s[i] = s[depth] ;
		s[depth] = tmp ;
		
		if ( solve( depth + 1 ) )
			return true ;
			
		tmp = s[i] ;
		s[i] = s[depth] ;
		s[depth] = tmp ;		
	}
	return false ;
}

int main()
{
	int t, tt ;
	int i ;
	scanf( "%d", &tt ) ;
	for ( t = 1 ; t <= tt ; ++t )
	{
		scanf( "%d %d %d", &n, &w, &l ) ;
		for ( i = 0 ; i < n ; ++i )
		{
			scanf( "%d", r + i ) ;
			s[i] = i ;
		}

		solve( 0 ) ;
		
		printf( "Case #%d: ", t ) ;
		for ( i = 0 ; i < n - 1 ; ++i )
			printf( "%d %d ", result[i][0], result[i][1] ) ;
		printf( "%d %d\n", result[i][0], result[i][1] ) ;
	}
	return 0 ;
}
