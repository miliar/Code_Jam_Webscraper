#include<stdio.h>

#define MAXL 32
#define MAXAL 32
#define MAXD 5500
#define ABERTO -1
#define FECHADO 1

int mrc[MAXL][MAXAL];
char word[MAXD][MAXL];
char p[MAXL*MAXL];

int L, D, N;

int calcula(char *p)
{
	for(int i = 0; i < L; i++)
		for(int j = 0; j < MAXAL; j++)
			mrc[i][j] = 0;

	int k = 0;
	int par = FECHADO;

	for(int i = 0; p[i] != 0; i++)
	{
		if(p[i] == '(')
		{
			par = ABERTO;
		}
		else if(p[i] == ')')
		{
			par = FECHADO;
			k++;
		}
		else
		{
			mrc[k][p[i] - 'a'] = 1;
			if(par == FECHADO) k++;
		}
	}

	int tot = 0;

	for(int i = 0; i < D; i++)
	{
		tot++;
		for(int j = 0; j < L; j++)
		{
			if(mrc[j][word[i][j] - 'a'] == 0)
			{
				tot--;
				break;
			}
		}
	}

	return tot;
}

int main()
{
	int res, teste = 0;
	scanf("%d %d %d", &L, &D, &N);

	for(int i = 0; i < D; i++)
		scanf(" %s", word[i]);

	for(int i = 0; i < N; i++)
	{
		scanf("%s", p);
		res = calcula(p);
		teste++;
		printf("Case #%d: %d\n", teste, res);
	}

	return 0;
}
