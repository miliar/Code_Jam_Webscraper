#include <iostream>

const int maxN = 30;
int T, N, K;
int f[maxN+1];

int main(void)
{
	int i, j;

	freopen("snapper.in", "r", stdin);
	freopen("snapper.out", "w", stdout);
	scanf("%d", &T);
	for(i=1; i<=T; i++)
	{
		scanf("%d%d", &N, &K);
		f[1] = 1;
		for(j=2; j<=N; j++)
			f[j] = f[j-1] * 2 + 1;
		if(f[N] > K) printf("Case #%d: OFF\n", i);
		else
		{
			if((K - f[N]) % (f[N] + 1) == 0) printf("Case #%d: ON\n", i);
			else printf("Case #%d: OFF\n", i);
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}