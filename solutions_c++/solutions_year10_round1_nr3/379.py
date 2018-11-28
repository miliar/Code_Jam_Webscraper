#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back

const int N = 110;

bool solve(int a, int b)
{
	if(a < b)
		swap(a, b);
	if(a % b == 0)
	{
		return a > b;
	}
	int d = a / b;
	bool t = !solve(b, a % b);
	if(d > 1)
	{
		t = max(t, !solve(b, a % b + b));
	}
	return t;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("oup.txt", "w", stdout);

	int test;
	scanf("%d\n", &test);

	for1(itm, test)
	{
		int a1, a2, b1, b2;
		scanf("%d %d %d %d\n", &a1, &a2, &b1, &b2);

		int ans = 0;
		for(int i = a1; i <= a2; ++i)
			for(int j = b1; j <= b2; ++j)
				ans += solve(max(i, j), min(i, j));

		printf("Case #%d: %d\n", itm, ans);
	}

	return 0;
}
