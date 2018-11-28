#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	1000

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

	int j;

	char strLine[MAX_LEN_LINE];
	// read first line
	if (fgets(strLine, MAX_LEN_LINE, fInput)==NULL)
	{
		// Fehler beim Lesen
		return -1;
	}

	iCountCases = atoi(strLine);

	char combine[36][3];
	char opposed[28][2];
	int iCountCombine;
	int iCountOpposed;

	char strList[101];
	int iListLen;
	char strC[5];

	char ResultList[101];
	int iResultLen;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;

		iCountCombine = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		
		for (j=0; j<iCountCombine; j++)
		{
			GetString(&strLine[ipos], strC, &ilen, &bEndLine);
			ipos += (ilen+1);
			combine[j][0] = strC[0];
			combine[j][1] = strC[1];
			combine[j][2] = strC[2];
		}
		
		iCountOpposed = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		for (j=0; j<iCountOpposed; j++)
		{
			GetString(&strLine[ipos], strC, &ilen, &bEndLine);
			ipos += (ilen+1);
			opposed[j][0] = strC[0];
			opposed[j][1] = strC[1];
		}

		iListLen = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		GetString(&strLine[ipos], strList, &ilen, &bEndLine);
		ipos += (ilen+1);


		// algorithm
		iResultLen = 0;

		for (j=0; j<iListLen; j++)
		{
			ResultList[iResultLen] = strList[j];
			iResultLen++;

			if (iResultLen>1)
			{
				bool bCombined = false;
				// nach combine prüfen
				for (int iCo=0; iCo<iCountCombine; iCo++)
				{
					if (ResultList[iResultLen-1]==combine[iCo][0])
					{
						if (ResultList[iResultLen-2]==combine[iCo][1])
						{
							iResultLen--;
							ResultList[iResultLen-1] = combine[iCo][2];
							iCo = iCountCombine;
							bCombined = true;
						}
					}
					else if (ResultList[iResultLen-1]==combine[iCo][1])
					{
						if (ResultList[iResultLen-2]==combine[iCo][0])
						{
							iResultLen--;
							ResultList[iResultLen-1] = combine[iCo][2];
							iCo = iCountCombine;
							bCombined = true;
						}
					}
				}
				
				// opposed prüfen
				if (!bCombined)
				{
					bool bHit;
					char cOpposed;
					for (int iOp=0; iOp<iCountOpposed; iOp++)
					{
						bHit = false;
						if (ResultList[iResultLen-1]==opposed[iOp][0])
						{
							bHit = true;
							cOpposed = opposed[iOp][1];
						}
						else if (ResultList[iResultLen-1]==opposed[iOp][1])
						{
							bHit = true;
							cOpposed = opposed[iOp][0];
						}

						// Liste bis vorletztes durchsuchen nach cOpposed
						if (bHit)
						{
							for (int l=0; l<iResultLen-1; l++)
							{
								if (ResultList[l]==cOpposed)
								{
									iResultLen = 0;
									iOp = iCountOpposed;
								}
							}
						}
					}
				}
			}
		}
		
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: [", iCase);
		for (j=0; j<iResultLen; j++)
		{
			if (j==iResultLen-1)
				fprintf(fOutput, "%c", ResultList[j]);
			else
				fprintf(fOutput, "%c, ", ResultList[j]);
		}		
		
		fprintf(fOutput, "]\n");

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}