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
		int L, t, N, C;
		fscanf(InStream, "%d", &L);
		fscanf(InStream, "%d", &t);
		fscanf(InStream, "%d", &N);
		fscanf(InStream, "%d", &C);

		int* QQQ = new int [C];
		for (int i=0; i<C; i++)
			fscanf(InStream, "%d", &QQQ[i]);

		int* dist = new int [N];
		for (int i=0; i<N; i++)
			dist[i] = QQQ[i%C];

		int* start = new int [N+1];
		start[0] = 0;
		for (int i=1; i<N+1; i++)
			start[i] = start[i-1]+dist[i-1]*2;

		int* marks = new int [N];
		for (int i=0; i<N; i++)
			marks[i] = 0;
		for (int ccc=0; ccc<L; ccc++)
		{
			int max = 0;
			int maxloc = -1;
			int curr;
			for (int i=0; i<N; i++)
			{
				if (marks[i]==0)
				{
					curr = 0;
					if (start[i]>=t)
						curr = dist[i];
					else if ((i<N)&&(start[i]<t)&&(start[i+1]>t))
						curr = dist[i]-0.5*(t-start[i]);
					if (curr>max)
					{
						max = curr;
						maxloc = i;
					}
				}
			}
			marks[maxloc] = 1;
			for (int i=maxloc+1; i<N+1; i++)
				start[i] -=max;
		}


		fprintf(OutStream, "Case #%d: %d\n", Case, start[N]);

		delete [] dist;
		delete [] QQQ;
		delete [] start;
		delete [] marks;
	}

	fclose(InStream);
	fclose(OutStream);
}