#include <cstdio>

int T, N, M;
int a[100][100];
char c[100][100];

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	int i, j, t;
	scanf("%d\n", &T);
	
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		
		scanf("%d %d\n", &N, &M);
		int ok = 1;
		
		for (i = 1; i <= N; i++)
		{
			scanf("%s", c[i]);
			for (j = 0; j < M; j++)
				a[i][j + 1] = c[i][j] == '.' ? 0 : 1;
		}
		
		for (i = 1; i <= N; i++)
		{
			for (j = 1; j <= M; j++)
			{
				if (a[i][j] == 1)
				{
					a[i][j] = 2;
					if (a[i][j + 1] == 1) a[i][j + 1] = 3;
					else { ok = 0; break;}
					if (a[i + 1][j] == 1) a[i + 1][j] = 4;
					else { ok = 0; break;}
					if (a[i + 1][j + 1] == 1) a[i + 1][j + 1] = 5;
					else { ok = 0; break;}
					if (i == N || j == M) {ok = 0; break;}
				}				
			}
			if (ok == 0) break;
		}
		
		if (ok == 0) printf("Impossible\n");
		else
		{
			for (i = 1; i <= N; i++)
			{
				for (j = 1; j <= M; j++)
				{
					switch(a[i][j])
					{
					case 0 : {printf("."); break;}
					case 2 : {printf("/"); break;}
					case 3 : {printf("\\"); break;}
					case 4 : {printf("\\"); break;}
					case 5 : {printf("/"); break;}
					}
				}
				printf("\n");
			}
		}
	}
	return 0;
}	