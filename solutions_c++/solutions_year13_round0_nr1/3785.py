#include <iostream>

const int NMAX = 4;

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
char tic[NMAX + 1][NMAX + 1];
char sir[100];

char xWin[5][5] = {"XXXX", "TXXX", "XTXX", "XXTX", "XXXT"};
char oWin[5][5] = {"OOOO", "TOOO", "OTOO", "OOTO", "OOOT"};

char pos[12][5];
bool hasDot = false;

int main()
{
	fscanf(f, "%d\n", &T);
	for (int t = 0; t < T; ++t)	
	{
		hasDot = false;
		for (int i = 0; i < NMAX; ++i)
		{
			fgets(sir, 100, f);
			for (int j = 0; j < NMAX; ++j)
			{
				tic[i][j] = sir[j];
				if (tic[i][j] == '.')
				{
					hasDot = true;
				}
			}
			tic[i][NMAX] = '\0';
		}
		fscanf(f, "\n");
		int k = 0;
		for (int i = 0; i < NMAX; ++i)
		{
			strcpy(pos[k++], tic[i]);
		}
		for (int i = 0; i < NMAX; ++i)
		{
			for (int j = 0; j < NMAX; ++j)
			{
				pos[k][j] = tic[j][i];
			}
			pos[k][NMAX] = '\0';
			k++;
		}
		for (int i = 0; i < NMAX; ++i)
		{
			pos[k][i] = tic[i][i];
		}
		pos[k][NMAX] = '\0';
		k++;

		for (int i = 0; i < NMAX; ++i)
		{
			pos[k][i] = tic[i][NMAX - i - 1];
		}
		pos[k][NMAX] = '\0';
		k++;

		bool x = false, o = false;
		for (int i = 0; i < 12; ++i)
		{
			for (int j = 0; j < 5; ++j)
			{
				if (!strcmp(pos[i], xWin[j]))
				{
					//x won
					x = true;
				}
				if (!strcmp(pos[i], oWin[j]))
				{
					//o won
					o = true;
				}
			}
		}
		if (x)
		{
			fprintf(g, "Case #%d: X won\n", t + 1); 
		}
		else if (o)
		{
			fprintf(g, "Case #%d: O won\n", t + 1); 
		}
		else if (hasDot)
		{
			fprintf(g, "Case #%d: Game has not completed\n", t + 1); 
		}
		else
		{
			fprintf(g, "Case #%d: Draw\n", t + 1); 
		}
	}
	return 0;
}