#include <stdlib.h>
#include <stdio.h>
#include <math.h>


int main()
{
	char acInputFile[255], acOutputFile[255];
	FILE *pInputFile, *pOutputFile;

	int iT; // Number of test cases
	int iK; // Number of fingure snappings
	int iN; // Bulb number

	char* pcResult;

	
	sprintf( acInputFile, "%s.in", "A-large");
	sprintf( acOutputFile, "%s.out",  "A-large");
	

	pInputFile = fopen(acInputFile,"r");
	if(pInputFile == 0)
	{
		printf("Error..Can't open input file: %s", acInputFile);
		return -1;
	}

	pOutputFile = fopen(acOutputFile,"w");
	if(pInputFile == 0)
	{
		printf("Error..Can't write to output file: %s", acOutputFile);
		return -1;
	}

	fscanf(pInputFile,"%d",&iT);
	int temp;
	for(int i = 1; i <= iT ; i++)
	{
		fscanf(pInputFile, "%d", &iN);
		fscanf(pInputFile, "%d", &iK);
	
		temp =(int)(pow(2.0,iN) - 1);

		pcResult = ((iK & temp) == temp)? "ON" : "OFF";
		fprintf(pOutputFile,"Case #%d: %s\n", i, pcResult);
	}
	return 0;
}