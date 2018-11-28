#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE		101

#define MAX_ENGINES			100
#define MAX_QUERYLEN		1000


int iCountSearchEngines;
int iLenQuery;
char strSearchEngines[MAX_ENGINES][MAX_LEN_LINE];
char strQuery[MAX_QUERYLEN][MAX_LEN_LINE];

int GetEngineNumber(char *str)
{
	for (int i=0; i<iCountSearchEngines; i++)
	{
		if (strcmp(str, &strSearchEngines[i][0]) == 0)
			return i;
	}
	return -1;
}

int main(int argv, char *argc[])
{
	if (argv < 2)
		return -1;
	
	int i;

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
	for (iCase=0; iCase<iCountCases; iCase++)
	{
		
		// number of search engines
		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return -1;

		int ipos = 0;
		char strZahl[20];
		while (strLine[ipos] != '\n' && ipos<MAX_LEN_LINE)
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[0], ipos);
		strZahl[ipos] = 0;
		iCountSearchEngines = atoi(strZahl);

		// search engines
		for (i=0; i<iCountSearchEngines; i++)
		{
			if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
				return -1;
			
			ipos = 0;
			while (strLine[ipos] != '\n' && ipos<MAX_LEN_LINE)
			{
				strSearchEngines[i][ipos] = strLine[ipos];
				ipos++;
			}
			strSearchEngines[i][ipos] = 0;
		}

		// query len
		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return -1;

		ipos = 0;
		while (strLine[ipos] != '\n')
		{
			ipos++;
		}
		strncpy(strZahl, strLine, ipos);
		strZahl[ipos] = 0;
		iLenQuery = atoi(strZahl);

		// query
		for (i=0; i<iLenQuery; i++)
		{
			if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
				return -1;
			
			ipos = 0;
			while (strLine[ipos] != '\n' && ipos<MAX_LEN_LINE)
			{
				strQuery[i][ipos] = strLine[ipos];
				ipos++;
			}
			strQuery[i][ipos] = 0;
		}


		// algorythm
		// look for last search engine in query, this is first
		int iPosQuery = 0;
		bool bEnd = false;
		int iSwitches = 0;
		while (iPosQuery < iLenQuery && bEnd==false)
		{
		
			int iEnginePos[MAX_ENGINES];
			for (i=0; i<MAX_ENGINES; i++)
				iEnginePos[i] = 0;

			i = iPosQuery;
			while (i<iLenQuery)
			{
				int inr = GetEngineNumber(&strQuery[i][0]);
				if (iEnginePos[inr] == 0)			
					iEnginePos[inr] = i+1;
				i++;
			}

			int imax = 0;
			int iMaxEngine = 0;
			for (i=0; i<iCountSearchEngines; i++)
			{
				if (iEnginePos[i] == 0)
				{
					// search engine not in list, 0 switches
					bEnd = true;
				}
				else if (iEnginePos[i] > imax)
				{
					iMaxEngine = i;
					imax = iEnginePos[i];
				}
			}
			iPosQuery = imax-1;

			if (bEnd == false)
				iSwitches++;
		}		

		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase+1, iSwitches);
	
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}