#include <stdio.h>

const int MOD = 100003;

int dp[501][501]; //число*номер

int C[501][502];

int main()
{
	int T,test, i, j, k;
	scanf("%d", &T);

	for (i=1;i<=500;i++)
	{
		C[i][0] = C[i][i] = 1;
	}

	for(i=2;i<=500;i++)
		for (j=1;j<i;j++)
			C[i][j] = (C[i-1][j-1] + C[i-1][j])%MOD;

	for (i=0;i<=500;i++)
		for (j=0;j<=500;j++)
			dp[i][j] = 0;

	for (i=2;i<=500;i++)
		dp[i][1] = 1;

	for (j=2;j<=500;j++)//номер числа
		for (i=j+1;i<=500;i++)//число
		{
			for (k=1;k<j;k++)//номер попереднього числа
				if (dp[j][k])
				{
					long long curr, a = dp[j][k], b = C[i-j-1][j-k-1];
					
					if (i-j-1 < j-k-1) b = 0;
					if (i-j-1==0 && j-k-1==0) b = 1;
					curr = a*b;
					curr%=(long long)MOD;
					dp[i][j]+=curr;

				}
		}


	for (test=0;test<T;test++)
	{
		int n, res=0;
		scanf("%d", &n);
		for (i=1;i<=n;i++)
			res = (res + dp[n][i])%MOD;
		printf("Case #%d: %d\n", test+1, res);
	}

	return 0;
}