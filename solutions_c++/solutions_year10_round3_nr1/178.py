#include <iostream>
#include <algorithm>
using namespace std;

struct NODE
{
	int a, b;
	bool operator< ( const NODE &right ) const
	{
		return a < right.a;
	}
};

NODE node[ 1010 ];
int n, total;

int main()
{
	int i, j, t, test = 0;
	
	freopen( "A-large.in", "r", stdin );
	freopen( "A-out.txt", "w", stdout );
	scanf( "%d", &t );
	
	while ( t-- )
	{
		
		scanf( "%d", &n );
		
		for ( i = 1; i <= n; ++i )
			scanf( "%d %d", &node[ i ].a, &node[ i ].b );
		sort( node + 1, node + 1 + n ); 
		
		total = 0;
		for ( i = 1; i <= n; ++i )
			for ( j = i + 1; j <= n; ++j )
				if ( node[ j ].a > node[ i ].a && node[ j ].b < node[ i ].b )
					++total;
		printf( "Case #%d: %d\n", ++test, total );
	}
	return 0;
}
