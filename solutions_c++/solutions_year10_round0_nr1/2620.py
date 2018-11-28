#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define	pb(n)	push_back(n)
#define	b(n)	n.begin()
#define	e(n)	n.end()

#define	FOR( i,v,s)	for( int i = ((int)v) ; i<s ; ++i )
#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define ETA 1e-7

using namespace std;

int main()
{

	freopen( "A-large.in" , "r", stdin );
	freopen( "test.out" , "w", stdout );

	int t, n, k;

	int test = 1 ;
	
	cin >> t ;

	while( t-- )
	{
		cin >> n>>k ;

		printf("Case #%d: ", test );
		if( (k&((1<<n)-1)) == ((1<<n)-1) )
			printf( "ON\n" );
		else
			printf( "OFF\n" );
		
		test++ ;
	}
	return 0;
}
