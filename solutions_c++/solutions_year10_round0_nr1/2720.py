#include <stdio.h>

bool SnapResult(int nNumOfSnappers, int nNumOfClicks)
{
	bool bResult = false;

	bool bChecker;
	bool *bSnapperArray;

	bSnapperArray = new bool[nNumOfSnappers];

	for( int i=0; i<nNumOfSnappers; i++ )
	{
		bSnapperArray[i] = false;
	}

	for( int j=0; j<nNumOfClicks; j++ )
	{
		for( int k=nNumOfSnappers-1; k>=1; k-- )
		{
			bChecker = true;

			for( int m=0; m<k; m++)
			{
				if( !bSnapperArray[m] )
				{
					bChecker = false;
					break;
				}
			}

			if( bChecker )
			{
				bSnapperArray[k] = !bSnapperArray[k];
			}
		}

		bSnapperArray[0] = !bSnapperArray[0];
	}

	bChecker = true;
	for( int n=0; n<nNumOfSnappers; n++ )
	{
		if( !bSnapperArray[n] )
		{
			bChecker = false;
			break;
		}
	}

	if( bChecker )
	{
		bResult = true;
	}

	delete [] bSnapperArray;

	return bResult;
}

int main()
{	
	int nNumOfCases = 0;
	int nNumOfSnappers = 0;
	int nNumOfClicks = 0;
	int nCurCase = 0;

	FILE *pFileInput;
	FILE *pFileOutput;

	pFileInput = fopen(".\\A-small-attempt0.in", "r");
	pFileOutput = fopen(".\\Q1.out", "w+");

	if( pFileInput != NULL && pFileOutput != NULL)
	{
		fscanf(pFileInput, "%d", &nNumOfCases);
		printf("Number of cases: %d\n", nNumOfCases);

		while( !feof(pFileInput) )
		{
			nCurCase++;

			if( nCurCase > nNumOfCases )
			{
				break;
			}

			fscanf(pFileInput, "%d %d", &nNumOfSnappers, &nNumOfClicks);

			if( SnapResult(nNumOfSnappers, nNumOfClicks) )
			{
				fprintf(pFileOutput, "Case #%d: ON\n", nCurCase);
			}
			else
			{
				fprintf(pFileOutput, "Case #%d: OFF\n", nCurCase);
			}
		}
	}

	fclose(pFileInput);
	fclose(pFileOutput);

	return 0;
}