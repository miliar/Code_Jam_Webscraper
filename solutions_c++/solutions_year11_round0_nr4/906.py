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
	char* szFilename = "C:\\cjdata\\D-large";
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
		//blocks
		int iBlockCount = 0;
		int iBadBlocks =0;
		fscanf(fin, "%d", &iBlockCount);
		int ictr2 = 0;
		while (ictr2 < iBlockCount)
		{
			//read new block in
			int newBlock = 0;
			fscanf(fin, "%d", &newBlock);
			
			if (newBlock != ictr2 +1)
				iBadBlocks++;

			ictr2++;
		}	
		
		char sLineOut[255];
		sprintf(sLineOut, "Case #%d: %1.6f", ictr +1, (float) iBadBlocks);
		
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

