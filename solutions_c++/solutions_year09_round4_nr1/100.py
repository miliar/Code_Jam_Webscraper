#include "stdio.h"
#include <vector>
#include <set>
#include <strstream>
#include <string>
#include <algorithm>
#include <hash_map>
#include <hash_set>
#include <queue>
using namespace std;
using namespace stdext;

int doit( int a[100], int k, int n )
{
	if( k == n )
	{
		return 0;
	}

	if( a[k] <= k+1 )
	{
		return doit( a, k+1, n );
	}
	else
	{
		for( int i=k+1; i<n; ++i )
		{
			if( a[i] <= k+1 )
			{
				for( int j=i; j>k; --j )
				{
					a[j] = a[j-1];
				}
				return i-k + doit( a, k+1, n );
			}
		}
	}
}

int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );

	int tn, m, n;
	scanf( "%d", &tn );
	for( int cn = 1; cn <= tn; ++cn )
	{
		scanf( "%d", &n );
		int a[100], p[100];
		for( int i=0; i<n; ++i )
		{
			getchar();
			a[i] = 0;
			p[i] = i;
			char c;
			for( int j=0; j<n; ++j )
			{
				c = getchar();
				if( c == '1' )
				{
					a[i] = j+1;
				}
			}
		}

		int ans = doit( a, 0, n );

		printf( "Case #%d: %d\n", cn, ans );
	}
	return 0;

}