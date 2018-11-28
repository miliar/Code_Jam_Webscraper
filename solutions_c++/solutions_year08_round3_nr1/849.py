// Round1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


void PrintAll();
void processInput( char *strIn );
long unsigned int ReadLine1(FILE *fpIn);
long unsigned int ReadLine2(FILE *fpIn);
long unsigned int OptimiseKeySwitch();
void sort();

long unsigned int nMaxLettersperKey, nNoofKeys, nTotalsLetters, nLetter[1000], nKeyPresses[1000];
char strnMaxLettersperKey[1000], strNoofKeys[1000][1000];


int main(int argc, char* argv[])
{
	char strIn[1000];
	//char strOut[1000];
	long unsigned int nKeySwitchCount;

	FILE *fpIn = fopen("D:\\A-small-attempt0.in.txt", "r");
	if ( fpIn==NULL )
	{
		printf("File read error");
		return 0;
	}

	FILE *fpOut = fopen("D:\\A.out", "w");


	fgets( strIn, 1000, fpIn );
	if ( feof(fpIn) ) return 0;
	long unsigned int inputCases = atoi(strIn);


	for ( long unsigned int i=0; i<inputCases; i++ )
	{
		ReadLine1(fpIn);
		ReadLine2(fpIn);


		nKeySwitchCount = OptimiseKeySwitch();
		PrintAll();

		printf( "\nKey switches count = %d\n", nKeySwitchCount );
		
		fprintf( fpOut, "Case #%d: %d\n", i+1, nKeySwitchCount );
		
	}


	//fputs( strOut, fpOut );
	fclose(fpIn);
	fclose( fpOut );

	return 0;
}

long unsigned int OptimiseKeySwitch()
{
	long unsigned int nCount=0;

	if ( nTotalsLetters == 0 )
		return 0;

	sort();

	long unsigned int i, j, indexLetter=0;

	for ( i=0; i<nMaxLettersperKey; i++ )
	{
		for ( j=0; j<nNoofKeys; j++ )
		{
			nKeyPresses[indexLetter] = i+1;
			indexLetter++;
		}
	}


	for ( i=0; i<nTotalsLetters; i++ )
	{
		nCount += nKeyPresses[i] * nLetter[i];
	}


	return nCount;
}

long unsigned int ReadLine1(FILE *fpIn)
{
	fscanf( fpIn, "%d %d %d\n", &nMaxLettersperKey, &nNoofKeys, &nTotalsLetters);
	if ( feof(fpIn) ) return 0;

	return 1;
}


long unsigned int ReadLine2(FILE *fpIn)
{
	char strIn[1000];
	fgets( strIn, 1000, fpIn );
	if ( feof(fpIn) ) return 0;

	if ( nTotalsLetters == 0 )
		return 1;

	char *strLetter = strtok( strIn, " " );
	nLetter[0] = atoi( strLetter );
	for ( long unsigned int i=1; i<nTotalsLetters; i++ )
	{
		strLetter = strtok( NULL, " " );
		nLetter[i] = atoi( strLetter );
	}

	return 1;
}


void PrintAll()
{
	printf("\n\n==================================");
	printf("\nMax Letters%d \nNo. of Keys=%d \nTotal Letters=%d", nMaxLettersperKey, nNoofKeys, nTotalsLetters);

	printf("\n**********************************");
	for ( long unsigned int i=0; i<nTotalsLetters; i++ )
	{
		printf("\nTotalsLetter (%d) = %d, key presses = %d", i, nLetter[i], nKeyPresses[i]);
	}

	printf("\n**********************************");

}

void sort()
{

	long unsigned int temp;
	for ( long unsigned int i=0; i<nTotalsLetters; i++ )
	{
		for ( long unsigned int j=i+1; j<nTotalsLetters; j++ )
		{
			if ( nLetter[i]<nLetter[j] )
			{
				temp = nLetter[i];
				nLetter[i] = nLetter[j];
				nLetter[j] = temp;
			}
		}
	}
}