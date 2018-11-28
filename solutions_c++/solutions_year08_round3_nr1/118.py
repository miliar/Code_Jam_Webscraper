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

ll f[1024];

int main()
{
	int numCases;
	scanf("%d", &numCases);

	FOR(tc, 1, numCases + 1)
	{
		int P, K, L;
		scanf("%d %d %d", &P, &K, &L);
		FOR(i, 0, L) scanf("%lld", &f[i]);
		sort(f, f + L);
		reverse(f, f + L);

		ll ans = 0;
		for(int i = 0; i < L; ++i)
		{
			ll pos = (i / K) + 1;
			ans += pos * f[i];
		}
		printf("Case #%d: %lld\n", tc, ans);
	}

	return 0;
}
