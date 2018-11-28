#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) forn(i, v.size())
#define pb push_back

double d[100000];
int N, C;
int cnt[1000000];

double get(int mask)
{
	if (mask == (1 << C) - 1)
		return 0.0;
	if (d[mask] != -1)
		return d[mask];

	double ans = 0;
	int count = 0, k = 0;
	forn(i, (1 << C))
	{
		if (cnt[i] != N)
			continue;

		count++;
		if ((i | mask) != mask)
		{
			ans += get(i | mask) + 1;
		}
		else
			k++;
	}
	return d[mask] = (ans + k) / (count - k);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	forn(i, (1 << 10))
	{
		cnt[i] = 0;
		forn(j, 20)
			cnt[i] += (i >> j) & 1;
	}

	int tests;
	scanf("%d\n", &tests);
	forn(test, tests)
	{
		
		scanf("%d%d", &C, &N);
		forn(i, (1 << C))
			d[i] = -1;
		printf("Case #%d: %.7lf\n", test + 1, get(0));
	}

	return 0;
}

