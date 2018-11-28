#include <stdio.h>
#include <stdlib.h>

void main()
{
	int T=0, R=0, K=0, N=0;

	FILE* fi = fopen("input.txt", "r");
	FILE* fo = fopen("output.txt", "w");

	fscanf(fi, "%d", &T);

	for(int t=0; t<T; t++)
	{
		int pGroup=0, pGroupFirst=0, euro=0, curSeat=0;
		int *group;

		fscanf(fi, "%d %d %d", &R, &K, &N);

		group = (int *)malloc(sizeof(int)*N);

		for(int n=0; n<N; n++)
			fscanf(fi, "%d", group+n);

		for(int r=0; r<R; r++)
		{
			curSeat = group[pGroup];
			pGroupFirst = pGroup;

			while(1)
			{
				pGroup = (pGroup+1)%N;

				if( curSeat < K && (group[(pGroup)%N] + curSeat <= K ) && (pGroupFirst != (pGroup)%N) )
				{					
					curSeat += group[pGroup];
				}
				else
				{
					euro += curSeat;
					break;
				}
			}
		}

		free(group);	
		fprintf(fo, "Case #%d: %d\n", t+1, euro);
	}

	fclose(fi);
	fclose(fo);
	
}