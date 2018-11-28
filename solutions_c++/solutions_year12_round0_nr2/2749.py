#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	500

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


	int iN;
	int iSurprise;
	int iBestResult;
	int iSumResults[100];

	int iResultNormal;
	int iResultSurprise;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iResultNormal = 0;
		iResultSurprise = 0;
		
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// x1
		iN = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iSurprise = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iBestResult = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		for (int j=0; j<iN; j++)
		{
			iSumResults[j] = GetInt(&strLine[ipos], &ilen, &bEndLine);
			ipos += (ilen+1);
		}

		
		// algorithm
		for (int j=0; j<iN; j++)
		{
			int iMin = iSumResults[j] / 3;
			int iRest = iSumResults[j] % 3;
			if (iMin>=iBestResult)
				iResultNormal++;
			else
			{
				int iMin1 = iMin;
				int iMin2 = iMin;
				if (iRest==0)
				{
					if (iSumResults[j]>0)
						iMin2++;
				}
				else
				{
					iMin1++;
					if (iSumResults[j]>1)
						iMin2 += 2;
				}
				if (iMin1>=iBestResult)
					iResultNormal++;
				else if (iMin2>=iBestResult)
					iResultSurprise++;
			}
		}

		int iResult = iResultNormal;
		if (iResultSurprise>iSurprise)
			iResult += iSurprise;
		else
			iResult += iResultSurprise;
		
		
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iResult);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}