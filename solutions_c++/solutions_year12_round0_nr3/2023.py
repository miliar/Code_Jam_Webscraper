#include <iostream>
#include <map>
#include <string>

using namespace std;

int dig[2000100];

bool vis[2000100];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T, cases = 1;
	int i, j, k, n, ans, t;
	int a, b, e;

	for( i = 0; i <= 9; ++i )
		dig[i] = 1;
	for( i = 10; i <= 2000000; ++i )
		dig[i] = dig[i/10]*10;

	memset(vis, 0, sizeof(vis));

	scanf("%d", &T);
	while( T-- )
	{
		ans = 0;
		scanf("%d %d", &a, &b);
		
		for( i = a; i <= b; ++i )
		{
			e = dig[i];

			for( j = 10; j <= e; j *= 10 )
			{
				t = i/j + (i%j) * (e/j*10);
				if( t > i && t <= b && !vis[t] )
				{
					ans++;
					vis[t] = 1;
				}
			}

			for( j = 10; j <= e; j *= 10 )
			{
				t = i/j + (i%j) * (e/j*10);
				if( t <= b )
					vis[t] = 0;
			}
		}

		printf("Case #%d: %d\n", cases++, ans);
	}

	return 0;
}