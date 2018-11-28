#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

FILE* fp1;
FILE* fp2; 
char str[505];
int n;
int f[20][505], g[20][505], r;

int main()
{
	fp1 = fopen("C-large.in", "r+");
	fp2 = fopen("b.txt", "w+");
	fscanf (fp1, "%d", &n);
	fgets(str, 503, fp1);
	for (int pp = 1; pp <= n; pp++)
	{
		fgets(str, 503, fp1);
		for (int i = 1; i < 20; i++) f[i][0] = 0;
		for (int i = 0; i < strlen(str); i++)
		{
			if (str[i] == 'w')
			{
				f[1][0]++;
				f[1][f[1][0]] = i;
			}
			else if (str[i] == 'e')
			{
				f[2][0]++;
				f[2][f[2][0]] = i;
				f[7][0]++;
				f[7][f[7][0]] = i;
				f[15][0]++;
				f[15][f[15][0]] = i;
			}
			else if (str[i] == 'l')
			{
				f[3][0]++;
				f[3][f[3][0]] = i;
			}
			else if (str[i] == 'c')
			{
				f[4][0]++;
				f[4][f[4][0]] = i;
				f[12][0]++;
				f[12][f[12][0]] = i;
			}
			else if (str[i] == 'o')
			{
				f[5][0]++;
				f[5][f[5][0]] = i;
				f[10][0]++;
				f[10][f[10][0]] = i;
				f[13][0]++;
				f[13][f[13][0]] = i;
			}
			else if (str[i] == 'm')
			{
				f[6][0]++;
				f[6][f[6][0]] = i;
				f[19][0]++;
				f[19][f[19][0]] = i;
			}
			else if (str[i] == ' ')
			{
				f[8][0]++;
				f[8][f[8][0]] = i;
				f[11][0]++;
				f[11][f[11][0]] = i;
				f[16][0]++;
				f[16][f[16][0]] = i;
			}
			else if (str[i] == 't')
			{
				f[9][0]++;
				f[9][f[9][0]] = i;
			}
			else if (str[i] == 'd')
			{
				f[14][0]++;
				f[14][f[14][0]] = i;
			}
			else if (str[i] == 'j')
			{
				f[17][0]++;
				f[17][f[17][0]] = i;
			}
			else if (str[i] == 'a')
			{
				f[18][0]++;
				f[18][f[18][0]] = i;
			}
		}
		memset(g, 0, sizeof(g));
		for (int i = 1; i <= f[1][0]; i++) g[1][i] = 1;
		for (int i = 2; i < 20; i++)
			for (int j = 1; j <= f[i][0]; j++) 
				for (int k = 1; k <= f[i - 1][0]; k++) 
					if (f[i - 1][k] < f[i][j]) 
					{
						g[i][j] += g[i - 1][k];
						g[i][j] %= 10000;
					}
		r = 0;
		for (int i = 1; i <= f[19][0]; i++)
		{
			r += g[19][i];
			r %= 10000;
		}
		fprintf(fp2, "Case #%d: %04d\n", pp, r);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}
