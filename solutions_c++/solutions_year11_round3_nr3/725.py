#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void main()
{
	FILE *InStream, *OutStream;
	InStream = fopen("in.txt", "a+");
	OutStream = fopen("out.txt", "w");

	int NumCases;
	fscanf(InStream, "%d", &NumCases);

	for (int Case=1; Case<=NumCases; Case++)
	{
		int N, L, H;
		fscanf(InStream, "%d", &N);
		fscanf(InStream, "%d", &L);
		fscanf(InStream, "%d", &H);

		int* freq = new int [N];
		for (int i=0; i<N; i++)
			fscanf(InStream, "%d", &freq[i]);

		bool flag = false;
		int result = -1;

		for (int i=L; i<=H; i++)
		{
			flag = true;
			for (int j=0; j<N; j++)
			{
				if (((i>=freq[j])&&(i%freq[j]==0))||((freq[j]>i)&&(freq[j]%i==0)))
					continue;
				else
					flag = false;
			}
			if (flag)
			{
				result = i;
				break;
			}
		}

		
		if (result != -1)
			fprintf(OutStream, "Case #%d: %d\n", Case, result);
		else
			fprintf(OutStream, "Case #%d: NO\n", Case);

		delete [] freq;
	}

	fclose(InStream);
	fclose(OutStream);
}