#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 1 << 10;

int a[nmax];
bool b[nmax];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("D.in", "rt", stdin);
	freopen("D.out", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
			--a[i];
		}
		memset(b, 0, sizeof(b));
		double ans = 0.0;
		for(int i = 0; i < n; ++i)
		{
			if (!b[i])
			{
				int x = a[i];
				b[x] = true;
				int k = 1;
				while(x != i)
				{
					x = a[x];
					b[x] = true;
					++k;
				}
				if (k > 1)
				{
					ans += k;
				}
			}
		}
		printf("Case #%d: %.6lf\n", tt + 1, ans);
	}
	return 0;
}