#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "w");
	char* possible = "Possible";
	char* broken = "Broken";

	int NumCases;
	fscanf(InStream, "%d", &NumCases);

	int PD, PG; 
	unsigned long N;

	for (int Case = 1; Case <= NumCases; Case++)
	{
		fscanf (InStream, "%ld", &N);
		fscanf (InStream, "%d", &PD);
		fscanf (InStream, "%d", &PG);
		if (((PG==100)&&(PD<100))||((PG==0)&&(PD>0)))
		{
			fprintf (OutStream, "Case #%d: %s\n", Case, broken);
			continue;
		}
		if (((PD==100)&&(PG==100))||((PD==0)&&(PG==0)))
		{
			fprintf (OutStream, "Case #%d: %s\n", Case, possible);
			continue;
		}
		bool flag = false;
		for (unsigned long D=1; D<=N; D++)
		{
			for (unsigned long WD=1; WD<=D; WD++)
			{
				if ((100*double(WD)/double(D))==PD)
					flag = true;
			}
		}
		if (flag)
			fprintf(OutStream, "Case #%d: %s\n", Case, possible);
		else
			fprintf(OutStream, "Case #%d: %s\n", Case, broken);
	}

	fclose(InStream);
	fclose(OutStream);
}