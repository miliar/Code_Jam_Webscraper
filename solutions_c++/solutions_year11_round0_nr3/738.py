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

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		int n;
		int s = 0;
		int sum = 0;
		scanf("%d", &n);
		int mn = INF;
		for(int i = 0; i < n; ++i)
		{
			int x;
			scanf("%d", &x);
			s ^= x;
			sum += x;
			mn = min(mn, x);
		}
		printf("Case #%d: ", tt + 1);
		if (s)
		{
			puts("NO");
		}
		else
		{
			printf("%d\n", sum - mn);
		}
	}
	return 0;
}