#include <stdio.h>
#include <string.h>
#include <assert.h>

#define MAX_HEIGHT    110
#define MAX_WIDE    110
#define MAX_QUEUE    MAX_HEIGHT*MAX_WIDE
#define INF      0x7f7f7f7f

struct POINT
{
	int x , y ;
} ;

int maps[MAX_HEIGHT][MAX_WIDE] ;
char basin[MAX_HEIGHT][MAX_WIDE] ;
POINT Queue[MAX_QUEUE] ;
int dx[] = { -1 , 0 , 0 , 1 } ;
int dy[] = { 0 , -1 , 1 , 0 } ;

int main () 
{
	int t , h , w , i , j , k , cnt ;
	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "B-large.out" , "w" , stdout ) ;
	scanf( "%d" , &t ) ;
	for ( cnt=1 ; cnt<=t ; ++cnt ) 
	{
		scanf( "%d%d" , &h , &w ) ;
		for ( i=0 ; i<h ; ++i )
			for ( j=0 ; j<w ; ++j) 
				scanf( "%d" , &maps[i][j] ) ;
		char letter = 'a' , dest ; 
		int Qhead , Qtail ;
		POINT now , temp ;
		memset( basin , '-' , sizeof(basin) ) ;
		for ( i=0 ; i<h ; ++i ) 
			for ( j=0 ; j<w ; ++j )
			{
				if ( basin[i][j] != '-' ) continue ;
				dest = '-' ;
				Qhead = Qtail = 0 ;
				temp.x = i ; temp.y = j ;
				Queue[Qtail++] = temp ;  
				while ( Qtail>Qhead ) 
				{
					now = Queue[Qhead++] ;
					int min_al = INF , dir = -1 ; 
					for ( k=0 ; k<4 ; ++k ) 
					{
						temp.x = now.x+dx[k] ;
						temp.y = now.y+dy[k] ;
						if ( temp.x<0 || temp.x>=h || temp.y<0 || temp.y>=w ) continue ;
						if ( maps[temp.x][temp.y]<min_al ) 
						{
							min_al = maps[temp.x][temp.y] ;
							dir = k ;
						}
					}

					if ( min_al >= maps[now.x][now.y] ) 
					{
						if ( basin[now.x][now.y] == '-' ) dest = letter++ ;
						else dest = basin[i][j] ;
						break ;
					}
					temp.x = now.x+dx[dir] ;
					temp.y = now.y+dy[dir] ;
					if ( basin[temp.x][temp.y] != '-' ) 
					{
						dest = basin[temp.x][temp.y] ;
						break ;
					}
					Queue[Qtail++] = temp ;  
				}
next_step:
				assert( dest>='a' && dest<='z' ) ;
				for ( k=0 ; k<Qtail ; ++k )
					basin[Queue[k].x][Queue[k].y] = dest ;
			}
			printf( "Case #%d:\n" , cnt ) ;
			for ( i=0 ; i<h ; ++i ) 
			{
				for ( j=0 ; j<w ; ++j ) 
					printf( "%c " , basin[i][j] ) ;
				puts( "" ) ;
			}
	}
	return 0 ;
}
