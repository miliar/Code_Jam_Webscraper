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

using namespace std;

int main()
{

	freopen( "C-small-attempt0.in" , "r", stdin );
	freopen( "test.out" , "w", stdout );

	int t, r, k, n;
	int g ;
	int c = 1;
	
	cin >> t ;
	
	while( t-- )
	{
		cin >> r;
		cin >>k;
		cin >> n ;
		
		vector<int> v ;
		int total = 0 ;
		
		FOR(i, 0, n)
		{
			cin >> g;
			v.pb(g);
		}
		
		int kk ,counter = 0,ii;
		
		FOR(i, 0, r)
		{
			kk = k ;
			ii = 0;
			while( kk-v[counter] >= 0 )
			{
				kk-= v[counter];
				ii++;
				counter = (counter+1)%n ;
				if( ii == n )
					break;
			}
			total+= k-kk ;
		}
		printf( "Case #%d: %d\n", c, total );
		c++ ;
	}
	
	return 0;
}
