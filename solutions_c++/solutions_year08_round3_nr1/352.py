#include <stdio.h>
#include <stdlib.h>

void swap(long long &a, long long &b)
{
	long long tmp = a;
	a=b;
	b=tmp;
}


void MaxToMin(long long* v, int N)
{
	int PosMax;
	for (int i=0; i<N-1; i++)
	{
		PosMax = i;
		for (int j=i+1; j<N; j++)
		{
			if (v[j]>v[PosMax])
				PosMax = j;
		}
		swap(v[i], v[PosMax]);
	}
}

void main()
{
	FILE* InFile = fopen("input.txt", "a+");
	FILE* OutFile = fopen("output.txt", "a+");

	int NCases;
	fscanf(InFile, "%d", &NCases);

	int P, K, L;

	long long result;
	long long *freq;

	for (int i=0; i<NCases; i++)
	{
		result = 0;
		fscanf(InFile, "%d %d %d", &P, &K, &L);
		freq = new long long [L];

		for (int k=0; k<L; k++)
			fscanf(InFile, "%lld", &freq[k]);

		MaxToMin(freq, L);

		for (int k=0; k<L; k++)
		{
			result += (int(k/K)+1)*freq[k];
		}

		fprintf(OutFile, "Case #%d: %lld\n", i+1, result);
		delete [] freq;
	}

	fclose(InFile);
	fclose(OutFile);
}