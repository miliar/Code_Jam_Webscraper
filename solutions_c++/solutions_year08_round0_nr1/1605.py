// GCJSU.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <io.h>
#include <fcntl.h>
#include <sys/stat.h>

#define MAX_CASE_COUNT		20
#define MAX_S_COUNT			100
#define MAX_Q_COUNT			1000
#define MAX_S_LENGTH		100

typedef struct _tagSCase
{
	int		iSCount;
	char	szS[MAX_S_COUNT][MAX_S_LENGTH];
	int		iSTotalInQ[MAX_S_COUNT];
	//int		iSLocationList[MAX_S_COUNT][MAX_Q_COUNT];

	int		iQCount;
	char	szQ[MAX_Q_COUNT][MAX_S_LENGTH];
	int		iQLocation[MAX_Q_COUNT];

	int		iSwitchCount;

}SCase, *PCase;

// Global variables
int iTotalCases = 0;;
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

int main(int argc, char* argv[])
{
	memset( &sc, '\0', sizeof( SCase ) * MAX_CASE_COUNT );

	int iRetVal = ReadInputFile();
	if ( iRetVal < 0 )	return -1;

	BuildCases();

	for ( int i = 0; i < iTotalCases; i++ )
	{
		printf( "\nCase %d: %d", i + 1, sc[i].iSwitchCount );
	}

	int fd = _open( "A-large.out", _O_WRONLY | _O_BINARY | _O_CREAT, _S_IWRITE );
	if ( fd == -1 )
	{
		printf( "Unable to create output file, please check your path" );
		return -1;
	}

	for ( i = 0; i < iTotalCases; i++ )
	{
		sprintf( szDummy, "Case #%d: %d\n", i + 1, sc[i].iSwitchCount );
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
	char szInputFile[] = "A-large.in";
	
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
		for ( j = 0; j < sc[i].iQCount; j++ )
		{
			for ( k = 0; k < sc[i].iSCount; k++ )
			{
				if ( strcmp( sc[i].szQ[j], sc[i].szS[k] ) == 0 )
				{
					sc[i].iQLocation[j] = k;
					break;
				}
			}
		}
	}

	// Calculate number of switches for each case
	for ( i = 0; i < iTotalCases; i++ )
	{
		for ( j = 0; j < sc[i].iQCount; j++ )
		{
			iTempMax = 0;
			for ( k = 0; k < sc[i].iSCount; k++ )
			{
				if ( sc[i].iSTotalInQ[k] )
				{
					iTempMax++;
				}
			}

			if ( iTempMax == sc[i].iSCount )
			{
				// It is time to switch, so increment
				sc[i].iSwitchCount++;

				// Reset the counter except last
				for ( k = 0; k < sc[i].iSCount; k++ )
				{
					if ( k != iLast )
					{
						sc[i].iSTotalInQ[k] = 0;
					}
				}
			}
			sc[i].iSTotalInQ[ sc[i].iQLocation[j] ] = 1;
			iLast = sc[i].iQLocation[j];
		}
		
		iTempMax = 0;
		for ( k = 0; k < sc[i].iSCount; k++ )
		{
			if ( sc[i].iSTotalInQ[k] )
			{
				iTempMax++;
			}
		}
		
		if ( iTempMax == sc[i].iSCount )
		{
			// It is time to switch, so increment
			sc[i].iSwitchCount++;
		}
	}
	
	/*
	// Count the S in the QLocation and prepare list of 
	for ( i = 0; i < iTotalCases; i++ )
	{
		for ( j = 0; j < sc[i].iQCount; j++ )
		{
			k = sc[i].iQLocation[j] - 1;
			
			sc[i].iSLocationList[k][ sc[i].iSTotalInQ[k] ] = j + 1;
			sc[i].iSTotalInQ[k]++;
		}
	}



	// Calculate the switch count in every case
	for ( i = 0; i < iTotalCases; i++ )
	{
		bTakeBreak = false;
		for ( j = 0; j < sc[i].iSCount; j++ )
		{
			if ( sc[i].iSTotalInQ[j] == 0 )
			{
				// We have turminating condition
				bTakeBreak = true;;
			}
		}

		if ( bTakeBreak )
		{
			// goto next case directly
			continue;
		}

		// If we reach here means that we do not have any other option
		// but to serach in the location list
		iMax = 0;
		iTempMax = 0;
		bTakeBreak = false;

		for ( k = 0; k < MAX_Q_COUNT; k++ )
		{
			for ( j = 0; j < sc[i].iSCount; j++ )
			{
				bFound = false;

				for ( l = 0; l < sc[i].iSTotalInQ[j]; l++ )
				{
					if ( iMax < sc[i].iSLocationList[j][l] )
					{
						bFound = true;
						
						if ( iTempMax < sc[i].iSLocationList[j][l] )
						{
							iTempMax = sc[i].iSLocationList[j][l];
						}
						break;
					}
				}
				
				if ( bFound == false )
				{
					bTakeBreak = true;
					break;
				}
			}

			if ( bTakeBreak )
			{
				break;
			}
			
			iMax = iTempMax;

			// If we reach here, that means we have to take one switch
			// so increase the switch count
			sc[i].iSwitchCount++;
		}
	}
	*/
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
	// Get the S count first
	GetNextLine();
	sc[iCaseNumber].iSCount = atoi( szDummy );

	for ( int i = 0; i < sc[iCaseNumber].iSCount; i++ )
	{
		GetNextLine();
		strcpy( sc[iCaseNumber].szS[i], szDummy );
	}

	// Get the Q count 
	GetNextLine();
	sc[iCaseNumber].iQCount = atoi( szDummy );

	for ( i = 0; i < sc[iCaseNumber].iQCount; i++ )
	{
		GetNextLine();
		strcpy( sc[iCaseNumber].szQ[i], szDummy );
	}
}