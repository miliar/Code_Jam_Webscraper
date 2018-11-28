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

int main()
{
	int numCases;
	scanf("%d", &numCases);

	FOR(tc, 1, numCases + 1)
	{
		int n;
		ll A, B, C, D, x0, y0, M;
		scanf("%d %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
		ll X = x0, Y = y0;
		ll x[128], y[128];
		for(int i = 0; i < n; ++i)
		{
			x[i] = X; y[i] = Y;
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}

		ll ans = 0;
		FOR(i, 0, n) FOR(j, i + 1, n) FOR(k, j + 1, n)
		{
			ll sumx = x[i] + x[j] + x[k];
			ll sumy = y[i] + y[j] + y[k];
			if((sumx % 3 == 0) && (sumy %3 == 0))
				++ans;
		}

		printf("Case #%d: %lld\n", tc, ans);
	}

	return 0;
}
