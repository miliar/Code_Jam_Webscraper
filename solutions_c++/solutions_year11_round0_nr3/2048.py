#include <cstdio>
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		int n;
		scanf("%d", &n);
		int c, curr = 0, sum = 0;
		int min = 1000001;
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &c);
			curr ^= c;
			sum += c;
			if (c < min)
				min = c;
		}
		printf("Case #%d: ", i + 1);
		if (curr)
			printf("NO\n");
		else
			printf("%d\n", sum - min);
	}
	return 0;
}