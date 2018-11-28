#include <stdio.h>
#include <string.h>
const int dir[4][2] = { { -1 , -1 } , { -1 , 1} , { 0 , 1 } , {0, -1} } ;
char g[22][22] , used[12][12] ;
int ans , r , c ;

void dfs ( int x , int y , int now )
{
	int k , tx , ty ;
	if ( now > ans ) ans = now ;
	if ( now + (c-y+1)/2 + (r-x-1)*(c+1)/2 <= ans ) return ;
	if ( x == r ) return ;
	if ( y == c ) { dfs ( x + 1 , 0 , now ) ; return ; }
	if ( g[x][y] == 'x' ) 
	{
		dfs ( x , y + 1 , now ) ; return ;
	}		
	for ( k = 0 ; k < 4 ; k ++ )
	{
		tx = x + dir[k][0] , ty = y + dir[k][1] ;
		if ( tx >= 0 && tx < r && ty >= 0 && ty < c && used[tx][ty] ) break ;
	}
	if ( k == 4 )
	{
		used[x][y] = 1 ;
		dfs ( x , y + 1 , now + 1 ) ;
		used[x][y] = 0 ;
	}
	dfs ( x , y + 1 , now ) ;
}

int main()
{
	freopen ( "C-small-attempt1.in" , "r" , stdin ) ;
	freopen ( "C-small-attempt1.out" , "w" , stdout ) ;
	int tn , prob = 0 , i ;	
	for ( scanf ( "%d" , &tn ) ; tn -- ; )
	{
		memset ( used , 0 , sizeof(used) ) ;
		scanf ( "%d%d" , &r , &c ) ;
		for ( i = 0 ; i < r ; i ++ ) scanf ( "%s" , g[i] ) ;
		ans = 0 ;
		dfs ( 0 , 0 , 0 ) ;
		printf ( "Case #%d: %d\n" , ++prob , ans ) ;
	}
	return 0 ;
}