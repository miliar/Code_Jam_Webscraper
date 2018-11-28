#include <cstdio>

int main()
{
	freopen("D:/in.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int t;
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		int N;
		scanf("%d", &N);
		int m = -1;
		int xor = 0;
		int sum = 0;
		while (N--)
		{
			int c;
			scanf("%d", &c);
			xor = xor ^ c;
			sum += c;
			if (m == -1 || m > c) m = c;
		}
		if (xor != 0) printf("NO\n");
		else printf("%d\n", sum - m);
	}
	return 0;
}
