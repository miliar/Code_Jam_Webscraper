#include <iostream>
#include <map>
#include <string>

using namespace std;

struct tt
{
	int pt;
	int st;
} a[1000];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int cases = 1, T;
	int i, j, s, p, n, ans, k;

	cin >> T;
	while( T-- )
	{
		ans = 0;
		cin >> n >> s >> p;
		for( i = 0; i < n; ++i )
		{
			cin >> a[i].pt;
			a[i].st = a[i].pt % 3;
		}

		for( i = 0; i < n; ++i )
		{
			if( a[i].pt == 0 )
			{
				if( p == 0 )
					ans++;
			}
			else if( a[i].st == 1 )
			{
				k = a[i].pt/3+1;
				if( k >= p )
					ans++;
			}
			else if( a[i].st == 0 )
			{
				if( a[i].pt/3 >= p )
					ans++;
				else if( s > 0 && a[i].pt/3 + 1 == p )
				{
					ans++;
					s--;
				}
			}
			else if( a[i].st == 2 )
			{
				if( a[i].pt/3+1 >= p )
					ans++;
				else if( s > 0 && a[i].pt/3+2 == p )
				{
					ans++;
					s--;
				}
			}
		}

		cout << "Case #" << cases++ << ": " << ans << endl;
	}

	return 0;
}