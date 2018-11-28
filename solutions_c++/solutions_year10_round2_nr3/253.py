#include <stdio.h>

const int MOD = 100003;
const int MAXN = 500 + 10;

int c[MAXN][MAXN];
int d[MAXN][MAXN];
int ans[MAXN];

void cal_com()
{
	int i, j;

	c[0][0] = 1;
	for(i = 1; i < MAXN; i++)
	{
		c[i][0] = 1;
		c[i][i] = 1;
		for(j = 1; j < i; j++)
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % MOD;
	}
}

void process()
{
	int i, j, k;
	long long temp;

	cal_com();
	d[0][0] = 1;
	for(i = 1; i < MAXN; i++)
		d[0][i] = d[1][i] = 1;
	for(i = 3; i < MAXN; i++)
	{
		for(j = 2; j+1 <= i; j++)
		{
			for(k = 1; k <= j-1; k++)
			{
				if(i-j-1 >= j-k-1)
				{
					temp = ((long long)d[k][j]) * c[i-j-1][j-k-1];
					temp %= MOD;
					d[j][i] += temp;
				}
			}
		}
	}
	for(i = 2; i < MAXN; i++)
	{
		for(j = 1; j < i; j++)
			ans[i] = (ans[i] + d[j][i]) % MOD;
	}
}

int main()
{
	int t, n, z;

	process();
	z = 1;
	scanf("%d", &t);
	while(t > 0)
	{
		scanf("%d", &n);
		printf("Case #%d: %d\n", z++, ans[n]);
		t--;
	}

	return 0;
}