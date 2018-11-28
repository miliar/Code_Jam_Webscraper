#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <deque>

using namespace std;

int a[1010];
int b[1010];
int n;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d %d", &a[i], &b[i]);

		int res = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = i + 1; j < n; ++j)
			{
				if (a[i] < a[j] && b[i] > b[j] ||
					a[i] > a[j] && b[i] < b[j])
					++res;
			}
		}
		printf("Case #%d: %d\n", t + 1, res);
	}

	return 0;
}