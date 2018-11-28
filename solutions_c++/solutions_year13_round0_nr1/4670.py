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

	char cField[4][4];
	int iResult;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		for (int iRow=0; iRow<4; iRow++)
		{
			fgets(strLine, MAX_LEN_LINE, fInput);
			for (int iCol=0; iCol<4; iCol++)
			{
				cField[iRow][iCol] = strLine[iCol];
			}
		}
		fgets(strLine, MAX_LEN_LINE, fInput);

		// algorithm
		iResult = 0;

		int iSumPoint = 0;
		// rows
		for (int iRow=0; iRow<4; iRow++)
		{
			int iSumX = 0;
			int iSumO = 0;
			for (int iCol=0; iCol<4; iCol++)
			{
				if (cField[iRow][iCol]=='X' || cField[iRow][iCol]=='T')
					iSumX++;
				if (cField[iRow][iCol]=='O' || cField[iRow][iCol]=='T')
					iSumO++;
				if (cField[iRow][iCol]=='.')
					iSumPoint++;
			}
			if (iSumX==4)
				iResult = 1;
			else if (iSumO==4)
				iResult = 2;
		}

		// cols
		if (iResult==0)
		{
			for (int iCol=0; iCol<4; iCol++)
			{
				int iSumX = 0;
				int iSumO = 0;
				for (int iRow=0; iRow<4; iRow++)
				{
					if (cField[iRow][iCol]=='X' || cField[iRow][iCol]=='T')
						iSumX++;
					if (cField[iRow][iCol]=='O' || cField[iRow][iCol]=='T')
						iSumO++;
				}
				if (iSumX==4)
					iResult = 1;
				else if (iSumO==4)
					iResult = 2;
			}
		}
		
		if (iResult==0)
		{
			int iSumX1 = 0;
			int iSumX2 = 0;
			int iSumO1 = 0;
			int iSumO2 = 0;
			for (int iDiag=0; iDiag<4; iDiag++)
			{
				if (cField[iDiag][iDiag]=='X' || cField[iDiag][iDiag]=='T')
					iSumX1++;
				if (cField[iDiag][iDiag]=='O' || cField[iDiag][iDiag]=='T')
					iSumO1++;
				if (cField[iDiag][3-iDiag]=='X' || cField[iDiag][3-iDiag]=='T')
					iSumX2++;
				if (cField[iDiag][3-iDiag]=='O' || cField[iDiag][3-iDiag]=='T')
					iSumO2++;
			}
			if (iSumX1==4 || iSumX2==4)
				iResult = 1;
			else if (iSumO1==4 || iSumO2==4)
				iResult = 2;
		}
		
		
		// Ausgabe
		if (iResult==1)
			fprintf(fOutput, "Case #%d: X won\n", iCase);
		else if (iResult==2)
			fprintf(fOutput, "Case #%d: O won\n", iCase);
		else if (iSumPoint>0)
			fprintf(fOutput, "Case #%d: Game has not completed\n", iCase);
		else
			fprintf(fOutput, "Case #%d: Draw\n", iCase);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}