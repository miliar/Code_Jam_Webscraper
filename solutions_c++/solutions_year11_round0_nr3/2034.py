#include <cstdio>

int main()
{
	int T, N;
	scanf("%d", &T);
	for (int c = 0; c < T; c++)
	{
		int candy, min = 1000001;
		int XOR = 0, sum = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &candy);
			sum += candy;
			XOR = XOR ^ candy;
			if (candy < min) min = candy;
		}
		printf("Case #%d: ", c+1);
		if (!XOR) printf("%d\n", sum-min);
		else printf("NO\n");
	}
	return 0;
}
