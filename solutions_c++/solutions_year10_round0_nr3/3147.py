#include <stdio.h>

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int R, k, N, G = 0;
		scanf("%d %d %d", &R, &k, &N);
		int * gp = new int[N];
		for (int n = 0; n < N; n++)
			scanf("%d", &gp[n]);
		for(int r = 0, n = 0, ln = 0, g = 0; r < R; G += g, g = 0, ln = n, r++)
			do
			{
				g += gp[n];
				if(++n == N)
					n = 0;
			} while(n != ln && g + gp[n] <= k);
		printf("Case #%d: %d\n", t, G);
		delete[] gp;
	}

	return 0;
}
