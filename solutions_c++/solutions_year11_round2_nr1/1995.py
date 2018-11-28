#include <cstdio>

int T, N;
char c[150][150];
int a[150][150];
int w[150], l[150], nr[150];
double wp[150], owp[150], oowp[150], rat[150];

int main()
{
	freopen("input.in", "r",stdin);
	freopen("output.out","w",stdout);
	
	int i, j, t;
	
	scanf("%d\n", &T);
	
	for (t = 1; t <= T; t++)
	{
		scanf("%d\n", &N);
		for (i = 1; i <= N; i++)
		{
			w[i] = l[i] = nr[i] = 0;
			wp[i] = owp[i] = oowp[i] = 0;
			
			scanf("%s", c[i]);
			for (j = 0; j < N; j++)
				if (c[i][j] == '.') a[i][j + 1] = 0;
				else if (c[i][j] == '1') 
					{
						a[i][j + 1] = 1;
						w[i]++;
						nr[i]++;
					}
				else
				{
					a[i][j + 1] = -1;
					l[i]++;
					nr[i]++;
				}
		}	
		
		for (i = 1; i <= N; i++)
		{
			wp[i] = (double)w[i] / nr[i];
			
			for (j = 1; j <= N; j++)
				if (a[i][j] != 0)
				{
					int wn = w[j];
					if (a[i][j] == -1) wn--;
					
					owp[i] += ((double)wn / (nr[j] - 1));
				}
				
			owp[i] /= nr[i];
		}
		
		printf("Case #%d:\n", t);
		for (i = 1; i <= N; i++)
		{
			for (j = 1; j <= N; j++)
				if (i != j && a[i][j]) oowp[i] += owp[j];
			oowp[i] /= nr[i];
				
			rat[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%lf\n", rat[i]);
		}		
	}
}