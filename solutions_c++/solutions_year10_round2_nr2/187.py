#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <limits.h>
#include <string>

using namespace std;

typedef long long int64;

int x[1000], v[1000];

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int test = 0; test < t; test++)
	{
		int n, k, b, c;
		cin >> n >> k >> b >> c;
		for (int i = 0; i < n; i++)
		{
			cin >> x[i];
		}
		for (int i = 0; i < n; i++)
		{
			cin >> v[i];
		}
		int bad = 0;
		int ans = 0;
		int q = 0;
		for (int i = n - 1; i >= 0; i--)
		{
			if (x[i] + c * v[i] < b)
				++bad;
			else
			{
				ans += bad;
				++q;
			}
			if (q >= k)
				break;
		}
		if (q >= k)
			printf("Case #%d: %d\n", test + 1, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", test + 1);
	}
	return 0;
}