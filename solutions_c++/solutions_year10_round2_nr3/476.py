#include <cstdio>

int main()
{
	int t;
	scanf("%u", &t);
	
	int c[501][501] = { 0 };
	c[0][0] = 1;
	
	for (int i = 1; i <= 500; ++i)
	{
		c[i][0] = c[i][i] = 1;
		
		for (int j = 1; j < i; ++j)
		{
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % 100003;
		}
	}
	
	int nways[501][501] = { 0 };
	
	for (int n = 2; n <= 500; ++n)
	{
		nways[n][0] = nways[n][1] = 1;
		
		for (int i = 2; i < n; ++i)
		{
			for (int j = 1, e = i - 1; j <= e; ++j)
			{
				nways[n][i] += (unsigned long long) nways[i][j] * c[n-i-1][i-j-1] % 100003;
				nways[n][i] %= 100003;
			}
			
			nways[n][0] += nways[n][i];
			nways[n][0] %= 100003;
		}
	}
	
	for (int i = 1; i <= t; ++i)
	{
		int n;
		scanf("%u", &n);
		
		int x = nways[n][n-1];
		
		for (int j = 1, e = n - 1; j < e; ++j)
		{
			for (int k = 1; k <= j; ++k)
			{
				x += (unsigned long long) nways[j+1][k] * c[n-j-2][j-k] % 100003;
				x %= 100003;
			}
		}
		
		printf("Case #%u: %u\n", i, x);
	}
	
	return 0;
}
