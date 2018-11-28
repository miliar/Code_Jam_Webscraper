#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	100

int n;
int v1[800];
int v2[800];

bool b1[800];
bool b2[800];

int iSkalar;


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


int GetMinv1()
{
	int imin = 100000;
	int iindex = 0;
	for (int i=0; i<n; i++)
	{
		if (v1[i]<imin && b1[i]==false)
		{
			imin = v1[i];
			iindex = i;
		}
	}
	b1[iindex] = true;
	return imin;
}


int GetMaxv2()
{
	int imax = -100000;
	int iindex = 0;
	for (int i=0; i<n; i++)
	{
		if (v2[i]>imax && b2[i]==false)
		{
			imax = v2[i];
			iindex = i;
		}
	}
	b2[iindex] = true;
	return imax;
}


int main(int argv, char *argc[])
{
	if (argv < 2)
		return -1;
	
	int i, j;

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
	for (i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// n
		n = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);


		// v1
		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		ipos = 0;
		for (j=0; j<n; j++)
		{
			v1[j] = GetInt(&strLine[ipos], &ilen, &bEndLine);
			b1[j] = false;
			ipos += (ilen+1);
		}
		// v2
		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		ipos = 0;
		for (j=0; j<n; j++)
		{
			v2[j] = GetInt(&strLine[ipos], &ilen, &bEndLine);
			b2[j] = false;
			ipos += (ilen+1);
		}


		// algorithm
		iSkalar = 0;
		for (j=0; j<n; j++)
		{
			iSkalar += (GetMinv1() * GetMaxv2());
		}
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iSkalar);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}