#include <stdio.h>

#if 0
long long fr(int x)
{
	long long res = 1;
	for (int i=1; i<=x; i++)
		res *= i;
	return res;
}

int c(int n, int k)
{
	if (n<k) return 0;
	return fr(n) / fr(k) / fr(n-k);
}

inline int min(int x, int y)
{
	if (x<y) return x;
	return y;
}
#endif 

int main()
{
//	printf("%d\n", c(21,1));
	int t;
	scanf("%d", &t);
	
	for (int ca=0; ca<t; ca++)
	{
		int n;
		scanf("%d", &n);
		
		int f[600][600] = {0};
		
		for (int i=0; i<=n; i++)
			f[0][i] = 1;
		for (int i=1; i<=n; i++)
			for (int j=0; j<=i; j++)
				for (int k=1; k<=j; k++)
				{
					f[i][j] += f[i-k][j];
					f[i][j] %= 100003;
				}
		
		
	
		
#if 0
		f[2][1] = 1;
		for (int i=2; i<=n; i++)
		{
			f[i][1] = 1;
			for (int j=2; j<i; j++)
				for (int k=j; k<=j; k++)
					for (int l=1; l<min(k,j); l++)
					{
						f[i][j] += f[k][l] * c(i-k-1, j-l-1);
						//if (j != l+1)
	//						f[i][j] += f[k][l] * c(i-k, j-l-1);
						printf("f[%d][%d] += f[%d][%d], (%d)\n", i,j,k,l, c(i-k-1, j-l-1));
						//else
						//	f[i][j] += f[k][l] * (k+1 == i);
					}
		}
#endif

#if 0
		for (int i=2; i<=n; i++)
		{
			for (int j=1; j<i; j++)
				printf("%d\t", f[i][j]);
			putchar(10);
		}
#endif
		int res = 0;
		for (int i=1; i<=n; i++)
		{
			res += f[n-1][i];
			res %= 100003;
		}
	printf("Case #%d: %d\n", ca+1, res % 100003);
//		printf("Case #%d: %d\n", ca+1, res);
	}
}
