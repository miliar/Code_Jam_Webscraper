#include <limits.h>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAX_N		9

int p[MAX_N], a[MAX_N];

int main ( )
{
	freopen ( "input", "r", stdin );
	freopen ( "output", "w", stdout );
	
	p[0] = 1;
	for ( int i = 1; i < MAX_N; ++i )
		p[i] = p[i-1] * 10;
	
	int ntests;
	scanf ( "%d", &ntests );
	
	for ( int t = 1; t <= ntests; ++t )
	{
		int lo, hi;
		scanf ( "%d%d", &lo, &hi );
		
		bool flag;
		int x, y, i, k;
		int ans = 0;
		
		int tmp = lo, n = 0;
		while ( tmp >= 10 )
			n++, tmp /= 10;
		
		for ( x = lo; x <= hi; ++x )
		{
			for ( i = 1; i <= n; ++i )
			{
				y = (x/p[i])+((x%p[i])*p[n-i+1]);
				flag = true;
				for ( k = 0; k < i; ++k )
					if ( a[k] == y )
						flag = false;
				a[i] = y;
				if ( flag && y > x && y <= hi )
					ans++;
			}
		}
		
		printf ( "Case #%d: %d\n", t, ans );
	}
	
	return 0;
}
