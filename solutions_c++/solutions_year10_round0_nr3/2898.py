#include <algorithm>
#include <stdio.h>

#define ll long long
#define MAX 1024

using namespace std;

ll bani[MAX], el[MAX], pn[MAX];

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	ll testCases, t = 0;
	for (scanf("%lld", &testCases); testCases; testCases--)
	{
		t++;
		ll r, k, n;
		scanf("%lld %lld %lld", &r, &k, &n);

		ll sum = 0;
		for (ll i = 0; i < n; i++)
		{
			scanf("%lld", &el[i]);
			el[i + n] = el[i]; 

			sum += el[i];
		}
		el[n + n] = 1;

		k = min(k, sum);

		for (ll i = 0; i < n; i++)
		{
			ll j = i, act = 0;
			for (j = i; act + el[j] <= k; j++)
				act += el[j];

			bani[i] = act; 
			pn[i] = j % n;
		}

		ll ac = 0, tot = 0;
		for (ll i = 0; i < r; i++)
		{
			tot += bani[ac];
			ac = pn[ac];
		}

		printf("Case #%lld: %lld\n", t, tot);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
