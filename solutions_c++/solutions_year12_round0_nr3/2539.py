#include <iostream>
#include <vector>
using namespace std ;
vector <int> a[ 2000001 ] ;
inline bool ck( int A , int B )
{
	for ( int i = 0 ; i < a[ A ] . size() ; i ++ )
	{
		if ( a[ A ][ i ] == B )
		{
			return false ;
		}
	}
	return true ;
}
int main ()
{
	for ( long long i = 1 , j , k , l ; i < 2000001 ; i ++ )
	{
		l = 1 ;
		while ( l < i ) l *= 10 ;
		j = 1 ;
		for (  ; j < i ; j *= 10 )
		{
			k = ( i % j ) * ( l / j ) + i / j ;
			if ( k < i && ck( i , k ) )
			{
				a[ i ] . push_back( k ) ;
			}
		}
	}
	int n = 0 , Case = 1 ;
	cin >> n ;
	while ( n -- )
	{
		int A , B ;
		long long ans = 0 ;
		cin >> A >> B ;
		for ( int i = A ; i <= B ; i ++ )
		{
			for ( int j = 0 ; j < a[ i ] . size() ; j ++ )
			{
				if ( A <= a[ i ][ j ] && a[ i ][ j ] <= B )
				{
					ans ++ ;
				}
			}
		}
		printf( "Case #%d: %lld\n" , Case ++ , ans ) ;
	}
}
