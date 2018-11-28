#include <stdio.h>
#include <string.h>

#define nmax 100005

int n, A, B, C, D, x0, y0, M, T;
int x[nmax], y[nmax];
long long a[3][3][4], nou[3][3][4];

int main()
{
	freopen("a.in", "r", stdin);
	// freopen("a.out", "w", stdout);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		x[0] = x0, y[0] = y0;
		for(int i = 1; i < n; i++)
		{
			x[i] = (int)((long long)((long long)A * x[i - 1] + B) % M);
			y[i] = (int)((long long)((long long)C * y[i - 1] + D) % M);
		}

		memset(a, 0, sizeof(a));
		a[0][0][0] = 1;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < 3; j++)
				for(int k = 0; k < 3; k++)
					for(int l = 0; l < 4; l++)
						nou[j][k][l] = 0;
	
			for(int j = 0; j < 3; j++)
				for(int k = 0; k < 3; k++)
					for(int l = 0; l < 4; l++)
						if(a[j][k][l] != 0)
						{
							nou[j][k][l] += (long long)a[j][k][l];
							if(l + 1 < 4)
								nou[(j + x[i]) % 3][(k + y[i]) % 3][l + 1] += (long long)a[j][k][l];
						}

			for(int j = 0; j < 3; j++)
				for(int k = 0; k < 3; k++)
					for(int l = 0; l < 4; l++)
						a[j][k][l] = nou[j][k][l];
		}
		printf("Case #%d: %Ld\n", t, a[0][0][3]);
	}
}
