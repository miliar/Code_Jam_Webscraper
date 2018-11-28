#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i, lo, hi) for(int i = (lo); i < (hi); ++i)
#define MP make_pair
#define PB push_back

typedef long long ll;

#define MOD 1000000007LL;

ll n, seq[550000];
ll memo[550000];

ll rec(int at)
{
	ll &ret = memo[at];
	if(ret != -1) return ret;
	if(at == n) return ret = 0;

	ll ans = 1;
	for(int i = at + 1; i < n; ++i)
	{
		if(seq[i] > seq[at])
		{
			ans = (ans + rec(i)) % MOD;
		}
	}

	return ret = ans;
}

int main()
{
	int numCases;
	scanf("%d", &numCases);

	FOR(tc, 1, numCases + 1)
	{
		ll m, X, Y, Z;
		scanf("%lld %lld %lld %lld %lld", &n, &m, &X, &Y, &Z);
		vector<ll> A(m);
		for(int i = 0; i < m; ++i) scanf("%lld", &A[i]);

		for(int i = 0; i < n; ++i)
		{
			seq[i] = A[i % m];
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
		}

		memset(memo, -1, sizeof(memo));

		ll ret = 0;
		for(int i = 0; i < n; ++i)
		{
			ret = (ret + rec(i)) % MOD;
		}

		printf("Case #%d: %lld\n", tc, ret);
	}

	return 0;
}
