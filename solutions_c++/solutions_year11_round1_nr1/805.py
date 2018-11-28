#define _CRT_SECURE_NO_DEPRECATE

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

void solveTest()
{
	int pd, pg;
	long long N;
	scanf("%lld%d%d", &N, &pd, &pg);
	bool good = false;
	for(int i = 1; i <= min(N, 100LL); ++i)
	{
		if (i * pd % 100 == 0)
		{
			good = true;
			break;
		}
	}
	if (!good)
	{
		puts("Broken");
		return;
	}
	if (pg == 100 && pd != 100)
	{
		puts("Broken");
		return;
	}
	if (pg == 0 && pd != 0)
	{
		puts("Broken");
		return;
	}
	puts("Possible");
}

int main()
{
	int t;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		cerr << i + 1 << " Done!\n";
		solveTest();
	}
	return 0;
}
