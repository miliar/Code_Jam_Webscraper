#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1000*1000+100;

typedef long long ll;
ll d[MAXN];

int main()
{
	int TC;
	cin >> TC;
	for(int T=1; T<=TC; T++)
	{
		ll l, t, n, c;
		cin >> l >> t >> n >> c;
		for(int i=0; i<c; i++)
		{
			ll a;
			cin >> a;
			for(int k=0; c*k+i<n; k++)
				d[k*c+i] = a;
		}

		ll ans = 0;
		for(int i=0; i<n; i++)
			if(ans + 2*d[i] >= t)
			{
				ll r = t - ans;
				d[i] -= r / 2;
				ans += r;
				break;
			}
			else
			{
				ans += d[i] * 2;
				d[i] = 0;
			}

		sort(d, d+n, greater<ll>());
		for(int i=0; i<n; i++)
			if(i < l)
				ans += d[i];
			else
				ans += d[i]*2;

		cout << "Case #" << T << ": " << ans << endl;
	}
	return 0;
}

