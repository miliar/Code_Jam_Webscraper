#include <stdio.h>


unsigned long MaxResult = 0;

void Solve(unsigned long int L, unsigned long int P, unsigned long int C, unsigned long res)
{
	if (P<=L*C)
	{
		if (res>MaxResult)
			MaxResult = res;
		return;
	}

	else
	{
		unsigned long int NewL=L, NewP=P;
		int step=1;
		while (NewL<NewP)
		{
			NewL = NewL*C;
			NewP = NewP/C;
			step++;
		}
		res++;
		Solve(L, NewL, C, res);
		Solve (NewL, P, C, res);
	}
}

void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "a+");

	int NumCase;
	fscanf(InStream, "%d", &NumCase);

	for (int Case = 1; Case<=NumCase; Case++)
	{
		unsigned long int result = 0;
		MaxResult = 0;
		unsigned long int L, P, C;
		fscanf(InStream, "%ld %ld %ld", &L, &P, &C);
		Solve (L, P, C, result);
		fprintf(OutStream, "Case #%d: %ld\n", Case, MaxResult);
	}

	fclose(InStream);
	fclose(OutStream);
}
