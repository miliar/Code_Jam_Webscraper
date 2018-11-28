#include <stdio.h>

int main()
{
	//freopen("C.txt", "r", stdin);
	//freopen("C-small.in", "r", stdin);
	//freopen("C-small.out.txt", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out.txt", "w", stdout);
	int i, t;
	scanf("%d", &t);
	for(i = 1; i <= t; i++)
	{
		int j, n;
		int sum = 0, xsum = 0;
		int smallest = 1000001;
		int a;
		scanf("%d", &n);
		for(j = 0; j < n; j++)
		{
			scanf("%d", &a);
			xsum ^= a;
			sum += a;
			if(a < smallest) smallest = a;
		}
		if(xsum == 0) {
			printf("Case #%d: %d\n", i, sum - smallest);
		} else {
			printf("Case #%d: NO\n", i);
		}
	}

	return 0;
}
