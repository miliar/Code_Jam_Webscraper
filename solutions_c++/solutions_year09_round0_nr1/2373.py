#include <cstdio>
#include <cstring>

int L, D, N, n, nr;
char cuv[5072][30];
char s[30][30];
char x[5000];

int main()
{
	freopen("alien.in","r",stdin);
	freopen("alien.out","w",stdout);

	int i, j, ok, rez, k, l, bun;


	scanf("%d %d %d\n", &L, &D, &N);

	for (i = 1; i <= D; i++) fgets(cuv[i], 50, stdin);

	for (k = 1; k <= N; k++)
	{
		rez = 0;
		printf("Case #%d: ", k);
		fgets(x, 4550, stdin);

		n = strlen(x);
		nr = 0;
		for (i = 0; i < n; i++)
		{
			if (x[i] == '(')
			{				
				for (j = i + 1; x[j] != ')'; j++) s[nr][j - i - 1] = x[j];
				nr++;
				i = j;
			}
			else
			{
				s[nr][0] = x[i];
				nr++;
			}
		}

		for (i = 1; i <= D; i++)
		{
			ok = 1;
			for (j = 0; j < L; j++)
			{
				bun = 0;
				for (l = 0; l < strlen(s[j]); l++) if (cuv[i][j] == s[j][l]) {bun = 1; break;}
				if (!bun) { ok = 0; break;}
			}
			rez += ok;
		}
		printf("%d\n",rez);
		for (i = 0; i < 30; i++) 
			for (j = 0; j < 30; j++) s[i][j] = NULL;
	}
	return 0;
}
			
				

		
