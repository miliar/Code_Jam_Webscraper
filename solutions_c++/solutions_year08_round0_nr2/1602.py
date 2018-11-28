// GCJTT.cpp : Defines the entry point for the console application.
//


#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <io.h>
#include <fcntl.h>
#include <sys/stat.h>

#define MAX_CASE_COUNT		100
#define MAX_TIME			100

typedef struct _tagSCase
{
	int		iA;
	int		iAStart[MAX_TIME];
	int		iAEnd[MAX_TIME];
	int		iAFlag[MAX_TIME];

	int		iB;
	int		iBStart[MAX_TIME];
	int		iBEnd[MAX_TIME];
	int		iBFlag[MAX_TIME];

	int		iAtoBTrips;
	int		iBtoATrips;

}SCase, *PCase;

// Global variables
int iTotalCases = 0;
int iTurnAroundTime = 0;
SCase sc[MAX_CASE_COUNT];
char *pBuf = NULL;
int iFileLength = 0;
int iCurrentPos = 0;
int iLastPos = 0;
char szDummy[200] = "\0";


// Funtion definitions
int ReadInputFile();
void BuildCases();
void GetNextLine();
void GetCase( int iCaseNumber );
void SortArray( int *pArr, int iArrCount );

int main(int argc, char* argv[])
{
	memset( &sc, '\0', sizeof( SCase ) * MAX_CASE_COUNT );

	int iRetVal = ReadInputFile();
	if ( iRetVal < 0 )	return -1;

	BuildCases();

	for ( int i = 0; i < iTotalCases; i++ )
	{
		printf( "\nCase #%d: %d %d", i + 1, sc[i].iAtoBTrips, sc[i].iBtoATrips );
	}

	int fd = _open( "B-large.out", _O_WRONLY | _O_BINARY | _O_CREAT, _S_IWRITE );
	if ( fd == -1 )
	{
		printf( "Unable to create output file, please check your path" );
		return -1;
	}

	for ( i = 0; i < iTotalCases; i++ )
	{
		sprintf( szDummy, "Case #%d: %d %d\n", i + 1, sc[i].iAtoBTrips, sc[i].iBtoATrips );
		_write( fd, szDummy, strlen( szDummy ) );
	}

	_close( fd );

	if ( pBuf )
	{
		delete pBuf;
		pBuf = NULL;
	}
	return 0;
}

int ReadInputFile()
{
	char szInputFile[] = "B-large.in";
	
	int fd = _open( szInputFile, _O_RDONLY | _O_BINARY, _S_IREAD );
	if ( fd == -1 )
	{
		printf( "Please check file path" );
		return -1;
	}

	iFileLength = _lseek( fd, 0L, SEEK_END );
	_lseek( fd, 0L, SEEK_SET );

	pBuf = new char[iFileLength];
	if ( pBuf == NULL )
	{
		printf( "Unable to allocate memory" );
		return -1;
	}

	_read( fd, pBuf, iFileLength );
	_close( fd );

	return 0;
}

