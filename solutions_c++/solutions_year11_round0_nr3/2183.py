#include <stdio.h>

int main()
{
	int T;

	scanf("%d", &T);
	for (int cases = 0; cases < T; cases ++) {
		int N;
		scanf("%d", &N);

		int min = 1000000000, check = 0, sum = 0;
		for (int i = 0; i<N; i++) {
			int c;
			scanf("%d", &c);
			
			check ^= c;
			sum += c;
			if (c < min)
				min = c;
		}

		printf("Case #%d: ", cases+1);
		if (check != 0)
			printf("NO\n");
		else
			printf("%d\n", sum-min);
	}
}
