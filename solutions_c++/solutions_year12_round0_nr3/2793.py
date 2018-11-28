#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	100

int GetInt(char *str, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	char strZahl[20];
	strncpy(strZahl, str, ipos);
	strZahl[ipos] = 0;
	int iResult = atoi(strZahl);
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
	return iResult;
}
double GetDouble(char *str, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	char strZahl[50];
	strncpy(strZahl, str, ipos);
	strZahl[ipos] = 0;
	double dResult = atof(strZahl);
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
	return dResult;
}
void GetString(char *str,char *strOut, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	strncpy(strOut, str, ipos);
	strOut[ipos] = 0;
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
}



int main(int argv, char *argc[])
{
	if (argv < 2)
		return -1;
	

	int iCountCases = 0;
	
	// read Input
	FILE *fInput = fopen(argc[1], "r");
	if (fInput == NULL)
		return -1;

	// output
	FILE *fOutput = fopen("output.txt", "w");
	if (fOutput == NULL)
	{
		fclose(fInput);
		return -1;
	}


	char strLine[MAX_LEN_LINE];
	// read first line
	if (fgets(strLine, MAX_LEN_LINE, fInput)==NULL)
	{
		// Fehler beim Lesen
		return -1;
	}

	iCountCases = atoi(strLine);

	int j;
	int iA;
	int iB;
	int iMerk[6];
	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// x1
		iA = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iB = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		
		// algorithm
		int iResult = 0;
		int iDigits = 0;
		int iFaktor = 1;
		int iTest = iA;
		while (iTest>0)
		{
			iDigits++;
			iTest /= 10;
		}
		for (j=1; j<iDigits; j++)
			iFaktor *= 10;
		for (j=iA; j<=iB; j++)
		{
			iTest = j;
			for (int m=0; m<iDigits-1; m++)
			{
				int iRest = iTest % 10;
				iTest = iTest / 10 + iRest*iFaktor;
				iMerk[m] = iTest;
				if (iTest>j && iTest<=iB)
				{
					bool bDouble = false;
					for (int n=0; n<m; n++)
						if (iTest==iMerk[n])
							bDouble = true;
					if (!bDouble)
						iResult++;
					//fprintf(fOutput, "%d: %d %d\n", iResult, j, iTest);
				}
			}
		}

		
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iResult);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}