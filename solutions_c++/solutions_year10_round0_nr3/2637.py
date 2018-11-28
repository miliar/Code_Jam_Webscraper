#include <stdio.h>

__int64 GetEuros(unsigned int nNumOfRounds, unsigned int nNumOfSeats, unsigned int nNumOfGroups, unsigned int *nGroupArray)
{
	__int64 n64Result = 0;
	__int64 n64FastCalTotal = -1;

	unsigned int nIndex = 0;
	unsigned int nNewIndex = 0;

	for( unsigned int i=0; i<nNumOfRounds; i++)
	{
		__int64 nSubTotal = 0;

		unsigned int k;
		for( k=0; k<nNumOfGroups; k++)
		{
			nNewIndex = nIndex + k;

			if( nNewIndex >= nNumOfGroups )
			{
				nNewIndex -= nNumOfGroups;
			}

			if( (nSubTotal + nGroupArray[nNewIndex]) <= nNumOfSeats )
			{
				nSubTotal += nGroupArray[nNewIndex];
			}
			else
			{
				break;
			}
		}

		nIndex = nNewIndex;

		//Special case for: everytime the seats can hold all the people
		if( i == 0 && nIndex == 0 )
		{
			n64Result = nSubTotal * nNumOfRounds;

			//Finished, exit calculation
			break;
		}

		n64Result += nSubTotal;

		if( nIndex == 0 && n64FastCalTotal == -1 )
		{
			//First time to Fast Cal
			n64FastCalTotal = n64Result;

			unsigned int nLoopCount = i+1;

			unsigned int nFactor = (nNumOfRounds - i - 1) / nLoopCount;

			if( nFactor > 0 )
			{
				i += (nLoopCount * nFactor);
				n64Result += (n64FastCalTotal * nFactor);
			}

			while( (i + nLoopCount) < nNumOfRounds )
			{
				i += nLoopCount;
				n64Result += n64FastCalTotal;
			}
		}
	}

	return n64Result;
}

int main()
{	
	unsigned int nNumOfCases = 0;
	unsigned int nNumOfRounds = 0;
	unsigned int nNumOfSeats = 0;
	unsigned int nNumOfGroups = 0;
	unsigned int *nGroupArray = NULL;
	unsigned int nCurCase = 0;

	FILE *pFileInput;
	FILE *pFileOutput;

	pFileInput = fopen(".\\C-large.in", "r");
	//pFileInput = fopen(".\\C-small-attempt0.in", "r");
	pFileOutput = fopen(".\\Q3.out", "w+");

	if( pFileInput != NULL && pFileOutput != NULL)
	{
		fscanf(pFileInput, "%u", &nNumOfCases);
		printf("Number of cases: %u\n\n", nNumOfCases);

		while( !feof(pFileInput) )
		{
			nCurCase++;

			if( nCurCase > nNumOfCases )
			{
				break;
			}

			printf("Case #%u:\n", nCurCase);

			fscanf(pFileInput, "%u %u %u", &nNumOfRounds, &nNumOfSeats, &nNumOfGroups);
			printf("Round#: %u, Seat#: %u, Group#: %u\n", nNumOfRounds, nNumOfSeats, nNumOfGroups);

			printf("Group info: ");

			nGroupArray = new unsigned int [nNumOfGroups];

			for( unsigned int i=0; i<nNumOfGroups; i++)
			{
				fscanf(pFileInput, "%u", &nGroupArray[i]);
				printf("%u ", nGroupArray[i]);
			}

			printf("\n\n");

			fprintf(pFileOutput, "Case #%u: %I64d\n", nCurCase, GetEuros(nNumOfRounds, nNumOfSeats, nNumOfGroups, nGroupArray));

			delete [] nGroupArray;
		}
	}

	fclose(pFileInput);
	fclose(pFileOutput);

	return 0;
}