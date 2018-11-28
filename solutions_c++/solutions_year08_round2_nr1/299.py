#include <stdio.h>
#include <string.h>

long long t, test, i, A, B, C, D, M, x[100010], y[100010], j, k, l, n; 
long long mat[3][3], unu, doi, sol;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &t);

	for(test = 1; test <= t; ++test)
	{
		memset(mat, 0, sizeof(mat));
		sol = 0;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x[0], &y[0], &M);
		mat[x[0] % 3][y[0] % 3] = 1;
		for(i = 1; i < n; ++i)
		{
			x[i] = (A * x[i - 1] + B) % M;
			y[i] = (C * y[i - 1] + D) % M;
			++mat[x[i] % 3][y[i] % 3];
		}
		
		for(i = 0; i < 3; ++i)
		{
			for(j = 0; j < 3; ++j)
			{
				if(mat[i][j] > 0)
				{
					unu = mat[i][j];
					--mat[i][j];
					for(k = 0; k < 3; ++k)
					{
						for(l = 0; l < 3; ++l)
						{
							if(mat[k][l])
							{
								doi = mat[k][l];
								--mat[k][l];
								int a1 = (3 - (i + k) % 3) % 3, a2 = (3 - (j + l) % 3) % 3;
								//printf("%d %d %d %d %d %d\n", i, j, k, l, a1, a2);
								sol += unu * doi * mat[a1][a2];
								++mat[k][l];
							}
						}
					}
					++mat[i][j];
				}
			}
		}
		sol /= 6;
		printf("Case #%lld: %lld\n", test, sol);
	}

	return 0;
}
