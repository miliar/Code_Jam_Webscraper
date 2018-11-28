#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std ;


double wp[ 200 ] , Owp[ 200 ] , Oowp[ 200 ] , Rpi[ 200 ] ;
int Win[ 200 ] , Tot[ 200 ] ;

int main()
{
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;
	int T ;
	scanf( "%d" , &T ) ;
	for ( int t = 0 ; t < T ; t ++ )
	{
		int n ;
		scanf( "%d" , &n ) ;
		char a[ 110 ][ 110 ] ;
		gets( a[ 0 ] ) ;
		for ( int i = 0 ; i < n ; i ++ )
			gets( a[ i ] ) ;
		//WP
		for ( int i = 0 ; i < n ; i ++ )
		{
			int tot = 0 ;
			int win = 0 ;
			for ( int j = 0 ; j < n ; j ++ )
				if ( a[ i ][ j ] != '.' )
				{
					tot ++ ;
					if ( a[ i ][ j ] == '1' )	win ++ ;
				}
			Tot[ i ] = tot ;
			Win[ i ] = win ;
			wp[ i ] = win / ( 1.0 * tot ) ;
		}
		//OWP
		for ( int i = 0 ; i < n ; i ++ )
		{
			double owp = 0 ;
			int opp = 0 ;
			for ( int j = 0 ; j < n ; j ++ )
				if ( j != i && a[ j ][ i ] != '.' ) 
				{
					opp ++ ;
					int x = Win[ j ] , y = Tot[ j ] ;
					if ( a[ j ][ i ] != '.' )
					{
						y -- ;
						if ( a[ j ][ i ] == '1' )	x -- ;
					}
					owp += x * 1.0 / y ;
				}
			Owp[ i ] = owp / opp ;
		}
		//oowp
		for ( int i = 0 ; i < n ; i ++ )
		{
			double oowp = 0 ;
			int opp = 0 ;
			for ( int j = 0 ; j < n ; j ++ )
				if ( j != i && a[ j ][ i ] != '.' )
				{
					oowp += Owp[ j ] ;
					opp ++ ;
				}
			oowp /= opp ;
			Oowp[ i ] = oowp ;
		}
		printf( "Case #%d:\n" , t + 1 ) ;
		//RPI
		for ( int i = 0 ; i < n ; i ++ )
		{
			Rpi[ i ] = 0.25 * wp[ i ] + 0.5 * Owp[ i ] + 0.25 * Oowp[ i ] ;
			printf( "%.9lf\n" , Rpi[ i ] ) ;
		}
/*		printf( "wp\n" ) ;
		for ( int i = 0 ; i < n ; i ++ )
			printf( "%lf\n" , wp[ i ] ) ;
		printf( "owp\n" ) ;
		for ( int i = 0 ; i < n ; i ++ )
			printf( "%lf\n" , Owp[ i ]  ) ;
		printf( "oowp\n" ) ;
		for ( int i = 0 ; i < n ; i ++ )
			printf( "%lf\n" , Oowp[ i ] ) ;
*/
	}
	return 0 ;
}







