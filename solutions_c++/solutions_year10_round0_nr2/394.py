#include <iostream>
#include <cstdio>

using namespace std;
typedef long long ll;

int T, n, g;
int a[2000], b[2000];

int gcd (int a, int b)
{
	if (!a) return b;
	return gcd (b % a, a);
}

ll nok (int a, int b)
{
	return a*1ll*b/gcd (a, b);
}

int main ()
{
	freopen ( "asd.in", "r", stdin );
	freopen ( "asd.out", "w", stdout );

	scanf ( "%d", &T );

	for ( int cs = 1; cs <= T; cs++ )
	{
		scanf ( "%d", &n );
		for ( int i = 0; i < n; i++ )
			scanf ( "%d", &a[i] );
		sort (a, a + n);

		for ( int i = 0; i < n - 1; i++ )
			b[i] = a[i + 1] - a[i];
		g = b[0];
		for ( int i = 1; i < n - 1; i++ )
			g = gcd (b[i], g);

		printf ( "Case #%d: %I64d\n", cs, ((a[0] + g - 1)/g)*1ll*g - a[0] );
	}

	return 0;
}
