#include <cstdio>
#include <cmath>

int main()
{
	int C, N, R, k, g[1000], E, i, k1, n, r;
	scanf("%d", &C);
	for(int c=1; c<=C; c++) {
		scanf("%d %d %d", &R, &k, &N);
		for(n=0; n<N; n++)
			scanf("%d", &g[n]);

		E=i=0;
		for(r=0; r<R; r++) {
			n=k1=0;
			while(++n <= N && (k1+g[i]) <= k) {
				k1 += g[i];
				if(++i >= N) i=0;
			}
			E += k1;
		}

		printf("Case #%d: %d\n", c, E);
	}
}