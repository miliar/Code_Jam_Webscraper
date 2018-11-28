#include <cstdio>
#include <cstring>


int nt;

int C[1000][1000];

int T[501][501];

const int M = 100003;

int n;

int main()
{
	for(int i = 0; i < 1000; i++) C[i][0] = 1;

	for(int i = 1; i < 1000; i++)
	for(int j = 1; j <= i; j++) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % M;


	for(n = 1; n <= 500; n++) T[n][1] = 1;

	__int64 tmp;

	for(n = 2; n <= 500; n++)
	for(int k = 2; k <= n; k++)
	{
		T[n][k] = 0;

		for(int l = 1; l < k; l++)
		{
			tmp = T[k][l];
			tmp *= C[n - k - 1][k - l - 1];
			tmp %= M;

			T[n][k] = (T[n][k] + tmp) % M;
		}

//		printf("T[%d][%d] = %d\n", n, k, T[n][k]);
	}


	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d", &n);

		int res = 0;
		for(int k = 1; k <= n; k++) res = (res + T[n][k]) % M;

		printf("%d\n", res);
	}

	return 0;	
}