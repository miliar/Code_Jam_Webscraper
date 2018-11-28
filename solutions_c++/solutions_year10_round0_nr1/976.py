#include <iostream>
#include <cstdio>

using namespace std;

int T, n, k;
int dp[20];

int main ()
{
	freopen ( "asd.in", "r", stdin );
	freopen ( "asd.out", "w", stdout );

	scanf ( "%d", &T );

	dp[1] = 1;
	for ( int i = 2; i <= 10; i++ )
		dp[i] = dp[i - 1]*2 + 1;

	for ( int cs = 1; cs <= T; cs++ )
	{
		scanf ( "%d%d", &n, &k );
		printf ( "Case #%d: ", cs );
		if (dp[n] > k)
			printf ( "OFF\n" );
		else
		if (dp[n] == k)
			printf ( "ON\n" );
		else
		{
			k -= dp[n] + 1;
			k %= dp[n] + 1;
			if (k == dp[n])
				printf ( "ON\n" );
			else
				printf ( "OFF\n" );
		}
	}

	return 0;
}
