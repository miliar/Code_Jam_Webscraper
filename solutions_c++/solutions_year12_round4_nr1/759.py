#include <stdio.h>
#include <string.h>

struct _vine
{
	int dist ;
	bool reach ;
} ;

struct _vine vine[10011] ;
int d[10011], l[10011] ;


int main()
{
	int t, tt ;
	int i, j, n ;
	int dest ;
	
	scanf( "%d", &tt ) ;
	for ( t = 1 ; t <= tt ; ++t )
	{
		
		scanf( "%d", &n ) ;
		for ( i = 0 ; i < n ; ++i )
		{
			scanf( "%d %d", &d[i], &l[i] ) ;
			vine[i].reach =false ;
			vine[i].dist = 1000000005 ;
		}
		scanf( "%d", &dest ) ;
		
		l[0] = d[0] ;
		
		for ( i = n - 1 ; i >= 0 ; --i )
		{
			if ( dest <= d[i] + l[i] )
			{
				vine[i].reach = true ;
				vine[i].dist = dest - d[i] ;
			}
			
			for ( j = i + 1 ; d[i] + l[i] >= d[j] && j < n ; ++j )
			{
				if ( vine[j].reach == true && d[j] - d[i] >= vine[j].dist 
					&& d[j] - d[i] < vine[i].dist )
				{
					vine[i].reach = true ;
					vine[i].dist = d[j] - d[i] ;
				}
			}
		}
		
		//for ( i = 1 ; i < n ; ++i )
		//	printf( "%d %d\n", vine[i].reach, vine[i].dist ) ;
		
		/*for ( j = 1 ; d[0] + l[0] >= d[j] && j < n ; ++j )
		{
			if ( vine[j].reach == true && d[j] - d[0] >= vine[j].dist )
			{
				//printf( "%d %d %d\n", l[0], vine[j].reach, vine[j].dist ) ;
				vine[0].reach = true ;
				break ;
			}
		}*/
		
		if ( vine[0].reach )
			printf( "Case #%d: YES\n", t ) ;
		else
			printf( "Case #%d: NO\n", t ) ;
		
	}
	return 0 ;
}
