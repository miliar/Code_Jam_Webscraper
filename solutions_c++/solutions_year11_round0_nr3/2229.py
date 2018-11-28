#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int main(int paramc, char ** params)
{
	if (paramc > 1)
		freopen(params[1], "r", stdin);
	int t;
	scanf("%d", &t);
	for (int T = 0; T < t; ++T)
	{
		int n, mn = -1u/4, value = 0, x, sum = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &x), value ^= x, mn = min(mn, x), sum += x;
		printf("Case #%d: ", T + 1);
		if (value)
			printf("NO\n");
		else
			printf("%d\n", sum - mn);
	}
	return 0;
}
