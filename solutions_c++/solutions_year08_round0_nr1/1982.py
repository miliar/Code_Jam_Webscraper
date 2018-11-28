#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void ClearMachPos(int* MachNextPos, int MachNum)
{
	for (int i=0; i<MachNum; i++)
		MachNextPos[i]=-1;
}

int FindNum(char** MachNames, char* CurMachName, int MachNum)
{
	for (int i=0; i<MachNum; i++)
	{
		if (strstr(CurMachName, MachNames[i]) == CurMachName)
		{
			return i;
		}
	}
}

void main ()
{
	int CaseNum;
	int MachNum;
	int QueryNum;
	char *CaseNumStr = new char [4];
	char *MachNumStr = new char [4];
	char *QueryNumStr = new char [5];
	char ** MachNames;
	int *MachNextPos;

	char* CurrentMach = new char [1000];
	int CurrentMachNum;

	FILE *InFile, *OutFile;
	InFile = fopen("input.txt", "a+");
	OutFile = fopen("output.txt", "a+");
	fgets(CaseNumStr, 4, InFile);
	CaseNum = atoi(CaseNumStr);
	
	for(int i=0; i<CaseNum; i++)
	{
		fgets(MachNumStr, 4, InFile);
		MachNum = atoi(MachNumStr);
		
		MachNames = new char* [MachNum];
	
		for (int k=0; k<MachNum; k++)
		{
			MachNames[k] = new char [1000]; 
			fgets(MachNames[k], 1000, InFile);
			printf("%s\n", MachNames[k]);
		}
		
		MachNextPos = new int [MachNum];
		int SwitchCount = 0;
		int MachinesLeft = MachNum;
		ClearMachPos(MachNextPos, MachNum);
		fgets(QueryNumStr, 5, InFile);
		QueryNum = atoi(QueryNumStr);
		int j=0;
		//for (int j=0; j<QueryNum; j++)
		while (j<QueryNum)
		{
			fgets(CurrentMach, 1000, InFile);
			CurrentMachNum = FindNum(MachNames, CurrentMach, MachNum);
			if (MachNextPos[CurrentMachNum] == -1) 
			{
				MachNextPos[CurrentMachNum] = j;
				MachinesLeft--;
			}
			if (MachinesLeft == 0)
			{	
				SwitchCount++;
				ClearMachPos(MachNextPos, MachNum);
				MachinesLeft = MachNum-1;
				MachNextPos[CurrentMachNum] = 0;
			}
			j++;
		}
		
		fprintf(OutFile, "Case #%d: %d\n", i+1, SwitchCount);
		delete [] MachNextPos;
	
		for (int k=0; k<MachNum; k++)
			delete [] MachNames[k];
		delete [] MachNames;
	}
	fclose(InFile);
	fclose(OutFile);

}