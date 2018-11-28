#include<stdio.h>

int main(void)
{
	int cases, round, capacity, groups;
	int N[1000];
	long double total;
	int cnt = 1;
	FILE * F_in = fopen("C-small-attempt0.in", "r");
	FILE * F_out= fopen("C-output.txt","w");

	fscanf(F_in, "%d", &cases);
	while(cases--)
	{
		fscanf(F_in, "%d %d %d", &round, &capacity, &groups);
		int ptrN;
		for(ptrN=0; ptrN < groups; ptrN++)
		{
			fscanf(F_in, "%d", &N[ptrN]);
		}
		total = ptrN = 0;
		while(round--)
		{
			int isOverCap = 0;
			int grp = groups;
			while(grp--)
			{
				isOverCap += N[ptrN];
				total += N[ptrN];
				ptrN++;
				if( ptrN >= groups )
					ptrN = ptrN % groups;
				if( (isOverCap + N[ptrN]) > capacity )
					break;
			}
		}
		fprintf(F_out, "Case #%d: %.0f\n", cnt++, total);
	}
	return 0;
}