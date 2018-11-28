#include <stdio.h>

void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "a+");
	int NumCases;
	unsigned long long Profit;

	fscanf(InStream, "%d", &NumCases);

	unsigned long int * Queue; 
	unsigned long long First;

	unsigned long int * TurnsFirst;
	unsigned long int * TurnsProfit;

	for (int Case=1; Case <= NumCases; Case++)
	{
		Profit = 0;
		unsigned long long R, K, N;
		fscanf(InStream, "%lld", &R);
		fscanf(InStream, "%lld", &K);
		fscanf(InStream, "%lld", &N);
		Queue = new unsigned long int [N];
		TurnsFirst = new unsigned long int [N];
		TurnsProfit = new unsigned long int [N];
		First = 0;
		for (unsigned long long j=0; j<N; j++)
		{
			fscanf(InStream, "%ld", &Queue[j]);
			TurnsFirst[j] = 0;
			TurnsProfit[j] = 0;
		}
		
		for (unsigned long long j=0; j<R; j++)
		{
			if (TurnsProfit[First] == 0)
			{
				unsigned long long Begin = First;
				unsigned long long Pass = 0;
				bool flag = true;
				while ((Pass+Queue[First] <= K)&&(flag))
				{
					Pass = Pass+Queue[First];
//					Profit += Queue[First];
					First = (First+1)%N;
					flag = (First != Begin);
				}
				Profit += Pass;
				TurnsProfit[Begin] = Pass;
				TurnsFirst[Begin] = First;
			}
			else
			{
				Profit += TurnsProfit[First];
				First = TurnsFirst[First];
				
			}
		}
		delete [] Queue;
		delete [] TurnsFirst;
		delete [] TurnsProfit;

		fprintf(OutStream, "Case #%d: %lld\n", Case, Profit);
	}

	fclose(InStream);
	fclose(OutStream);
}