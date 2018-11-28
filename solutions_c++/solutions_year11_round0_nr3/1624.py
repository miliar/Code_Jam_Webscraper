#include <stdio.h>
#include <cassert>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-8;

void prepare()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

int CASE;

int n, c[1005], r[30];

bool solve()
{
	printf("Case #%d: ", CASE++);

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &c[i]);

	int ans = INF, sum = 0;
	for (int i = 0; i < n; i++)
	{
		ans = min(ans, c[i]);
		sum += c[i];
	}
	ans = sum - ans;

	memset(r, 0, sizeof(r));
	for (int k = 0; k < 23; k++)
	{
		for (int i = 0; i < n; i++)
		{
			r[k] += (c[i] & 1);
			c[i] >>= 1;
		}
		if (r[k] % 2 == 1)
		{
			printf("NO\n");
			return false;
		}
	}

	printf("%d\n", ans);

	return false;
}

int main()
{
	prepare();
	int tn;
	CASE = 1;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}
