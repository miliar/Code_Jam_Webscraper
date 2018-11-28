#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	2000

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

	int iCount;
	int iPositions[100];
	int iWho[100];
	int iPosO;
	int iPosB;
	int iLastActionO;
	int iLastActionB;
	int iTime;

	char strWho[5];

	int j;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		
		iCount = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		for (j=0; j<iCount; j++)
		{
			GetString(&strLine[ipos], strWho, &ilen, &bEndLine);
			ipos += (ilen+1);
			if (strWho[0]=='O')
				iWho[j] = 0;
			else
				iWho[j] = 1;
			iPositions[j] = GetInt(&strLine[ipos], &ilen, &bEndLine);
			ipos += (ilen+1);
		}
		
		// algorithm
		iPosO = 1;
		iPosB = 1;
		iLastActionO = 0;
		iLastActionB = 0;
		iTime = 0;
		for (j=0; j<iCount; j++)
		{
			if (iWho[j]==0)
			{
				int iWay = abs(iPositions[j] - iPosO);
				int iBefore = iTime - iLastActionO;
				int iNewTime = iWay - iBefore;
				if (iNewTime<0)
					iNewTime = 0;
				iTime += iNewTime + 1;
				iLastActionO = iTime;
				iPosO = iPositions[j];
			}
			else
			{
				int iWay = abs(iPositions[j] - iPosB);
				int iBefore = iTime - iLastActionB;
				int iNewTime = iWay - iBefore;
				if (iNewTime<0)
					iNewTime = 0;
				iTime += iNewTime + 1;
				iLastActionB = iTime;
				iPosB = iPositions[j];
			}
		}
		
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iTime);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}