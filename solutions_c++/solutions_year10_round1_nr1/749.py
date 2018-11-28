#include <stdio.h>
#include <string.h>

int	T;
int N, K;
char b[100][100];
char tr[100][100];
char f[100][100];
int cas = 0;

int R, B;

void trans()
{
	int i, j;
	memset(tr, 0, sizeof(tr));
	for (i=N-1; i>=0; i--)
	{
		for (j=0; j<N; j++)
		{
			tr[j][N-i-1] = b[i][j];
		}
	}
	/*for (i=0; i<N; i++)
	{
		printf("%s\n", tr[i]);
	}*/
}

void fall()
{
	int i, j, k;
	
	for (j=0; j<N; j++)
	{		
		for (i=N-1; i>=0; i--)
		{
			for (k=i; k<N; k++)
			{
				if (k+1<N && tr[k][j] != '.' && tr[k+1][j] == '.')
				{
					 tr[k+1][j] = tr[k][j];
					 tr[k][j] = '.';
				}				
			}
		}		
	}
	for (j=0; j<N; j++)
	{
		for (i=N-1; i>=0; i--)
		{
			f[i][j] = tr[i][j];
		}
	}
	/*printf("\n");
	for (i=0; i<N; i++)
	{
		printf("%s\n", f[i]);
	}*/
}

void add(int k, char tar)
{
	if (k < K)	return ;
	if (tar == 'R')
		R++;
	else 
		B++;
}

void from(int x, int y, char tar)
{
	int i, j, k;
	
	i = x, j = y;
	for (k=0; k<K && i < N; k++)
	{
		if (f[i][j] != tar) break;
		i++;
	}
	add(k, tar);
		
	i = x, j = y;
	for (k=0; k<K && j < N; k++)
	{
		if (f[i][j] != tar) break;
		j++;
	}
	add(k, tar);
	
	i = x, j = y;
	for (k=0; k<K && i < N  && j<N; k++)
	{
		if (f[i][j] != tar) break;
		i++;
		j++;
	}
	add(k, tar);

	i = x, j = y;
	for (k=0; k<K && i < N  && j >= 0; k++)
	{
		if (f[i][j] != tar) break;
		i++;
		j--;
	}
	add(k, tar);
}


int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int i, j;

	scanf("%d", &T);
	while (T--)
	{
		scanf("%d %d", &N, &K);
		memset(b, 0, sizeof(b));		
		for (i=0; i<N; i++)
		{
			scanf("%s", b[i]);
		}
		trans();
		fall();

		R = B = 0;
		for (i=0; i<N; i++)
		{
			for (j=0; j<N; j++)
			{
				from(i, j, 'R');
				from(i, j, 'B');
			}
		}

		printf("Case #%d: ", ++cas);
		if (R > 0 && B > 0)
			printf("%s", "Both");
		if (R > 0 && B == 0)
			printf("%s", "Red");
		if (R == 0 && B > 0)
			printf("%s", "Blue");
		if (R == 0 && B == 0)
			printf("%s", "Neither");
		printf("\n");
	}	
	return 0;
}