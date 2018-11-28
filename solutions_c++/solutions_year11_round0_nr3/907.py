#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#ifndef max
#define max(a,b) (((a) > (b)) ? (a) : (b))
#endif

#ifndef min
#define min(a,b) (((a) < (b)) ? (a) : (b))
#endif

//----------------------------------------------------------------------------
// Useful functions

int ipow(int base, int exp)
{
    int result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}


int main(int argc, char *argv[])
{
	//Variables
	char* szFilename = "C:\\cjdata\\C-large";
	int iTCCount =0;
	
	//Open input/output files
	char szFIn[255], szFOut[255];
	sprintf(szFIn, "%s.in", szFilename);
	sprintf(szFOut, "%s.out", szFilename); 	

	printf("\nOpening input %s, and output %s, ", szFIn, szFOut);

	FILE *fin, *fout;
	fin = fopen(szFIn, "rt");
	fout = fopen(szFOut, "wt");
	if (!fin || !fout)
	{
		printf("error opening files: input %d, output %d", (int) fin, (int) fout);
		abort();
	}

	//process =============================================================
	
	//test cases
	fscanf(fin, "%d", &iTCCount);
	printf("\nTesting %d cases: ", iTCCount);

	int ictr = 0;
	while (ictr < iTCCount)
	{
		//Candies
		int iCandyCount = 0;
		fscanf(fin, "%d", &iCandyCount);

		int ictr2 = 0;
		int TotalCandyVal = 0;
		int realTotal = 0;
		int orVal = 0;
		int loVal = 999999999;
		int newVal =0;
		while (ictr2 < iCandyCount)
		{
			//read each combination in
			fscanf(fin, "%d", &newVal);
			TotalCandyVal ^= newVal;
			orVal |= newVal;
			realTotal += newVal;
			if (loVal > newVal)
				loVal = newVal;
			
			ictr2++;
		}	

		//Work out the highest we can steal
		int iSteal = realTotal - loVal;

		char sLineOut[255];
		if (TotalCandyVal == 0)
			sprintf(sLineOut, "Case #%d: %d", ictr +1, iSteal);
		else
			sprintf(sLineOut, "Case #%d: NO", ictr +1);

		printf("\n%s", sLineOut);
		fprintf(fout, "%s\n", sLineOut);

		ictr++;
	}

	//close files =========================================================
	fclose(fin);
	fclose(fout);
	printf("\nFiles closed.\n");


#if _DEBUG
	system("pause");
#endif

	return 0;
}

