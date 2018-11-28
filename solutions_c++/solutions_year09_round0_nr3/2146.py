#include<stdio.h>
#include<string.h>

#define MAX 516

char linha[MAX];
char s[64] = "welcome to code jam";

int pd[MAX][MAX];

int calcula(char *v)
{
	int n = strlen(s);
	int m = strlen(v);

	for(int j = 0; j < m; j++)
	{
		if(s[n-1] == v[j])
			pd[n - 1][j] = 1;
		else
			pd[n-1][j] = 0;
	}

	for(int i = n - 2; i >= 0; i--)
	{
		for(int j = m - 1; j >= 0; j--)
		{
			pd[i][j] = 0;
			if(s[i] == v[j])
			for(int k = m - 1; k >= j + 1; k--)
			{
				pd[i][j] = (pd[i][j] + pd[i + 1][k]) % 10000;
			}
		}
	}

	int res = 0;

	for(int i = 0; i < m; i++)
		res = (res + pd[0][i]) % 10000;

	return res;
}

int main()
{
	int res, testes;
	scanf("%d%*c", &testes);

	for(int i = 1; i <= testes; i++)
	{
		gets(linha);

		res = calcula(linha);

		printf("Case #%d: %04d\n", i, res);
	}

	return 0;
}
