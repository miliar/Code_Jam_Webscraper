#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	10000

int iMaxLetters;
int iKeys;
int iLetters;

int iCountLetters[1000];
bool bUsed[1000];

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

int GetMaxLetter()
{
	int imax = 0;
	int iindex = 0;
	for (int i=0; i<iLetters; i++)
	{
		if (iCountLetters[i]>imax && bUsed[i] == false)
		{
			imax = iCountLetters[i];
			iindex = i;
		}
	}
	bUsed[iindex] = true;
	return imax;
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


	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// iMaxLetters
		iMaxLetters = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iKeys = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iLetters = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);

		// counts
		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;

		ipos = 0;
		int j;
		for (j=0; j<iLetters; j++)
		{
			bUsed[j] = false;
			iCountLetters[j] = GetInt(&strLine[ipos], &ilen, &bEndLine);
			ipos += (ilen+1);
		}

		// algorithm

/*		bool bImpossible = false;
		if (iMaxLetters*iKeys < iLetters)
		{
			bImpossible = true;
			iLetters = 0;
		}
*/
		int iCount = 0;
		__int64 iPresses = 0;
		for (j=0; j<iLetters; j++)
		{
			iPresses += GetMaxLetter() * (iCount / iKeys + 1);
			iCount++;
		}

		char strZahl[50];
		_i64toa(iPresses, strZahl, 10);
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %s\n", iCase, strZahl);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}