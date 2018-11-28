#include <iostream.h>
#include <string.h>

#define DEBUG

char SENames[101][101], queries[1000][101];
int numQueries = 0, numSE = 0;

// this process can be improved using a hash table instead
int getSEIndex( char strSE[] )
{
	for( int i = 0; i < numSE; i++ )
		if( strcmp( SENames[i], strSE ) == 0 )
			return i;
}

bool allFlagged( bool SEFoundFlag[] )
{
	for( int i = 0; i < numSE; i++ )
		if( !SEFoundFlag[i] )
			return false;

	return true;
}

void resetFlags( bool SEFoundFlag[] )
{
	for( int i = 0; i < numSE; i++ )
		SEFoundFlag[i] = false;	
}

int getMinSwitches()
{
	int i = 0, numSwitches = 0;
	bool SEFoundFlag[100];

	resetFlags( SEFoundFlag );
	for( i = 0; i < numQueries; i++ )
	{
		SEFoundFlag[getSEIndex( queries[i] )] = true;
		if( allFlagged( SEFoundFlag ) )
		{
			resetFlags( SEFoundFlag );
			SEFoundFlag[getSEIndex( queries[i] )] = true;
			numSwitches++;
		}
	}

	return numSwitches;
}

int main( int argc, char *argv[] )
{
	FILE *fpIn, *fpOut;
	int numTestCases, caseNum = 1, i;
	char genStr[3];
	
	if( ( fpIn = fopen( argv[1], "r" ) ) == 0 )
	{
		cout << "Problem opening input file" << endl;
		return 1;
	}

	if( ( fpOut = fopen( argv[2], "w" ) ) == 0 )
	{
		cout << "Problem opening output file" << endl;
		return 1;
	}

	fscanf( fpIn, "%d", &numTestCases );

#ifdef DEBUG
	cout << "Num Test Cases : " << numTestCases << endl;
#endif

	while( caseNum <= numTestCases )
	{
		fscanf( fpIn, "%d", &numSE );
		fgets( genStr, 2, fpIn ); // skip over newline?!?
		for( i = 0; i < numSE; i++ )
		{
			fgets( SENames[i], 100, fpIn );
#ifdef DEBUG
			cout << "se_" << i << " : " << SENames[i] << endl;
#endif
		}
		fscanf( fpIn, "%d", &numQueries );
		fgets( genStr, 2, fpIn ); // skip over newline?!?
		for( i = 0; i < numQueries; i++ )
		{
			fgets( queries[i], 100, fpIn );
#ifdef DEBUG
			cout << "q_" << i << " : " << queries[i] << endl;
#endif
		}

		fprintf( fpOut, "Case #%d: %d\n", caseNum, getMinSwitches() );

		caseNum++;
	}
}
