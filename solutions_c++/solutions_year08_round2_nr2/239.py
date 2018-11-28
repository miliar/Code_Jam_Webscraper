#include <iostream>
#include <set>
using namespace std ;
bool b[1005] ;
int m ;
int prime[1000] ;

void init(){
	int i , j ;
	for( i = 2 ; i < 35 ; i ++ )
	{
		if( b[i] )
			continue ;
		for( j = i * i ; j <= 1000 ; j += i )
			b[j] = true ;
	}
	m = 0 ;
	for( i = 2 ; i <= 1000 ; i ++ )
		if( !b[i] )
			prime[m++] = i ;
}
int c[1005] ;
int n ;
set<int>Q ;
int Set[1005] ;

int find_set( int x )
{
	if( x != Set[x] )
		Set[x] = find_set( Set[x] ) ;
	return Set[x] ;
}
void link( int x , int y )
{
	Set[x] = y ;
}
void Union(int x, int y )
{
	link( find_set(x ) , find_set(y) ) ;
}

int main(){
	int test ;
	freopen( "B-small-attempt0.in" , "r" , stdin ) ;
	freopen("B-small-attempt0.out" , "w" , stdout ) ;
	scanf("%d" , &test ) ;
	int t = 1 ;
	init() ;
	while( test -- )
	{
		int a , b , p ;
		scanf("%d%d%d" , &a , &b , &p ) ;
		int i , j , k ;
		n = b - a + 1 ;
		for( i = a ; i <= b ; i ++ )
			Set[i] = i ;
		for( i = 0 ; i < n ; i ++ )
			c[i] = a + i ;

		/*for( i = 0 ; i < n ; i ++ )
		{
			for( j = i + 1 ; j < n ; j ++ )
				g[i][j] = gcd( c[i] , c[j] ) ;
		}*/
		Q.clear () ;
		int val ;
		bool find = false ;
		for( i = a ; i <= b ; i ++ )
		{
			for( j = i + 1 ; j <= b ; j ++ )
			{
				for( k = 0 ; k < m ; k ++ )
					if( prime[k] >= p && i % prime[k] == 0 && j % prime[k] == 0 )
					{
						Union( i , j ) ;
					}
			}
		}
		for( i = a ; i <= b ; i ++ )
			Q.insert( find_set(i) ) ;
		printf("Case #%d: %d\n" , t ++  , Q.size () ) ;
	}
	return 0 ;
}