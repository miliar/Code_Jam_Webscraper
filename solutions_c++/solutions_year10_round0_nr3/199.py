#include <stdio.h>
#include <cstring>
#define maxl 2010
#define ll long long

ll c[maxl], a[maxl], top, vis[maxl];
ll n, r, k;

ll calc(ll& p)
{
	ll sum = a[p], cnt = 1;
	p = (p + 1) % n;
	while(sum + a[p] <= k && cnt < n)
	{
		sum += a[p];
		p = (p + 1) % n;
		cnt++;
	}
	return sum;
}

ll solve()
{
	ll i;
	memset(vis, -1, sizeof vis);

	ll p = 0, flag = 1;

	top = 0;
	for(ll i=1; ;++i)
	{
		if(vis[p] != -1){ flag = 0; break; }
		vis[p] = top;
		//prllf("%lld ", p);
		c[top++] = calc(p);
		//prllf("%lld\n", c[top-1]);
	}

	//for(ll i=0; i<top; ++i) prllf("%lld ", c[i]);
	//puts("");

	ll st = vis[p], en = top - 1;

	ll sum = 0, ans = 0;
	for(ll i=st; i<=en; ++i) sum += c[i];

	if(r <= en + 1)
	{
		for(ll i=0; i<r; ++i) ans += c[i];
		return ans;
	}
	else
	{
		for(ll i=0; i<st; ++i) ans += c[i];
		r -= st;

		ll times = r / (en - st + 1), un = 0;
		for(ll i=st; i<=en; ++i) un += c[i];

		ans += times * un;

		for(ll i=0; i<r % (en - st + 1); ++i)
		{
			ans += c[st + i];
		}
		return ans;
	}

}

int main()
{
	ll t, tc = 0;
	scanf("%lld", &t);
	while(t--)
	{
		scanf("%lld%lld%lld", &r, &k, &n);
		for(ll i=0; i<n; ++i) scanf("%lld", &a[i]);

		printf("Case #%lld: %lld\n", ++tc, solve());
	}
	return 0;
}

