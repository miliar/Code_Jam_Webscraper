#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE		15

int iTurnaround;
int iDeparturesA;
int iDeparturesB;

int iDepartureTimeAB[100];
int iArrivalTimeAB[100];

int iDepartureTimeBA[100];
int iArrivalTimeBA[100];

bool bDepartedA[100];
bool bDepartedB[100];

bool bTrainAUsed[100];
bool bTrainBUsed[100];


int GetEarliestDepart(char c)
{
	int imin = 1440;
	int iminNumber = -1;
	if (c=='A')
	{
		for (int i=0;i<iDeparturesA; i++)
		{
			if (iDepartureTimeAB[i]<imin && !bDepartedA[i])
			{
				imin = iDepartureTimeAB[i];
				iminNumber = i;
			}
		}
	}
	else
	{
		for (int i=0;i<iDeparturesB; i++)
		{
			if (iDepartureTimeBA[i]<imin && !bDepartedB[i])
			{
				imin = iDepartureTimeBA[i];
				iminNumber = i;
			}
		}
	}
	return iminNumber;
}
bool IsTrainInStation(char c, int time)
{
	bool bResult = false;
	if (c=='A')
	{
		// look for trains from B to A
		for (int i=0;i<iDeparturesB; i++)
		{
			if (iArrivalTimeBA[i]+iTurnaround <= time && !bTrainBUsed[i])
			{
				// take this train
				bTrainBUsed[i] = true;
				return true;
			}
		}
	}
	else
	{
		// look for trains from A to B
		for (int i=0;i<iDeparturesA; i++)
		{
			if (iArrivalTimeAB[i]+iTurnaround <= time && !bTrainAUsed[i])
			{
				// take this train
				bTrainAUsed[i] = true;
				return true;
			}
		}
	}
	return bResult;
}

bool AreAllTrainsDeparted()
{
	bool bResult = true;
	int i;
	for (i=0; i<iDeparturesA; i++)
	{
		if (!bDepartedA[i])
			return false;
	}
	for (i=0; i<iDeparturesB; i++)
	{
		if (!bDepartedB[i])
			return false;
	}
	return bResult;
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
		
		// turnaround time
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
		iTurnaround = atoi(strZahl);

		// departures at a and b
		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return -1;

		// departures at A
		ipos = 0;
		int istart = ipos;
		while (strLine[ipos] != ' ' && strLine[ipos] != '\n' && ipos<MAX_LEN_LINE)
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[istart], ipos-istart);
		strZahl[ipos-istart] = 0;
		iDeparturesA = atoi(strZahl);

		// departures at B
		ipos++;
		istart = ipos;
		while (strLine[ipos] != ' ' && strLine[ipos] != '\n' && ipos<MAX_LEN_LINE)
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[istart], ipos-istart);
		strZahl[ipos-istart] = 0;
		iDeparturesB = atoi(strZahl);

		
		// departures and arrivals
		for (i=0; i<(iDeparturesA+iDeparturesB); i++)
		{
			if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
				return -1;
			
			// departure hour
			ipos = 0;
			istart = ipos;
			while (strLine[ipos] != ':' && strLine[ipos] != ' ' && strLine[ipos] != '\n')
			{
				ipos++;
			}
			strncpy(strZahl, &strLine[istart], ipos-istart);
			strZahl[ipos-istart] = 0;
			int iDepartureHour = atoi(strZahl);
			// departure minute
			ipos++;
			istart = ipos;
			while (strLine[ipos] != ':' && strLine[ipos] != ' ' && strLine[ipos] != '\n')
			{
				ipos++;
			}
			strncpy(strZahl, &strLine[istart], ipos-istart);
			strZahl[ipos-istart] = 0;
			int iDepartureMinute = atoi(strZahl);
			// arrival hour
			ipos++;
			istart = ipos;
			while (strLine[ipos] != ':' && strLine[ipos] != ' ' && strLine[ipos] != '\n')
			{
				ipos++;
			}
			strncpy(strZahl, &strLine[istart], ipos-istart);
			strZahl[ipos-istart] = 0;
			int iArrivalHour = atoi(strZahl);
			// arrival minute
			ipos++;
			istart = ipos;
			while (strLine[ipos] != ':' && strLine[ipos] != ' ' && strLine[ipos] != '\n')
			{
				ipos++;
			}
			strncpy(strZahl, &strLine[istart], ipos-istart);
			strZahl[ipos-istart] = 0;
			int iArrivalMinute = atoi(strZahl);
			ipos++;

			int iDepartureTime = iDepartureHour*60+iDepartureMinute;
			int iArrivalTime = iArrivalHour*60 + iArrivalMinute;
			if (i<iDeparturesA)
			{
				iDepartureTimeAB[i] = iDepartureTime;
				iArrivalTimeAB[i] = iArrivalTime;
			}
			else
			{
				iDepartureTimeBA[i-iDeparturesA] = iDepartureTime;
				iArrivalTimeBA[i-iDeparturesA] = iArrivalTime;
			}


		}

		// algorythm
		int iCountA = 0;
		int iCountB = 0;

		for (i=0; i<100; i++)
		{
			bDepartedA[i] = false;
			bDepartedB[i] = false;
			bTrainAUsed[i] = false;
			bTrainBUsed[i] = false;
		}
		
		bool bReady = false;
		while (bReady == false)
		{
			// look for earliest train
			int iEarliestA = GetEarliestDepart('A');
			int iEarliestB = GetEarliestDepart('B');
			
			
			int itA;
			if (iEarliestA>=0)
			{
				itA = iDepartureTimeAB[iEarliestA];
			}
			else
				itA = 1440;
			int itB;
			if (iEarliestB>=0)
			{
				itB = iDepartureTimeBA[iEarliestB];
			}
			else
				itB = 1440;

			
			if (itB<itA)
			{
				// B
				bool b = IsTrainInStation('B', iDepartureTimeBA[iEarliestB]);
				if (b == false)
					iCountB++;
				bDepartedB[iEarliestB] = true;
			}
			else
			{
				// A
				bool b = IsTrainInStation('A', iDepartureTimeAB[iEarliestA]);
				if (b == false)
					iCountA++;
				bDepartedA[iEarliestA] = true;
			}

			bReady = AreAllTrainsDeparted();
		}


		// Ausgabe
		fprintf(fOutput, "Case #%d: %d %d\n", iCase+1, iCountA, iCountB);
	
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}