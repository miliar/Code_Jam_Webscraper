// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <algorithm>

using namespace std;

int t, n;
int v[10000];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);

	for (int k = 0; k < t; k++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &v[i]);
		sort(v, v + n);
		int c = 0;
		int total = 0;
		for (int i = 0; i < n; i++)
		{
			c ^= v[i];
			if (i != 0) total += v[i];
		}
		if (c != 0)
		{
			printf("Case #%d: NO\n", k + 1);
		}
		else
		{
			printf("Case #%d: %d\n", k + 1, total);
		}
	}

	return 0;
}