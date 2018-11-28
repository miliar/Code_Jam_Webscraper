#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	100
int iDigits[40];
int iCount;

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

bool IsUgly(char *str, int len)
{
	__int64 iResult = 0;
	bool bEnd = false;
/*	unsigned __int64 iloop = 1;
	for (int i=0; i<len-1; i++)
		iloop *= 3;
	while (iloop>0)
	{
*/
	unsigned __int64 iZw = iDigits[0];;	
	bool bplus = true;
	for (int i=0; i<len-1; i++)
	{
		if (str[i]=='1')
			iZw = iZw*10 + iDigits[i+1];
		if (str[i]=='2')
		{
			if (bplus)
				iResult += iZw;
			else
				iResult -= iZw;
			bplus = true;
			iZw = iDigits[i+1];
		}
		if (str[i]=='3')
		{
			if (bplus)
				iResult += iZw;
			else
				iResult -= iZw;
			bplus = false;
			iZw = iDigits[i+1];
		}
	}

	if (bplus)
		iResult += iZw;
	else
		iResult -= iZw;

	if (iResult<0)
		iResult = -iResult;
	if (iResult%2==0 || iResult%3==0 || iResult%5==0 || iResult%7==0)
		return true;
	else
		return false;
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
		while (strLine[ipos]!= '\n')
		{
			char strZahl[2];
			strZahl[0] = strLine[ipos];
			strZahl[1] = 0;
			iDigits[ipos] = atoi(strZahl);
			ipos++;
		}
		iCount = ipos;
		
		// algorithm
		char str[39];
		for (int j=0; j<39; j++)
			str[j] = '1';
		
		int iResult = 0;
		__int64 iloop = 1;
		for (int i=0; i<iCount-1; i++)
			iloop *= 3;
		while (iloop>0)
		{
			if (IsUgly(str, iCount))
				iResult++;

			char c = str[0];
			
			int iStelle = 0;
			while (iStelle<40 && c=='3')
			{
				str[iStelle] = '1';
				iStelle++;
				c = str[iStelle];
			}
			if (str[iStelle]=='2')
				str[iStelle] = '3';
			if (str[iStelle]=='1')
				str[iStelle] = '2';

			iloop--;
		}

		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iResult);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}