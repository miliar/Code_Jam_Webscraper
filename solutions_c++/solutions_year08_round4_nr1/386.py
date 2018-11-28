#include<iostream>

using namespace std ;
struct node
{
	int state ;
	int val ;
};
node a[10005] ;
int m;
int dp[10005][2] ;
int Max = 10006 ;

void dfs( int f )
{
	bool leaf = false ;
	int i ;	
	if( 2*f + 1 <= m )
	{
		leaf = true ;
		dfs( 2*f ) ;
		dfs( 2*f + 1 ) ;
		if( a[f].val == 1 )
		{
			dp[f][0] = min( dp[2*f][0] + dp[2*f+1][1] , min( dp[2*f][1] + dp[2*f+1][0] , dp[2*f][0] + dp[2*f+1][0] )) ;
			dp[f][1] = dp[2*f][1] + dp[2*f+1][1] ;
			if( a[f].state == 1 )
				dp[f][1] = min( dp[f][1] , min( dp[2*f][1] + dp[2*f+1][0] + 1 , dp[2*f][0] + dp[2*f+1][1] + 1 )) ;
		}
		else
		{
			dp[f][1] = min( dp[2*f][0] + dp[2*f+1][1] , min( dp[2*f][1] + dp[2*f+1][0] , dp[2*f][1] + dp[2*f+1][1] )) ;
			dp[f][0] = dp[2*f][0] + dp[2*f+1][0] ;
			if( a[f].state == 1)
				dp[f][0] = min( dp[f][0] , min( dp[2*f][1] + dp[2*f+1][0] + 1 , dp[2*f][0] + dp[2*f+1][1] + 1 ))  ;
		}
	}
	if( !leaf )
	{
		if( a[f].val == 0 )
		{
			dp[f][0] = 0 ;
			dp[f][1] = Max ;
		}
		else
		{
			dp[f][0] = Max ;
			dp[f][1] = 0 ;
		}
		return ;
	}
}
int main(){
	freopen("A-large(1).in","r",stdin);
	freopen("A-large(1).out","w",stdout);
	int test ;
	cin >> test ;
	int t = 1 ;
	while( test -- )
	{
		
		cin >> m ;
		int root  ;
		cin >> root ;
		int i ;
		for( i = 1 ; i <= ( m -1 ) / 2 ; i ++ )
		{
			cin >> a[i].val >> a[i].state ;
		}

		for( i = ( m - 1 ) / 2 + 1 ; i <= m ; i ++ )
		{
			cin >> a[i].val ;
			a[i].state = -1 ;
		}

		for( i = 0  ; i <= m ; i ++ )
			dp[i][0] = dp[i][1] = Max ;
		dfs( 1 ) ;
		printf("Case #%d: " , t ++ ) ;
		if( dp[1][root] >= Max )
			printf("IMPOSSIBLE\n") ;
		else
			printf("%d\n" , dp[1][root] ) ;
	}
	return  0;
}