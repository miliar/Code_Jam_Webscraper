#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int n, a[1002], b[1002], c[1002];
bool f[1002];

int main ( )
{
	freopen ( "i.in", "r", stdin );
	freopen ( "o.out", "w", stdout );
	
	int T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o );
		
		int i;
		scanf ( "%d", &n );
		if ( n == 0 )
		{
			printf ( "0\n" );
			continue;
		}
		for ( i = 1; i <= n; ++i )
			scanf ( "%d", &a[i] );
		sort ( a + 1, a + n + 1 );
		a[0] = a[1]-1; a[n+1] = a[n]+2;
		for ( i = 1; i <= n; ++i )
			if ( a[i] == a[i-1] )
				b[i] = b[i-1];
			else b[i] = b[i-1] + 1;
		for ( i = 1; i <= n; ++i )
			++c[b[i]];
		
		for ( i = 1; i <= n; ++i )
			f[i] = true;
		
		int j, ans = n, l = 0, tt;
		for ( i = 1; i <= n; ++i ) if ( f[i] )
		{
			if ( l == 0 || a[i] == tt+1 )
				++l, tt = a[i], --c[b[i]];
			else
			{
				if ( a[i] != tt )
				{
					ans <?= l; l = 1; tt = a[i]; --c[b[i]];
					continue;
				}
				int t = a[i], tl = l, ttt = i;
				for ( j = i + 1; j <= n; ++j )
					if ( a[j] == t || !f[j] )
						continue;
					else if ( a[j] == t + 1 && c[b[j]] > c[b[ttt]] )
						++tl, t = a[j], ttt = j, f[j]= false,--c[b[j]];
					else break;
				ans <?= tl; l = 0; --i;
			}
		}
		ans <?= l;
		printf ( "%d\n", ans );
	}
	return 0;
}
