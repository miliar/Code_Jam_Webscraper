#include <stdio.h>

int count[512][512], comb[512][512];

const int MOD = 100003;
int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);
	int i, j, n, poz, k;
	comb[0][0] = 1;
	comb[1][0] = comb[1][1] = 1;
	for(i = 2; i <= 512; ++i)
	{
		comb[i][0] = 1;
		for(j = 1; j <= i; ++j)
			comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD;
	}
	for(n = 2; n <= 500; ++n)
	{
		count[n][1] = 1;
		for(poz = 2; poz < n; ++poz)			
		{
			
			for(k = 1; k < poz; ++k)
				count[n][poz] += (count[poz][k] * comb[n - 1 - poz][poz - 1 - k]) % MOD;
			count[n][n] = (count[n][n] + count[n][poz]) % MOD; 
		}
	}
	
	int ntest, t;
	scanf("%d", &ntest);
	for(t = 1; t <= ntest; ++t)
	{
		scanf("%d", &n);
		printf("Case #%d: %d\n", t, count[n][n] + 1);
	}
	return 0;
}