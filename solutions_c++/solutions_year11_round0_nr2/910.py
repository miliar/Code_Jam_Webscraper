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

bool execComb(char comb[256][256], char *sInvoked)
{
	int iLen = strlen(sInvoked);
	if (iLen >= 2)
	{
		char c = comb[sInvoked[iLen-2]][sInvoked[iLen-1]];
		if (c != ' ')
		{
			sInvoked[iLen-2] = c;
			sInvoked[iLen-1] = 0;

			return true;
		}
	}

	return false;
}

bool execOpp(bool opp[256][256], char *sInvoked)
{
	int iLen = strlen(sInvoked);
	if (iLen >= 2)
	{
		int ictr = 0;
		while (ictr < iLen -1)
		{
			int ictr2 = 1;
			while (ictr2 < iLen)
			{
				if (opp[sInvoked[ictr]][sInvoked[ictr2]])
				{
					//copy the rest of the string over index ictr
					/*ictr2++;
					while (ictr2 <= iLen)
						sInvoked[ictr++] = sInvoked[ictr2++];
						*/

					//Clear the whole invoked list?
					sInvoked[0] = 0;
					return true;
				}

				ictr2++;
			}

			ictr++;
		}		
	}

	return false;
}

int main(int argc, char *argv[])
{
	//Variables
	//char* szFilename = "C:\\cjdata\\B-small-attempt2";
	char* szFilename = "C:\\cjdata\\B-large";
	//char* szFilename = "C:\\cjdata\\sample";
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
		char comb[256][256];
		bool opp[256][256];

		memset(comb, ' ', 256*256*sizeof(char));
		memset(opp, false, 256*256*sizeof(bool));

		//combinators
		int iCombCount = 0;
		fscanf(fin, "%d", &iCombCount);
		int ictr2 = 0;
		while (ictr2 < iCombCount)
		{
			//Blocks of 3 letters
			char c[5];
			fscanf(fin, " %s", c);

			comb[c[0]][c[1]] = c[2];
			comb[c[1]][c[0]] = c[2];

			ictr2++;
		}	
		
		//Opposers
		int iOppCount = 0;
		fscanf(fin, "%d", &iOppCount);
		ictr2 = 0;
		while (ictr2 < iOppCount)
		{
			//Blocks of 3 letters
			char c[5];
			fscanf(fin, " %s", c);

			opp[c[0]][c[1]] = true;
			opp[c[1]][c[0]] = true;

			ictr2++;
		}	

		//Sequence
		int iSeqCount = 0;
		fscanf(fin, "%d", &iSeqCount);
		char sIn[101];
		fscanf(fin, "%s", sIn);

		char sInvoked[101];
		memset(sInvoked, 0, 101*sizeof(char));

		ictr2 = 0;
		while (ictr2 < iSeqCount)
		{
			int iLen = strlen(sInvoked);
			sInvoked[iLen++] = sIn[ictr2++];
			sInvoked[iLen] = 0;

			bool changed;
			do 
			{
				changed = false;

				while (execComb(comb, sInvoked))
					changed = true;

				if (execOpp(opp, sInvoked))
					changed = true;

			} while (changed);
		}

		char sLineOut[255];
		sprintf(sLineOut, "Case #%d: [", ictr +1 );

		int iLen = strlen(sInvoked);
		ictr2 =0;
		while (ictr2 < iLen)
		{
			if (ictr2 > 0)
				sprintf(sLineOut, "%s, ", sLineOut);

			sprintf(sLineOut, "%s%c", sLineOut, sInvoked[ictr2]);

			ictr2++;
		}
		
		sprintf(sLineOut, "%s]", sLineOut);
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