void BuildCases( )
{
	int i = 0;
	int j = 0;
	int k = 0;
	int l = 0;
	int iMax = 0;
	int iLast = 0;
	int iTempMax = 0;

	bool bFound = false;
	bool bTakeBreak = false;

	iCurrentPos = 0;
	
	// Get the total cases first
	GetNextLine();
	iTotalCases = atoi( szDummy );

	// Get the next count of the S 
	for ( i = 0; i < iTotalCases; i++ )
	{
		GetCase( i );
	}

	printf( "\nTotal case count is %d\n", iTotalCases );

	// Now assign number of S in QLocation
	for ( i = 0; i < iTotalCases; i++ )
	{
		// From A to B
		for ( j = 0; j < sc[i].iA; j++ )
		{
			iMax = 3660;	// Max value in minutes
			iTempMax = -1;	// No valid index
			
			for ( k = 0; k < sc[i].iB; k++ )
			{
				if ( sc[i].iBFlag[k] )
				{
					continue;
				}

				if ( sc[i].iAEnd[j] <= sc[i].iBStart[k] )
				{
					if ( iMax > sc[i].iBStart[k] )
					{
						iMax = sc[i].iBStart[k];
						iTempMax = k;
					}
				}
			}
			
			if ( iTempMax >= 0 )
			{
				sc[i].iBFlag[iTempMax] = 1;
			}
		}

		// From B to A
		for ( k = 0; k < sc[i].iB; k++ )
		{		
			iMax = 3660;	// Max value in minutes
			iTempMax = -1;	// No valid index
			
			for ( j = 0; j < sc[i].iA; j++ )
			{
				if ( sc[i].iAFlag[j] )
				{
					continue;
				}

				if ( sc[i].iBEnd[k] <= sc[i].iAStart[j] )
				{
					if ( iMax > sc[i].iAStart[j] )
					{
						iMax = sc[i].iAStart[j];
						iTempMax = j;
					}
				}
			}

			if ( iTempMax >= 0 )
			{
				sc[i].iAFlag[iTempMax] = 1;
			}

		}
	}

	// Now calculate the trips for A to B
	for ( i = 0; i < iTotalCases; i++ )
	{
		for ( j = 0; j < sc[i].iA; j++ )
		{
			if ( sc[i].iAFlag[j] == 0 )
			{
				sc[i].iAtoBTrips++;
			}
		}

		for ( k = 0; k < sc[i].iB; k++ )
		{
			if ( sc[i].iBFlag[k] == 0 )
			{
				sc[i].iBtoATrips++;
			}
		}
	}

}

void GetNextLine()
{
	for ( iLastPos = iCurrentPos; pBuf[iCurrentPos] != '\n' ; iCurrentPos++ );

	memset( szDummy, 0, 200 );
	strncpy( szDummy, pBuf + iLastPos, iCurrentPos - iLastPos );
	iCurrentPos++;
}

void GetCase( int iCaseNumber )
{
	// Get the turn around time
	GetNextLine();
	iTurnAroundTime = atoi( szDummy );

	// Get the S count first
	GetNextLine();

	char szNA[3] = "\0";
	char szNB[3] = "\0";

	for ( unsigned int i = 0; i < strlen( szDummy ); i++ )
	{
		if ( szDummy[i] != ' ' )
		{
			szNA[i] = szDummy[i];
		}
		else
		{
			i++;
			break;
		}
	}

	sc[iCaseNumber].iA = atoi( szNA );

	for ( int j = 0; i < strlen( szDummy ); i++, j++ )
	{
		if ( szDummy[i] != '\n' )
		{
			szNB[j] = szDummy[i];
		}
	}

	sc[iCaseNumber].iB = atoi( szNB );

	int iSH = 0;
	int iSM = 0;
	int iEH = 0;
	int iEM = 0;

	for ( j = 0; j < sc[iCaseNumber].iA; j++ )
	{
		iSH = iSM = iEH = iEM = 0;
		GetNextLine();
		sscanf( szDummy, "%02d:%02d %02d:%02d\n", &iSH, &iSM, &iEH, &iEM );
		sc[iCaseNumber].iAStart[j] = ( iSH * 60 ) + iSM;
		sc[iCaseNumber].iAEnd[j] = ( iEH * 60 ) + iEM + iTurnAroundTime;
	}

	SortArray( sc[iCaseNumber].iAEnd, sc[iCaseNumber].iA );

	for ( j = 0; j < sc[iCaseNumber].iB; j++ )
	{
		iSH = iSM = iEH = iEM = 0;
		GetNextLine();
		sscanf( szDummy, "%02d:%02d %02d:%02d\n", &iSH, &iSM, &iEH, &iEM );
		sc[iCaseNumber].iBStart[j] = ( iSH * 60 ) + iSM;
		sc[iCaseNumber].iBEnd[j] = ( iEH * 60 ) + iEM + iTurnAroundTime;
	}

	SortArray( sc[iCaseNumber].iBEnd, sc[iCaseNumber].iB );
}

void SortArray( int *pArr, int iArrCount )
{
	int i = 0;
	int j = 0;
	int iDummy = 0;

	for ( i = 0; i < iArrCount; i++ )
	{
		for ( j = 1; j < iArrCount; j++ )
		{
			if ( pArr[j -1] > pArr[j] )
			{
				iDummy = pArr[j - 1];
				pArr[j-1] = pArr[j];
				pArr[j] = iDummy;
			}
		}
	}
}