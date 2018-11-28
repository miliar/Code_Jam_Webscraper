// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int t;
	scanf("%d", &t);

	for (int k = 0; k < t; k++)
	{
		int n;
		scanf("%d", &n);
		vector<pair<int, int>> values;
		for (int i = 0; i < n; i++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			values.push_back(make_pair(a, b));
		}
		sort(values.begin(), values.end());

		int count = 0;
		for (int i = 0; i < n; i++)
		{
			int v = values[i].second;
			for (int j = 0; j < i; j++)
				if (values[j].second > v)
					count++;
		}

		printf("Case #%d: %d\n", k + 1, count);
	}

	return 0;
}