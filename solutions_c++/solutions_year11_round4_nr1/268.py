#include <cstdio>

struct node
{
	double b, e;
	int w;
}a[1001], t;

void sort ( int l, int r )
{
	int i = l, j = r, x = a[(l+r)>>1].w;
	
	while ( i <= j )
	{
		while ( a[i].w < x ) ++i;
		while ( a[j].w > x ) --j;
		
		if ( i <= j )
		{
			t = a[i]; a[i] = a[j]; a[j] = t;
			++i; --j;
		}
	}
	
	if ( l < j ) sort ( l, j );
	if ( i < r ) sort ( i, r );
}

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o );
		
		int i, l, s, r, n;
		double t, x, ans;
		
		scanf ( "%d%d%d%lf%d", &l, &s, &r, &t, &n );
		ans = l;
		for ( i = 1; i <= n; ++i )
			scanf ( "%lf%lf%d", &a[i].b, &a[i].e, &a[i].w ),
			ans -= a[i].e - a[i].b;
		
		x = ans / r;
		if ( x > t + 1e-7 )
		{
			ans = t + ( ans - t * r ) / s;
			t = 0;
		}
		else ans = x, t -= x;
		
		sort ( 1, n );
		
		for ( i = 1; i <= n; ++i )
		{
			if ( t > 1e-7 )
				x = ( a[i].e - a[i].b ) / ( a[i].w + r );
			if ( x > t + 1e-7 )
			{
				ans += t + ( a[i].e - a[i].b - t * ( a[i].w + r ) ) /
					   ( a[i].w + s );
				t = 0;
			}
			else ans += x, t -= x;
		}
		
		printf ( "%.6lf\n", ans );
	}
	return 0;
}
