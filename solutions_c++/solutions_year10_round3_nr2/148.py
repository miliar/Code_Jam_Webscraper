// B.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int T, N, res, L, P, C;
vector< int > a, b;

int f(int l, int p)
{
	long long r = 0, l1 = l, p1 = p;
	if (l1 * (long long)C >= p1)
		return 0;
	while (l1 < p1)
	{
		l1 *= C;
		if (p1 % C)
		{
			p1 /= C;
			p1++;
		}
		else
		{
			p1 /= C;
		}
	}
	r = max(f(l, l1), f(p1, p)) + 1;
	return r;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d %d %d", &L, &P, &C);
		res = f(L, P);
		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}

