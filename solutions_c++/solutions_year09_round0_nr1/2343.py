#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	10000

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

	int ipos = 0;
	int ilen = 0;
	bool bEndLine;
	int iWordlen = GetInt(&strLine[ipos], &ilen, &bEndLine);
	ipos += ilen+1;
	int iWords = GetInt(&strLine[ipos], &ilen, &bEndLine);
	ipos += ilen+1;
	iCountCases = GetInt(&strLine[ipos], &ilen, &bEndLine);

	int i, j;

	char *cWordLetter = new char[5000*26];

	int *iListe = new int[15*26*5000];
	int *iLens = new int[15*26];
	for (i=0; i<15; i++)
		for (j=0; j<26; j++)
			iLens[i*26+j] = 0;

	for (i=0; i<iWords; i++)
	{
		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		for (j=0; j<iWordlen; j++)
		{
			unsigned int iLetter = (unsigned int)(strLine[j]-'a');
			cWordLetter[i*26+j] = strLine[j];
			iListe[j*26*5000+iLetter*5000+iLens[j*26+iLetter]] = i;
			iLens[j*26+iLetter]++;
		}
	}

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int iMatches[5000];
		for (j=0; j<iWords; j++)
			iMatches[j] = j;
		int iLenMatch = iWords;

		
		int iMatches2[5000];
		int iLenMatch2 = 0;
		int ipos = 0;
		int iLetterPos = 0;
		bool bInKlammer = false;
		do
		{
			if (strLine[ipos]=='(')
			{
				bInKlammer = true;
			}
			else if (strLine[ipos]==')')
			{
				bInKlammer = false;
				iLetterPos++;
			}
			else
			{
				// Buchstaben untersuchen
				unsigned int iLetter = (unsigned int)(strLine[ipos]-'a');
				for (j=0; j<iLens[iLetterPos*26+iLetter]; j++)
				{
					int iW = iListe[iLetterPos*26*5000+iLetter*5000+j];

					for (int k=0; k<iLenMatch; k++)
					{
						if (iW==iMatches[k])
						{
							iMatches2[iLenMatch2] = iW;
							iLenMatch2++;
						}
					}
				}
				
				if (bInKlammer==false)
					iLetterPos++;
			}
			
			if (bInKlammer==false)
			{
				// Matches2 auf Matches 1 übertragen
				for (j=0; j<iLenMatch2; j++)
					iMatches[j] = iMatches2[j];
				iLenMatch = iLenMatch2;
				iLenMatch2 = 0;
			}
			ipos++;
		}while (iLetterPos<iWordlen && iLenMatch>0);

		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iLenMatch);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}