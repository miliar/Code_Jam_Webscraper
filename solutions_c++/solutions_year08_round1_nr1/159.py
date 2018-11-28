#include <stdio.h>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
	int casen, n, i, j;
	freopen( "d:\\temp\\out.txt", "w", stdout );
	freopen( "d:\\temp\\in.txt", "r", stdin );
	scanf( "%d", &casen );

	for( int k=1; k<=casen; ++k )
	{
		scanf( "%d", &n );
		vector<__int64> a(n),b(n);
		int num;

		for( i=0; i<n; ++i )
		{
			scanf( "%d", &num );
			a[i] = num;
		}

		for( i=0; i<n; ++i )
		{
			scanf( "%d", &num );
			b[i] = num;
		}

		sort( a.begin(), a.end() );
		sort( b.begin(), b.end(), greater<__int64>() );

		__int64 ans = 0;
		for( i=0; i<n; ++i )
		{
			ans += a[i] * b[i];
		}

		printf( "Case #%d: %I64d\n", k, ans );

	}
	return 0;

}