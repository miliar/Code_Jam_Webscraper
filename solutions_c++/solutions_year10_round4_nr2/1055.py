// B.cpp : Defines the entry point for the console application.
//
// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

int T, k, P;
char ch;
int M[15000];
char mas[1000][1000];
int res = 0, n = 0;

int f(int b, int e, int s)
{
	if (b >= e)
		return 0;
	int r = 0;
	bool flag = false;
	for (int i = b; i <= e; i++)
	{
		if (M[i] + s < P)
			flag = true;
	}
	if (flag)
	{
		int a = f(b, (b + e) / 2, s + 1);
		int b1 = f((b + e) / 2 + 1, e, s + 1);
		r = a + b1 + 1;
	}
	else
	{
		r = 0;
	}
	return r;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &P);
		for (int i = 0; i < (1 << P); i++)
		{
			scanf("%d", &M[i]);
		}
		for (int i = 0; i < P; i++)
		{
			for (int j = 0; j < (1 << (P - i - 1)); j++)
			{
				int x;
				scanf("%d", &x);
			}
		}
		n = 1 << P;
		res = f(0, n - 1, 0);
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}



