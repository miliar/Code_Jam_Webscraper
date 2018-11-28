#include <algorithm>
#include <stdio.h>
#include <vector>

#define MAX 1000010
#define ll long long
#define pb push_back

using namespace std;

int testCases;
ll l, t, n, c;
ll cost[MAX];

int main()
{
	freopen("b-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);

	int te = 0;
	for (scanf("%d", &testCases); testCases; testCases--)
	{
		te++;
		printf("Case #%d: ", te);
		scanf("%lld %lld %lld %lld", &l, &t, &n, &c);

		for (int i = 1; i <= c; i++)
			scanf("%lld", &cost[i]);
		cost[0] = cost[c];

		ll tt = 0;
		for (int i = 1; i <= n; tt += 2 * cost[i], i++)
			cost[i] = cost[i % c];

		vector <ll> vctNr;
		ll ta = 0;
		for (int i = 1; i <= n; i++)
		{
			if (ta + 2 * cost[i] <= t)
				ta += 2 * cost[i];
			else
			{
				vctNr.pb((ta + 2 * cost[i] - t) / 2);

				for (int j = i + 1; j <= n; j++)
					vctNr.pb(cost[j]);
				break;
			}
		}

		sort(vctNr.begin(), vctNr.end());
		reverse(vctNr.begin(), vctNr.end());

		l = min(l, (ll) vctNr.size());
		for (int i = 0; i < l; i++)
			tt -= vctNr[i];

		printf("%lld\n", tt);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
