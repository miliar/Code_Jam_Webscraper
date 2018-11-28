#include <iostream>
#include <cstdio>

using namespace std;
typedef long long ll;

int T, n, k, col, R;
ll dp[2000];
int w[2000], h[2000];
int a[2000];

ll get (int R, int u)
{
	if (!R) return 0;

	if (w[u])
	{
		ll path = dp[u];
		int next = w[u];

		for ( int i = h[u]; i != u; i = h[i] ) path += dp[i];

		memset (w, 0, sizeof (w));
		memset (dp, 0, sizeof (dp));
		memset (h, 0, sizeof (h));

		return path*1ll*(R / (col - next + 1)) + get (R % (col - next + 1), u);
	}

	ll cnt = 0;
	int tmp = u;

	w[u] = ++col;

	for ( int j = 0; cnt + a[u] <= k && j < n; cnt += a[u], u = (u + 1) % n, j++ );

	dp[tmp] = cnt;
	h[u] = tmp;

	return cnt + get (R - 1, u);
}

int main ()
{
	freopen ( "asd.in", "r", stdin );
	freopen ( "asd.out", "w", stdout );

	scanf ( "%d", &T );

	for ( int cs = 1; cs <= T; cs++ )
	{
		memset (w, 0, sizeof (w));
		memset (h, 0, sizeof (h));
		memset (dp, 0, sizeof (dp));

		scanf ( "%d%d%d", &R, &k, &n );
		for ( int i = 0; i < n; i++ )
			scanf ( "%d", &a[i] );

		col = 0;
		printf ( "Case #%d: %I64d\n", cs, get (R, 0) );
	}

	return 0;
}
