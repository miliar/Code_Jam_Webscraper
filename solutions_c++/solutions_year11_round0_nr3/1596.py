#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 1005;
int a[N];
int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++)
	{
		printf("Case #%d: ", i);
		int n;
		scanf("%d", &n);
		int m = 1 << 30, sum = 0, x = 0;
		for (int p, j = 0; j < n; j ++)
		{
			scanf("%d", &p);
			m = min(m, p);
			sum += p;
			x ^= p;
		}
		if (x != 0)
			printf("NO\n");
		else printf("%d\n", sum - m);
	}
	return 0;
}

