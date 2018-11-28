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

int n, dig[64], sym[64];

ll ans;

bool isUgly(ll num)
{
	return (num % 2 == 0) || (num % 3 == 0) || (num % 5 == 0) || (num % 7 == 0);
}

void calc()
{
	ll cur = dig[0], ret = 0;
	int prev = 1;

	sym[n - 1] = 3;
	FOR(i, 0, n)
	{
		if(sym[i] == 0)
		{
			cur = cur * 10 + (ll)dig[i + 1];
		}
		else // (sym[i] != 0)
		{
			if(prev == 1) ret += cur;
			else ret -= cur;
			cur = dig[i + 1];
			prev = sym[i];
		}
	}

	if(isUgly(ret)) ++ans;
}

void rec(int index)
{
	if(index == n - 1)
	{
		calc();
		return;
	}

	FOR(i, 0, 3)
	{
		sym[index] = i;
		rec(index + 1);
	}
}

int main()
{
	int numCases;
	scanf("%d", &numCases);

	FOR(tc, 1, numCases + 1)
	{
		char str[64];
		scanf("%s", str);
		n = strlen(str);
		FOR(i, 0, n) dig[i] = str[i] - '0';
		
		ans = 0;
		rec(0);
		printf("Case #%d: %lld\n", tc, ans);
	}

	return 0;
}
