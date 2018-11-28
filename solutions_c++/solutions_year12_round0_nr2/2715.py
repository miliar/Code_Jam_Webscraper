#include<stdio.h>

int isMaxValue(int total, int p)
{
	if((total+2) / 3 >= p)
		return 1;
	return 0;
}

int isSuprising(int total, int p)
{
	int max;
	if((total+4) % 3 == 0)
		max=(total+4) / 3;
	if((total+3) % 3 == 0)
		max=(total+3) / 3;
	if((total+2) % 3 == 0)
		max=(total+2) / 3;

	if(max >= p && max-2 > 0)
		return 1;
	
	return 0;
}

int main()
{
	FILE *fin;
	FILE *fout;
	int count, h, h2, caseNr;
	int N, S, p, better1, better2;

	fin=fopen("input.txt", "r");
	fout=fopen("output.txt", "w");

	fscanf(fin, "%d", &count);

	for(caseNr=1; caseNr <= count; caseNr++)
	{
		fscanf(fin, "%d %d %d ", &N, &S, &p);		
		
		better1=0;
		better2=0;

		for(h=0; h<N; h++)
		{
			fscanf(fin,"%d ", &h2);
			if(isMaxValue(h2, p))
				better1++;
			else
				if(better2<S && isSuprising(h2, p))
					better2++;
		}		
		
		fprintf(fout, "Case #%d: %d\n", caseNr, better1 + better2);
	}

	fclose(fin);
	fclose(fout);
}
