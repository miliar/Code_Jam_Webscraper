#include <iostream>
#include <algorithm>
#include <math.h>
#include <stdlib.h>

using namespace std;

#define MAX 1024

int a[MAX];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int t;
	int n;
	cin >> t;
	for (int ti = 1; ti <= t; ++ti)
	{
		cin >> n;
		int xorsum = 0;
		int sum = 0;
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &a[i]);
			xorsum ^= a[i];
			sum += a[i];
		}
		if (xorsum != 0)
		{
			printf("Case #%d: NO\n", ti);
			continue;
		}
		sort(a + 1, a + 1 + n);
		printf("Case #%d: %d\n", ti, sum - a[1]);
	}
	return 0;
}

