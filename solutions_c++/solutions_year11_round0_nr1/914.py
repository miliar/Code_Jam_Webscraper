#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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
	char* szFilename = "C:\\cjdata\\A-large";
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
	//fgets(sIn, 65536, fin);
	fscanf(fin, "%d", &iTCCount);
	//iTCCount = atoi(sIn);
	printf("\nTesting %d cases: ", iTCCount);

	int pos[2];  //position
	int stat[2]; //inactive since move num

	int ictr = 0;
	while (ictr < iTCCount)
	{
		int idxMove = 0;

		pos[0] = 1;
		pos[1] = 1;
		stat[0] = 0;
		stat[1] = 0;

		int iSequenceLength = 0;
		fscanf(fin, "%d", &iSequenceLength);

		int ictr2 = 0;
		while (ictr2 < iSequenceLength)
		{
			char c;
			int nextRobot = 1;
			int buttonPos = 0;
			fscanf(fin, " %c %d", &c, &buttonPos);
			if (c=='O')
				nextRobot = 0;

			idxMove += max(0, abs(buttonPos - pos[nextRobot]) - (idxMove - stat[nextRobot])) +1;  //+1 for the button press
			pos[nextRobot] = buttonPos;
			stat[nextRobot] = idxMove;
	
			ictr2++;
		}	
		
		char sLineOut[255];
		sprintf(sLineOut, "Case #%d: %d", ictr +1, idxMove);
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

