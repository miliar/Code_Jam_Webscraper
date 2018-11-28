#include <stdio.h>
#include<stdlib.h>
#include<time.h>

int T,R,C;

int U[10];
int V[10];

char pic[100][100];

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");

	fscanf(fin, "%d", &T);
	for(int aaa=1; aaa<=T; aaa++)
	{
		fprintf(fout,"Case #%d:\n", aaa);

		fscanf(fin, "%d%d", &R, &C);

		for(int i = 0; i < R; i++)
			fscanf(fin, "%s", pic[i]);

		for(int i = 0; i < R; i++)
			pic[i][C]='.';

		for(int i = 0; i < C; i++)
			pic[R][i]='.';

		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				if(pic[i][j] == '#')
				{
					pic[i][j] = '/';
					if(pic[i+1][j] != '#') goto hell;
					pic[i+1][j] = '\\';
					if(pic[i][j+1] != '#') goto hell;
					pic[i][j+1] = '\\';
					if(pic[i+1][j+1] != '#') goto hell;
					pic[i+1][j+1] = '/';
				}
			}
		}
		for(int i = 0; i < R; i++)
		{
			pic[i][C]='\n';
			pic[i][C+1]='\0';
			fputs(pic[i], fout);
		}

		continue;
hell:
		fputs("Impossible\n", fout);
	}

	return 0;
}
