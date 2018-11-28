// AlienNumber.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <string.h>


int main(int argc, char* argv[])
{
	FILE *pIn = fopen("C:\\jam\\A-large-practice.in", "r");
	FILE *pOt = fopen("C:\\jam\\A-large-practice.ot", "w");

	int caseNum = 0;

	fscanf(pIn, "%d", &caseNum);

	int mask[33] = {0};

	for(int i =1 ; i < 33 ; i++)
	{
		mask[i] = (mask[i-1] << 1) + 1;
	}

	for(int i = 0 ; i < caseNum ; i++)
	{
		int nSnappers =0;
		int nTime = 0;

		fscanf(pIn, "%d %d", &nSnappers, &nTime);

//		int ret = (nTime >> (nSnappers -1)) & 0x00000001;
		int ret = nTime & mask[nSnappers];

		// output
		if(ret == mask[nSnappers])
			fprintf(pOt, "Case #%d: ON\n", i+1 );
		else
			fprintf(pOt, "Case #%d: OFF\n", i+1 );
	}
	fclose(pOt);
	fclose(pIn);

	return 0;
}



