#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long LL;

#define sz(c) ((int) (c).size ())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int N;
LL a[1005];

LL gcd (LL a, LL b)
{
	return a == 0 ? b : gcd (b % a, a);
}

int main ()
{
	int tests;
	scanf ("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		printf ("Case #%d: ", test);
		scanf ("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf ("%lld", &a[i]);
		LL T = 0;
		for (int i = 0; i < N; i++)
			for (int j = i + 1; j < N; j++)
				T = gcd (T, (LL) abs (a[j] - a[i]));				
		if (T == 1)
			puts ("0");
		else
		{
			for (int i = 1; i < N; i++)
				assert (a[i] % T == a[i - 1] % T);
			printf ("%lld\n", (T - (a[0] % T)) % T);
		}
	}
	return 0;
}

