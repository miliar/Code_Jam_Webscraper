#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
const int maxn = 1005;

ll g[maxn],vis[maxn], money[ maxn ];
ll n , start , size , R, k, top ;

int main ()
{
	freopen ("C-large.in", "r", stdin);
	freopen ("C.out", "w", stdout);
	ll T ;

	scanf ("%lld", &T);

	for (ll cas = 1 ; cas <= T; cas++)
	{
		scanf ("%lld %lld %lld", &R, &k , &n);

		for( ll i = 0; i < n; i++)
			scanf ("%lld", &g[i] );

		ll ans = 0 ;
		ll iter = 0 ;

		memset (vis,0,sizeof vis);
		memset (money,0,sizeof money);

		top = 0;

		for( iter = 1; ; iter ++)
		{
			if( vis[top] )
			{
				start = vis[ top ];
				size = iter - start;
				--iter;
				break ;
			}
			vis[ top ] = iter;
			ll total = 0;
			money [ iter ] = money[ iter - 1 ];
			for (int j = 0 ; j < n && total + g[top] <= k ; j++ )
			{
				total += g[top];
				top = (top+1)%n;
			}
			money [ iter ] += total ;
		}
		
		if( R<=iter )
			ans = money[ R ];
		else
		{
			ans = money[ iter ];
			ans += ((R-iter)/size)*(money[iter]-money[start-1]) ;
			R -= iter; R %= size;
			ans += money[start-1+R] - money[start-1];
		}
		printf("Case #%lld: %lld\n", cas,ans);
	}

	return 0;
}
