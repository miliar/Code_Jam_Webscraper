#include <algorithm>
#include <stdio.h>

#define ll long long

using namespace std;

ll c;

inline ll meet(ll a, ll b)
{
	for (; a < b; )
	{
		a *= c;
		b = (b + c - 1) / c;
	}

	return (a + b) / 2;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int testCases, t = 1;
	for (scanf("%d", &testCases); testCases; testCases--, t++)
	{
		ll a, b;
		scanf("%lld %lld %lld", &a, &b, &c);
		
		int i;
		for (i = 0; a * c < b; i++)
			b = meet(a, b);

		printf("Case #%d: %d\n", t, i);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
