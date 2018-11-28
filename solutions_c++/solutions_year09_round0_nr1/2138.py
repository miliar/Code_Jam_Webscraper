#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define L_MAX 15
#define D_MAX 5000

#define INPUTFILE "A-large.in"
#define OUTPUTFILE "A-large.out"

char dict[D_MAX][L_MAX + 1];
char pattern[L_MAX][26];
char line[450];



int main()
{
	FILE *fpIn, *fpOut;

	fpIn = fopen(INPUTFILE, "r");
	fpOut = fopen(OUTPUTFILE, "w");

	int L, D, N;
	fscanf(fpIn, "%d %d %d", &L, &D, &N);

	for (int i = 0; i < D; i++)
	{
		fscanf(fpIn, "%s", dict[i]);
	}

	for (int cnt1 = 0; cnt1 < N; cnt1++)
	{
		for (int i = 0; i < L; i++)
		{
			for (int j = 0; j < 26; j++)
				pattern[i][j] = 0;
		}

		fscanf(fpIn, "%s", line);
		int cnt3 = 0;	
		for (int cnt2 = 0; cnt2 < L; cnt2++)
		{
			if (line[cnt3] == 0)
				break;
			if (line[cnt3] == '(')
			{
				cnt3++;
				while (line[cnt3] != ')')
				{
					int idx = line[cnt3] - 'a';
					pattern[cnt2][idx] = 1;
					cnt3++;
				}
				cnt3++;
			}
			else
			{
				int idx = line[cnt3] - 'a';
				pattern[cnt2][idx] = 1;
				cnt3++;
			}
		} // for (int cnt2 = 0; cnt2 < L; cnt2++)

		int sum = 0;
		for (int cnt2 = 0; cnt2 < D; cnt2++)
		{
			int cnt3 = 0;
			for (; cnt3 < L; cnt3++)
			{
				int idx = dict[cnt2][cnt3] - 'a';
				if (pattern[cnt3][idx] == 0)
					break;
			}

			if (cnt3 == L)
				sum++;
		}

		fprintf(fpOut, "Case #%d: %d\n", cnt1 + 1, sum);

	} // for (int cnt1 = 0; cnt1 < N; cnt1++)

	fclose(fpIn);
	fclose(fpOut);
}