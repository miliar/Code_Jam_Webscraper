#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int n;
ll d;
ll c[210];
ll ile[210];
ll mn[210];

bool ok(ll t)
{
	ll start = -1000000000000000000LL;
	for(int i=0; i<n; ++i)
	{
		ll minst = max(start + d, c[i] - t);
		ll koniec = minst + mn[i];
		if(koniec > c[i] + t) return false;
		start = koniec;
	}
	
	return true;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int icas=1; icas<=cases; ++icas)
	{
		scanf("%d%lld", &n, &d);
		d *= 2;
		ll left = -1, right = 10000000000000000LL;
		for(int i=0; i<n; ++i)
		{
			scanf("%lld%lld", &c[i], &ile[i]);
			c[i] *= 2;
			mn[i] = (ile[i]-1) * d;
			left = max(left, mn[i]/2 - 1);
		}
		
		while(left+1 < right)
		{
			ll mid = (left + right)/2;
			if(ok(mid)) right = mid;
			else left = mid;
		}
		
		printf("Case #%d: %.3lf\n", icas, (double)right / 2);
	}
	return 0;
}
