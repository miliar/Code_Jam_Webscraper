#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n, p, s;

inline bool check1(int n)
{
	for (int i = 0; i <= 10; ++i)
		for (int zz = -1; zz <= 1; ++zz)
		{
			int j = i + zz;
			int k = n - i - j;
			if (i <= 10 && j <= 10 && k <= 10 && i >= 0 && j >= 0 && k >= 0 && abs(i - j) <= 1 && abs(i - k) <= 1 && abs(j - k) <= 1 && max(i, max(j, k)) >= p)
				return 1;
		}
	return 0;
}

inline bool check2(int n)
{
	for (int i = 0; i <= 10; ++i)
		for (int zz = -2; zz <= 2; ++zz)
		{
			int j = i + zz;
			int k = n - i - j;
			if (i <= 10 && j <= 10 && k <= 10 && i >= 0 && j >= 0 && k >= 0 && abs(i - j) <= 2 && abs(i - k) <= 2 && abs(j - k) <= 2 && max(i, max(j, k)) >= p)
				return 1;
		}
	return 0;
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		scanf("%d%d%d", &n, &s, &p);
		int ans = 0;
		int k = 0;
		for (int i = 0; i < n; ++i)
		{
			int v;
			scanf("%d", &v);
			if (check1(v))
				++ans;
			else
			if (check2(v))
				++k;
		}
		printf("Case #%d: %d\n", t + 1, ans + min(s, k));
	}
	return 0;
}
