#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

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

	iCountCases = atoi(strLine);

	int x1;

	char cMap[26];
	cMap[0] = 'y';	//a
	cMap[1] = 'h';	//b
	cMap[2] = 'e';	//c
	cMap[3] = 's';	//d
	cMap[4] = 'o';	//e
	cMap[5] = 'c';	//f
	cMap[6] = 'v';	//g
	cMap[7] = 'x';	//h
	cMap[8] = 'd';	//i
	cMap[9] = 'u';	//j
	cMap[10] = 'i';	//k
	cMap[11] = 'g';	//l
	cMap[12] = 'l';	//m
	cMap[13] = 'b';	//n
	cMap[14] = 'k';	//o
	cMap[15] = 'r';	//p
	cMap[16] = 'z';	//q
	cMap[17] = 't';	//r
	cMap[18] = 'n';	//s
	cMap[19] = 'w';	//t
	cMap[20] = 'j';	//u
	cMap[21] = 'p';	//v
	cMap[22] = 'f';	//w
	cMap[23] = 'm';	//x
	cMap[24] = 'a';	//y
	cMap[25] = 'q';	//z

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ilen = strlen(strLine)-1;
		bool bEndLine;
		
		// algorithm

		
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: ", iCase);
		for (int j=0; j<ilen; j++)
		{
			if (strLine[j]>='a' && strLine[j]<='z')
			{
				int iLetter = (unsigned int)strLine[j]-(unsigned int)'a';
				fprintf(fOutput, "%c", cMap[iLetter]);
			}
			else
				fprintf(fOutput, "%c", strLine[j]);
		}
		fprintf(fOutput, "\n");

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}