// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int T, N, res;
vector< int > a, b;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d", &N);
		a.clear();
		a.resize(N);
		b.clear();
		b.resize(N);
		res = 0;
		for (int i = 0; i < N; i++)
		{
			scanf("%d %d", &a[i], &b[i]);
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = i + 1; j < N; j++)
			{
				if (!(a[i] < a[j] && b[i] < b[j] || a[i] > a[j] && b[i] > b[j]))
				{
					res++;
				}
			}
		}

		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}

