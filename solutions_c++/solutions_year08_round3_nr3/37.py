#include <stdio.h>

#define nmax 50005
#define mmax 1005
#define mod 1000000007

int T, n, m, a[nmax];
long long X, Y, Z;
long long A[mmax], sum;
long long c[nmax];

int main()
{
	freopen("c.in", "r", stdin);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d%d%Ld%Ld%Ld", &n, &m, &X, &Y, &Z);
		for(int i = 0; i < m; i++) scanf("%Ld", &A[i]);

		for(int i = 0; i < n; i++)
		{
			a[i] = A[i % m];
			A[i % m] = (long long)((long long)X * A[i % m] + Y * (i + 1)) % Z;
		}

		long long sum = 0;
		for(int i = 0; i < n; i++)
		{
			c[i] = 1;
			for(int j = 0; j < i; j++)
				if(a[j] < a[i]) 
				{
					c[i] += (long long)c[j];
					while(c[i] >= mod) c[i] -= mod;
				}
			sum += (long long)c[i];
			while(sum >= mod) sum -= mod;
		}
		printf("Case #%d: %Ld\n", t, sum);
	}
}
