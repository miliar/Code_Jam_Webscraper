#include <iostream>


const long long mod = 100003;
const int maxN = 500;


long long power[600], ans[600][600], c[600][600];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	power[0] = 1;
	for(int i = 1; i < 510; i++)
		power[i] = (power[i - 1] * 2) % mod;
	memset(c, 0, sizeof(c));
	c[0][0] = 1;
	for(int i = 1; i <= maxN; i++)
		for(int j = 0; j <= maxN; j++)
			c[i][j] = (c[i - 1][j] + (j > 0 ? c[i - 1][j - 1] : 0)) % mod;
	for(int i = 2; i <= maxN; i++)
		ans[i][1] = 1;
	for(int i = 2; i <= maxN; i++)
		for(int j = 2; j < i; j++)
		{
			ans[i][j] = 0;
			for(int k = 1; k < j; k++)
				ans[i][j] = (ans[i][j] + ans[j][k] * c[i - j - 1][j - k - 1]) % mod;
		}
	int t;
	scanf("%d", &t);
	for(int test = 0; test < t; test++)
	{
		int n;
		scanf("%d", &n);
		long long x = 0;
		for(int i = 1; i < n; i++)
			x = (x + ans[n][i]) % mod;
		printf("Case #%d: %lld\n", test + 1, x);
	}
}