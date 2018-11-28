#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LEN_OF_ONE_LINE_IN_A_FILE 1024
#define MAX_LEN_OF_ONE_OUTPUT_LINE 40
#define NUM_OF_LINES_PER_TESTCASE 1

#define TRUE 1
#define FALSE 0
#define ON 1
#define OFF 0

/* Line to store one line at a time from the input File... */
char oneLineFromFile[MAX_LEN_OF_ONE_LINE_IN_A_FILE];
char outputString[MAX_LEN_OF_ONE_OUTPUT_LINE];

/* Read a line from Input File & Prepare a string [oneLineFromFile]*/
void ReadOneLineFromFile(FILE* inputFile)
{
	fgets(oneLineFromFile, MAX_LEN_OF_ONE_LINE_IN_A_FILE, inputFile);
}

/* Fetch next nuber from Line [oneLineFromFile]*/
long NextNumFromLine(int isFirstTimeForThisLine)
{
	static char* readStart;
	long val = 0;	
	char * endptr;
	
	if (isFirstTimeForThisLine)
	{
		readStart = oneLineFromFile;
	}

	val = strtol(readStart, &endptr, 10);
	readStart = endptr + 1;

	return val;
}

long NumberOfTestCases(FILE* inputFile)
{
	ReadOneLineFromFile(inputFile);
	return NextNumFromLine(TRUE);
}

void RefreshOutputString()
{
	memset(outputString,'\0',MAX_LEN_OF_ONE_OUTPUT_LINE);
}


/****************To be configured for each problem ********************/

/* Input Data */
int numSnappers;
int numSnaps;
char output[2][5] = {"OFF", "ON"};

void ReadTestCaseGenerateInputData(FILE* inputFile)
{	
	ReadOneLineFromFile(inputFile);

	numSnappers = NextNumFromLine(TRUE);
	numSnaps = NextNumFromLine(FALSE);
}

int ProcessInputGenerateOutput()
{
	int allOnWithPower = (1 << numSnappers) - 1;
	int on = numSnaps & allOnWithPower;
	
	if (on == allOnWithPower)
		return ON;
	return OFF;
}

void GenerateOutPutStringAndWritetoFile(FILE* outputFile,int currentTestCase)
{
	RefreshOutputString();
	sprintf(outputString,"Case #%d: %s\n",currentTestCase,output[ProcessInputGenerateOutput()]);
	fputs(outputString,outputFile);
}


int main(int argc, char* argv[])
{
	long numberOfTestCases;
	long looopVar;
	FILE* inputFile = NULL;
	FILE* outputFile = NULL;
	
	inputFile = fopen(argv[1],"r");
	outputFile = fopen(argv[2],"w");

	numberOfTestCases = NumberOfTestCases(inputFile);

	for (looopVar = 0; looopVar < numberOfTestCases; looopVar++)
	{
		ReadTestCaseGenerateInputData(inputFile);
		GenerateOutPutStringAndWritetoFile(outputFile,looopVar + 1);
	}
	
	fclose(outputFile);
	fclose(inputFile);	
	return 0;

}
