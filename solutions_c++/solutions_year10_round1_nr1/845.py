#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std ;

#define MAX_ROW 60

char table[MAX_ROW][MAX_ROW] ;
int N , K ;

bool in( int x , int y ) 
{
	if ( x>=0 && x<N && y>=0 && y<N ) return 1 ;
	else return 0 ;
}

int check( char ch ) 
{
	int max , i , j , k ;
	int dx[] = { 0 , 1 , 1 , 1 , 0 , -1 , -1 , -1 } ;
	int dy[] = { -1 , -1 , 0 , 1 , 1 , 1 , 0 , -1 } ;

	max = 0 ;
	for ( i=0 ; i<N ; ++i ) 
		for ( j=0 ; j<N ; ++j ) 
			if ( table[i][j] == ch ) 
			{
				int temp ;
				int x , y ;
				for ( k=0 ; k<8 ; ++k )
				{
					x = i+dx[k] ; y = j+dy[k] ;
					temp = 1 ;
					while ( in(x,y) && table[x][y]==ch )
					{
						x += dx[k] ; y += dy[k] ;
						++temp ;
					}
					if ( temp>max ) max = temp ;
				}
			}
//	printf( "%c %d\n" , ch , max ) ;
	return max ;
}

int main()
{
	int caseT , caseNum , i , j ;

	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;

	scanf( "%d" , &caseNum ) ;
	for ( caseT=1 ; caseT<=caseNum ; ++caseT ) 
	{
		scanf( "%d%d" , &N , &K ) ;
		for ( i=0 ; i<N ; ++i ) scanf( "%s" , table[i] ) ;
		for ( i=0 ; i<N ; ++i )
		{
			for ( j=N-1 ; j>=0 ; --j ) 
			{
				if ( table[i][j] == '.' ) 
				{
					int k = j-1 ;
					while ( k>=0 && table[i][k]=='.' ) --k ;
					if ( k<0 ) goto next ;
					else swap( table[i][k] , table[i][j] ) ;
				}
			}
next:;
		}

//		printf( "%d %d\n" , N , K ) ; 
//		puts( "" ) ;
//		for ( i=0 ; i<N ; ++i ) puts( table[i] ) ;

		printf( "Case #%d: " , caseT ) ;
		int r = check( 'R' ) ;
		int b = check( 'B' ) ; 
		if ( r>=K && b>=K ) puts( "Both" ) ; 
		else if ( r>=K ) puts( "Red" ) ;
		else if ( b>=K ) puts( "Blue" ) ;
		else puts( "Neither" ) ;
	}

	return 0 ;
}