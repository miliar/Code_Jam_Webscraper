#include <stdio.h>
#define IBF 0

int Val[1000];
int nVal;

int main()
{
	int T, nT, i, S, min;
	FILE *fin=fopen("C-small-attempt0.in", "r");
	FILE *fout=fopen("output.txt", "w");

	fscanf(fin, "%d", &T);
	for (nT=1; nT<=T; nT++)
	{
		fscanf(fin, "%d", &nVal);
		for (i=0; i<nVal; i++)
			fscanf(fin, "%d", &Val[i]);

		S=0;
		for (i=0; i<nVal; i++)
			S = S^Val[i];

		if (S != 0)
		{
			fprintf(fout, "Case #%d: NO\n", nT);
			continue;
		}

		min=S=Val[0];
		for (i=1; i<nVal; i++)
		{
			if (min>Val[i]) min=Val[i];
			S += Val[i];
		}
		fprintf(fout, "Case #%d: %d\n", nT, S-min);
	}

	fclose(fin);
	fclose(fout);
}