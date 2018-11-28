#include <cstdio>

int T, L, cL, C, N, a[1005];
int d[1005][1005];

inline int min(int x, int y) {return x < y ? x : y;}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	int i, j, t;
	
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		
		scanf("%d %d %d %d", &L, &cL, &N, &C);
		for (i = 1; i <= C; i++) scanf("%d", &a[i]);
		a[0] = a[C];
		d[1][0] = 0;
		
		for (i = 0; i <= N + 1; i++)
			for (j = 0; j <= L; j++) d[i][j] = 0;
		
		for (i = 2; i <= N + 1; i++)
		{
			for (j = 0; j <= min(L, i); j++)
			{
				if (j == 0) d[i][j] = d[i - 1][j] + a[(i - 1) % C] * 2;
				else
				{
					int x = d[i - 1][j - 1];
					int boost, notBoost;
					if (x < cL)
					{
						if (x + a[(i - 1) % C] * 2 < cL)
						{
							boost = 0;
							notBoost = a[(i - 1) % C] * 2;
						}
						else 
						{
							notBoost = (cL - x);
							boost = a[(i - 1) % C] - notBoost / 2;
						}
					}
					else 
					{
						notBoost = 0;
						boost = a[(i - 1) % C];
					}
					d[i][j] = min(d[i - 1][j] + a[(i - 1) % C] * 2, d[i - 1][j - 1] + boost + notBoost);					
				}
			}
		}
			
		int res = d[N + 1][0];
		for (i = 1; i <= L; i++)
			if (d[N + 1][i] != 0) res = min(res, d[N + 1][i]);
		printf("%d\n", res);
	
	}
	
	return 0;	
}
