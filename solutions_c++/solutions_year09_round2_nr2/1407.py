// Problem1.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N;
char initNumber[30] = "0 ";
long int nextNumber;

int digits[10], newDigits[10];

void SolveCase()
{
	int found = 0;
	long int intInitNumber;
	int i;

	sscanf(initNumber, "%d", &intInitNumber);

	nextNumber = intInitNumber;

	memset(digits, 0, sizeof(digits));

	// Contar los dígitos del primer número
	for (i=0; i<strlen(initNumber); i++)
		digits[ initNumber[i] - '0' ] += 1;

	while (!found)
	{
		nextNumber++;

		char strNumber[30];

		// Contar los dígitos del número que estamos probando
		sprintf(strNumber, "%ld", nextNumber);
		
		memset(newDigits, 0, sizeof(digits));

		for (i=0; i<strlen(strNumber); i++)
			newDigits[ strNumber[i] - '0' ] += 1;

		// Comparar si son iguales
		if (memcmp(&digits[1], &newDigits[1], 36) == 0)
			found = 1;
	}

}

int main()
{
	int testCase;
    FILE *inFile, *outFile;
    
    inFile = fopen("input.txt", "rt");
    outFile = fopen("output.txt", "wt");

    fscanf(inFile, "%d", &N);

    for (testCase=1; testCase<=N; testCase++)
    {
		fscanf(inFile, "%s", initNumber);

		SolveCase();

        fprintf(outFile, "Case #%d: %ld\n", testCase, nextNumber);
    }
    
    fclose(outFile);
    fclose(inFile);

	return 0;
}

