#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int n, a, b;
char s[20];

int calc(int v)
{
	int m = v, len = 0;
	while (m)
	{
		s[len++] = m % 10 + '0';
		m /= 10;
	}
	for (int i = 0, j = len - 1; i < j; i++, j--)
	{
		swap(s[i], s[j]);
	}
	int x = 0, res = 0;
	for (int i = 1; i < len; i++)
	{
		x = 0;
		for (int j = i; j < len; j++)
		{
			x = x * 10 + s[j] - '0';
		}
		for (int j = 0; j < i; j++)
		{
			x = x * 10 + s[j] - '0';
		}
		res += (x >= a && x < v);
	}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &n);
	for (int t = 0; t < n; t++)
	{
		scanf("%d%d", &a, &b);
		int ans = 0;
		for (int i = a + 1; i <= b; i++)
		{
			ans += calc(i);
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}