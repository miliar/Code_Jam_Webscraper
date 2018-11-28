#include <stdio.h>
#include <string.h>
#include <ctype.h>

char string[] = "welcome to code jam";
char Input[1000];
int matrix[1000][1000];
int Inputlen;
int stringLen;

void InitMatrix()
{
	for(int i = 0; i <= stringLen; i++)
	{
		for(int j = 0; j <= Inputlen; j++)
		{
			matrix[i][j] = 0;			
		}
	}
	for(int i = 0; i <= Inputlen; i++)
	{
		matrix[0][i] = 1;
	}
}

void getMatch()
{
	int add = 0;
	for(int i = 1; i <= stringLen; i++)
	{
		for(int j = 1; j <= Inputlen; j++)
		{
			if(Input[j-1] == string[i-1])
			{
				matrix[i][j] = (matrix[i-1][j-1] + matrix[i][j-1])%10000;
			}
			else
			{
				matrix[i][j] = matrix[i][j-1];
			}
		}
	}
}

int main()
{
	int nCase = 1;
	int N;
	
	stringLen = strlen(string);
	
	scanf("%d\n", &N);
	for(int i = 0; i < N; i++)
	{
		gets(Input);
		Inputlen = strlen(Input);
		InitMatrix();
		getMatch();
		printf("Case #%d: %04d\n", nCase, matrix[stringLen][Inputlen]);
		nCase++;
	}

	return 0;
}

//So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam.