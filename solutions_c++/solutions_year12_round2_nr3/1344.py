#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long LL;

int t, n, a[100] = {}, Count[5000010] = {}, len[5000010] = {}, b[5000010][21], s[21] = {};
int tsum = 0;

bool func(int f, int l, int time)
{
	if (f >= n)
		return false;;
	for (int i = f; i < n; i++)
	{
		tsum += a[i];
		s[l-1] = a[i];
		if (func(i+1, l+1, time))
			return true;
		if (Count[tsum] != time)
		{
			Count[tsum] = time;
			len[tsum] = l;
			for (int j = 0; j < l; j++)
				b[tsum][j] = s[j];
		}
		else
		{
			for (int j = 0; j < len[tsum]; j++)
				printf("%d ", b[tsum][j]);
			printf("\n");
			for (int j = 0; j < l; j++)
				printf("%d ", s[j]);
			return true;
		}
		tsum -= a[i];
	}
	return false;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d:\n", i+1);
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			scanf("%d", &a[j]);
		if (!func(0, 1, i+1))
			printf("Impossible");
		printf("\n");
	}
	
	return 0;
}