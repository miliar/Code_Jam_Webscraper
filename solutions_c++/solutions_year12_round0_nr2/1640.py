#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int cas;
	int x;
	scanf( "%d", &cas );
	for ( int i = 1; i <= cas; i++ )
	{
		int ans = 0;
		int n,s,p;
		scanf( "%d%d%d", &n, &s, &p );
		for ( int j = 1; j <= n; j++ )
		{
			scanf( "%d", &x );
			if ( x % 3 == 0 )
			{
				if ( x / 3 >= p ) ans++;
				else 
				if ( s != 0 )
				{
					if ( x / 3 >= p-1 && x > 0 ) 
					{
						s--;
						ans++;
					}
				}
			}
			else if ( x % 3 == 1 )
			{
				if ( x / 3 >= p - 1 ) ans++;
			}
			else if ( x % 3 == 2 )
			{
				if ( x / 3 >= p - 1) ans++;
				else 
				if ( s != 0 )
				{
					if ( x / 3 >= p - 2 ) 
					{
						s--;
						ans++;
					}
				}
			
			}
		}
		if ( s >= 0 )
		printf( "Case #%d: %d\n", i, ans );
		else
		printf( "Case #%d: %d\n", i, ans+s );
	}
	return 0;
}