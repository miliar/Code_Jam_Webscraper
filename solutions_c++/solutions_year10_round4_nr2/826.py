#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <algorithm>
#include <cassert>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair
typedef long long lint;
const int INF = 2000000000;

int n, p, p2;
int f[1500];

__forceinline bool intcheck(int a, int b)
{
	bool ok = true;
	for (int i = a; i < b && ok; i++)
		ok = f[i] <= 0;
	return ok;
}

__forceinline bool check()
{
	bool ok = true;
	for (int i = 0; i < p && ok; i++)
		ok = f[i] <= 0;
	return ok;
}

bool solve(int case_num)
{
	scanf("%d", &n);
	p = 1;
	for (int i = 0; i < n; i++)
		p *= 2;

	for (int i = 0; i < p; i++)
	{
		scanf("%d", &f[i]);
		f[i] = n - f[i];
	}

	int x;
	for (int i = 0; i < p - 1; i++)
		scanf("%d", &x);

	int ans = 0;
	int gg = p;
	while (gg != 1)
	{
		for (int bs = 0; bs < p; bs += gg)
		{
			if (intcheck(bs, bs + gg))
				continue;

			for (int i = bs; i < bs + gg; i++)
				f[i]--;

			ans++;
		}

		if (check())
			break;

		gg /= 2;
	}

	printf("Case #%d: ", case_num);
	//answer
	printf("%d", ans);
	//======
	printf("\n");
	return true;
}

int main()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
		solve(i + 1);
	return 0;
}