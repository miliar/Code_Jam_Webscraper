#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<queue>
#include<math.h>
#include<algorithm>
#define MAXSIZE 500
using namespace std ;
int main( )
{
	//freopen( "C-small-attempt0 (1).in" , "r" , stdin ) ;
	FILE *in = fopen( "test.in" , "r" ) ;
	FILE *out = fopen( "output.txt" , "w" ) ;
	//freopen( "output3.txt" , "w" , stdout ) ;
	int T , t , sum , m , n  , i , j ,red ;
	int number , ans , total ;
	int vis[MAXSIZE][MAXSIZE] ;
	
	fscanf( in , "%d" , &t ) ;
	T = t ;
	while( t-- )
	{
		char map[MAXSIZE][MAXSIZE] ;
		memset( vis, 0 , sizeof(vis ) ) ;
		
		ans = 0 ;
		fscanf( in , "%d %d" , &n , &m ) ;
		for( i = 0 ; i < n ; i++ )
		{
			fscanf( in , "%s" , &map[i] ) ;	
		}
		red = total = 0 ;
		for( i = 0 ; i < n ; i++ )
		{
			for( j = 0 ; j < m ; j++ )
			{
				if( map[i][j] == '#' )
				{	
					vis[i][j] = 1 ;
					total++ ;
				}
				else
					vis[i][j] = 0 ;
			}
		}	
		for( i = 0 ; i < n-1 ; i++ )
		{
			for( j = 0 ; j < m-1 ; j++ )
			{
				if( map[i][j] == '#' && map[i][j+1] == '#' && map[i+1][j] == '#' && map[i+1][j+1] == '#' 
				 && vis[i][j] == 1 && vis[i][j+1] == 1 && vis[i+1][j] == 1 && vis[i+1][j+1] == 1 )
				{
					red++ ;
					vis[i][j] = 2 ;
					vis[i][j+1] = 3 ;
					vis[i+1][j] = 3 ;
					vis[i+1][j+1] = 2 ;
				}
			}
		}	
	
		printf( "%d\n" , red);	
		if( total %4 == 0 & red * 4 == total )
		{
			fprintf( out , "Case #%d:\n" , T - t ) ;
			for( i = 0 ; i < n ; i++ )
			{
				for( j = 0 ; j < m ; j++ )
				{
					if( map[i][j] == '#' && vis[i][j] == 2 )
						fprintf( out , "/");
					else if( map[i][j] == '#' && vis[i][j] == 3 )
						fprintf( out , "\\");
					else
					fprintf( out , ".") ;
				}
				fprintf( out , "\n" ) ;
			}
			
		}
		else
			fprintf( out , "Case #%d:\nImpossible\n" , T - t ) ;
	}
	system("pause");
	return 0 ;
}
