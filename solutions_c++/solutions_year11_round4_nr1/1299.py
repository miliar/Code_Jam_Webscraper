#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_LEN_LINE	200

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

	int iLenW[100];

	iCountCases = atoi(strLine);

	int x1;
	int iSumW;
	double dRestRun;

	double dResult;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;

		iSumW = 0;
		for (int j=0; j<100; j++)
			iLenW[j] = 0;
		int iX = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		int iVs = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		int iVr = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		int iT = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		int iN = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		for (int iwalk=0; iwalk<iN; iwalk++)
		{
			fgets(strLine, MAX_LEN_LINE, fInput);
			ipos = 0;
			int iBegin = GetInt(&strLine[ipos], &ilen, &bEndLine);
			ipos += (ilen+1);
			int iEnd = GetInt(&strLine[ipos], &ilen, &bEndLine);
			ipos += (ilen+1);
			iSumW += iEnd-iBegin;
			int iSpeedW = GetInt(&strLine[ipos], &ilen, &bEndLine);
			ipos += (ilen+1);
			iLenW[iSpeedW-1] += iEnd - iBegin;
		}
		
		// algorithm
		dRestRun = (double)iT;
		dResult = 0.0;
		double dTimeWalk = (double)(iX - iSumW)/(double)iVr;
		bool bRestRun = true;
		if (dTimeWalk >= dRestRun)
		{
			double dWRun = (double)iVr * dRestRun;
			dResult += dRestRun;
			dResult += ((double)(iX-iSumW)-dWRun) / (double)iVs;
			bRestRun = false;
		}
		else
		{
			dResult += dTimeWalk;
			dRestRun -= dTimeWalk;
		}
		int iposW = 0;
		while (bRestRun)
		{
			dTimeWalk = (double)(iLenW[iposW])/(double)(iVr+iposW+1);
			if (dTimeWalk >= dRestRun)
			{
				double dWRun = (double)(iVr+iposW+1) * dRestRun;
				dResult += dRestRun;
				dResult += ((double)(iLenW[iposW])-dWRun) / (double)(iVs+iposW+1);
				bRestRun = false;
			}
			else
			{
				dResult += dTimeWalk;
				dRestRun -= dTimeWalk;
			}
			iposW++;
			if (iposW==100)
				bRestRun = false;
		}
		for (int j=iposW; j<100; j++)
		{
			dResult += ((double)(iLenW[j]) / (double)(iVs+j+1));
		}
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %.9f\n", iCase, dResult);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}