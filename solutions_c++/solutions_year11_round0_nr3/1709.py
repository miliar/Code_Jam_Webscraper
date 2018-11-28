#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

int candy[1010];

int main()
{
	int t;
	int n, sum;
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test)
	{
		sum = 0;
		scanf("%d", &n);
		int minCandy = 10000000;
		int ans = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &candy[i]);
			if (candy[i] < minCandy)
				minCandy = candy[i];
			ans ^= candy[i];
			sum += candy[i];
		}
		printf("Case #%d: ", test);
		if (!ans)
			printf("%d\n", sum - minCandy);
		else printf("NO\n");
	}
	return 0;
}