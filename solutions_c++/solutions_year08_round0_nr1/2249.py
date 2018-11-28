// Uni.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <string.h>

int ReadSearchEngines(FILE *fpIn);
int ReadSearchQueries(FILE *fpIn);
void PrintAll();
int OptimiseSearchQuery();
int MaxArray(int optimised[]);

int nSearchEngines, nSearchQueries;
char strSearchEngines[100][1000], strSearchQueries[1000][1000];

int main(int argc, char* argv[])
{
	//printf("Hello World!\n");
	int nSearchQuerySwitchCount = 0;

	FILE *fpIn = fopen("D:\\A-large.in","r");
	if ( fpIn == NULL )
		return 0;

	FILE *fpOut = fopen("D:\\A.out","w");


	char strIn[1000];
	fgets( strIn, 1000, fpIn );
	if ( feof(fpIn) ) return 0;
	int inputCases = atoi(strIn);

	for ( int i=0; i<inputCases; i++ )
	{
		ReadSearchEngines(fpIn);
		ReadSearchQueries(fpIn);

		PrintAll();

		nSearchQuerySwitchCount = OptimiseSearchQuery();
		printf( "\nSearch query switches count = %d\n", nSearchQuerySwitchCount );
		
		fprintf( fpOut, "Case #%d: %d\n", i+1, nSearchQuerySwitchCount );
		
	}

/*	while( !feof(fpIn) )
	{
		fgets( strIn, 1000, fpIn );
		if ( feof(fpIn) )
			break;
		printf( "%s", strIn );
	}
*/
	fclose(fpIn);
	fclose(fpOut);

	return 0;
}

int ReadSearchEngines(FILE *fpIn)
{
	char strIn[1000];
	fgets( strIn, 1000, fpIn );
	if ( feof(fpIn) ) return 0;
	
	nSearchEngines = atoi(strIn);
	for ( int i=0; i<nSearchEngines; i++ )
	{
		fgets( strIn, 1000, fpIn );
		if ( feof(fpIn) ) return 0;

		strIn[strlen(strIn)-1]='\0';
		strcpy( strSearchEngines[i], strIn );
	}

	return 1;
}


int ReadSearchQueries(FILE *fpIn)
{
	char strIn[1000];
	fgets( strIn, 1000, fpIn );
	if ( feof(fpIn) ) return 0;
	
	nSearchQueries = atoi(strIn);
	for ( int i=0; i<nSearchQueries; i++ )
	{
		fgets( strIn, 1000, fpIn );
		if ( feof(fpIn) ) return 0;
		strIn[strlen(strIn)-1]='\0';
		strcpy( strSearchQueries[i], strIn );
	}

	return 1;
}


void PrintAll()
{
	printf("\n\n==================================");
	for ( int i=0; i<nSearchEngines; i++ )
	{
		printf("\n%s", strSearchEngines[i]);
	}

	printf("\n**********************************");
	for ( i=0; i<nSearchQueries; i++ )
	{
		printf("\n%s", strSearchQueries[i]);
	}

}

int OptimiseSearchQuery()
{
	int optimised[100];
	int nSearchQuerySwitchCount = 0;

	for ( int qFull=0; qFull<nSearchQueries; qFull++ )
	{

		for ( int i=0; i<100; i++ ) 	optimised[i] = 0;

		for ( int s=0; s<nSearchEngines; s++ )
		{
			for ( int q=qFull; q<nSearchQueries; q++ )
			{
				if ( stricmp(strSearchEngines[s], strSearchQueries[q]) != 0 )
					optimised[s]++;
				else
					break;
			}
		}

		int optimisedEngineIndex = MaxArray(optimised);
		printf("\nOptimised index = %d, count=%d", optimisedEngineIndex, optimised[optimisedEngineIndex] );
		qFull = qFull + optimised[optimisedEngineIndex]-1;
		nSearchQuerySwitchCount++;
	}

	if ( nSearchQuerySwitchCount > 0 )
		nSearchQuerySwitchCount--;

	return nSearchQuerySwitchCount;
}

int MaxArray(int optimised[])
{
	int maxIndex = 0;
	for ( int i=0; i<nSearchEngines; i++ )
	{
		if ( optimised[maxIndex] < optimised[i] )
			maxIndex = i;
	}

	return maxIndex;
}
