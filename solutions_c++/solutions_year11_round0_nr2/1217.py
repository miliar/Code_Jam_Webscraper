#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>

#define PARA_N 101 

int main(void)
{
	FILE *fpr;
	FILE *fpw;

	int caseNum;
	int n;
	char Comb[8][8];
	int Disp[8][8];
	int Map[256];
	char Res[PARA_N];
	int i, j, k;
	char cA, cB, cC;

	for (i=0; i<256; i++)
	{
		Map[i] = -1;
	}

	Map['Q'] = 0;
	Map['W'] = 1;
	Map['E'] = 2;
	Map['R'] = 3;
	Map['A'] = 4;
	Map['S'] = 5;
	Map['D'] = 6;
	Map['F'] = 7;



	fpr = fopen("B-small-attempt2 (1).in", "r");
	if (!fpr) 
	{
		printf("fail to open the input file!\n");
		return 0;
	}

	fpw = fopen("B-small-attempt2.out", "w");
	if (!fpw)
	{
		printf("fail to open the output file!\n");
		return 0;
	}
	
	fscanf(fpr, "%d", &caseNum);

	for (i=0; i<caseNum; i++)
	{
		memset(Comb, 0, 64*sizeof(char));
		memset(Disp, 0, 64*sizeof(int));
		memset(Res, 0, PARA_N*sizeof(char));

		fscanf(fpr, "%d ", &n);

		if (n>0) 
		{
			for (j=0; j<n; j++)
			{
				fscanf(fpr, "%c", &cA);
				fscanf(fpr, "%c", &cB);
				fscanf(fpr, "%c ", &cC);
				Comb[Map[cA]][Map[cB]] = cC;
				Comb[Map[cB]][Map[cA]] = cC;
			}
		}

		fscanf(fpr, "%d ", &n);

		if (n>0) 
		{
			for (j=0; j<n; j++)
			{
				fscanf(fpr, "%c", &cA);
				fscanf(fpr, "%c ", &cB);
				Disp[Map[cA]][Map[cB]] = 1;
				Disp[Map[cB]][Map[cA]] = 1;
			}
		}

		fscanf(fpr, "%d ", &n);
		k = 0;
		while (n>0)
		{
			fscanf(fpr, "%c", &Res[k]);
			if (k > 0)
			{
				if (Comb[Map[Res[k]]][Map[Res[k-1]]] != 0)
				{
					Res[k-1] = Comb[Map[Res[k]]][Map[Res[k-1]]];
					Res[k] = 0;
					n--;
					continue;
				}
			}

			for (j=0; j<k; j++)
			{
				if (Map[Res[j]] >= 0)
					if (Disp[Map[Res[k]]][Map[Res[j]]] == 1)
					{
						while (k>=0)
						{
							Res[k] = 0;
							k--;
						}
						break;
					}					
			}

			k++;
			n--;
		}

		fprintf(fpw, "Case #%d: [", i+1);
		for (j=0; j<k; j++)
		{
			fprintf(fpw, "%c", Res[j]);
			if (Res[j+1]!=0)
				fprintf(fpw, ", ");
		}
		fprintf(fpw, "]\n");
	}

	fclose(fpr);
	fclose(fpw);
	return 0;
}
