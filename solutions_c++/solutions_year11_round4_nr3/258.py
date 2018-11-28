#include <iostream>

using namespace std;

long long a[1000001];

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int T;
	
	int k;
	a[k = 1] = 2;
	for ( int i = 3; i <= 1000000; i += 2 )
	{
		int j;
		for ( j = 1; j <= k && a[j] * a[j] <= i; ++j )
			if ( i % a[j] == 0 )
				break;
		if ( j > k ||a[j] * a[j] > i ) a[++k] = i;
	}
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o );
		
		long long x;
		cin >> x;
		
		if ( x == 1 )
		{
			printf ( "0\n" );
			continue;
		}
		
		int i;
		for ( i = 1; i <= k; ++i )
			if ( a[i] > x )
				break;
		
		long long ans = 1;
		for ( int j = 1; j < i; ++j )
		{
			long long y = a[j];
			while ( y * a[j] <= x )
				++ans, y *= a[j];
		}
		
		cout << ans << endl;
	}
	return 0;
}
