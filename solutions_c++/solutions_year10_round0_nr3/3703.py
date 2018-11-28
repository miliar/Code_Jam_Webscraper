#include <stdio.h>

void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "a+");
	int NumCases;
	unsigned long int Profit;

	fscanf(InStream, "%d", &NumCases);

	unsigned long int * Queue; 
	unsigned long int First;

	for (int Case=1; Case <= NumCases; Case++)
	{
		Profit = 0;
		unsigned long int R, K, N;
		fscanf(InStream, "%ld", &R);
		fscanf(InStream, "%ld", &K);
		fscanf(InStream, "%ld", &N);
		Queue = new unsigned long int [N];
		First = 0;
		for (unsigned long int j=0; j<N; j++)
			fscanf(InStream, "%ld", &Queue[j]);
		
		for (unsigned long int j=0; j<R; j++)
		{
			unsigned long int Begin = First;
			unsigned long int Pass = 0;
			bool flag = true;
			while ((Pass+Queue[First] <= K)&&(flag))
			{
				Pass = Pass+Queue[First];
				Profit += Queue[First];
				First = (First+1)%N;
				flag = (First != Begin);
			}
		}

		fprintf(OutStream, "Case #%d: %ld\n", Case, Profit);
	}

	fclose(InStream);
	fclose(OutStream);
}