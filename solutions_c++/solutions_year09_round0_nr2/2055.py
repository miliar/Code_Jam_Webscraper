#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <list>

using namespace std;

// DEBUG On/Off flag
int i_Debug;

// Directions: N=1, W=2, E=3, S=4
#define EMPTY	'*'

int i_Cases = 0;
int i_H = 0;	
int i_W = 0;
int i_Size = 0;

int i_Basin;
int* ai_Alts;
int* ai_Chrs;
list<int> lst_Temp;

int GetSquare(int iCurrSq, int iDirn)
{
	int iSq = -1;
	switch(iDirn)
	{
	case 1: // North
		if (iCurrSq > i_W)
			iSq = iCurrSq - i_W;
		break;
	case 2: // West
		if (iCurrSq % i_W != 1)
			iSq = iCurrSq - 1;
		break;
	case 3: // East
		if (iCurrSq % i_W != 0)
			iSq = iCurrSq + 1;
		break;
	case 4: // South
		iSq = iCurrSq + i_W;
		if (iSq > i_Size)
			iSq = -1;
		break;		
	}
	return iSq;
}

int GetLowestSq(int iCurrSq)
{
	int iLowSq = -1;
	for(int i=1; i<=4; i++)
	{
		int iChkSq = GetSquare(iCurrSq,i);
		if ((iChkSq>0) && (ai_Alts[iChkSq]<ai_Alts[iCurrSq]) 
				&& (iLowSq==-1 || ai_Alts[iChkSq]<ai_Alts[iLowSq]))
		{
			iLowSq = iChkSq;
		}
	}
	return iLowSq;
}

void TraverseFromSq(int iStartSq)
{
	if (i_Debug) printf("TraverseFromSq: Sq=%d; Alt=%d\n",iStartSq,ai_Alts[iStartSq]);
	int iCurrSq = iStartSq;
	while(true)
	{
		if (ai_Chrs[iCurrSq] != EMPTY) // found an existing path
		{
			list<int>::iterator ite = lst_Temp.begin();
			for (; ite!=lst_Temp.end(); ite++)
			{
				int iSq = *ite;
				ai_Chrs[iSq] = ai_Chrs[iCurrSq];
				if (i_Debug) printf("set ai_Chrs[%d] = %c\n",iSq,ai_Chrs[iSq]); 
			}
			if (!lst_Temp.empty())
				lst_Temp.clear();
			return;
		}
		
		lst_Temp.push_back(iCurrSq);
		
		int iLowSq = GetLowestSq(iCurrSq);
		if (iLowSq > 0)
		{
			iCurrSq = iLowSq;
			if (i_Debug) printf("changing to lowest: Sq=%d; Alt=%d\n",iCurrSq,ai_Alts[iCurrSq]);
		}
		else // found a new sink
		{
			ai_Chrs[iCurrSq] = i_Basin;
			if (i_Debug) printf("Found Sink: Sq=%d; Alt=%d; Chr=%c\n",iCurrSq,ai_Alts[iCurrSq],ai_Chrs[iCurrSq]);
			i_Basin++;
		}
	}	
}

void Traverse()
{
	for(int i=1; i<=i_Size; i++)
	{
		TraverseFromSq(i);	
	}	
}

void Start(char* zFile)
{	
	string line;
	ifstream myfile(zFile);
	if (myfile.is_open())
	{
		getline (myfile,line);
		i_Cases = atoi(line.c_str());
		if (i_Debug) printf("Cases = %d\n",i_Cases);
		
		for (int i=1; i<=i_Cases; i++)
		{
			getline (myfile,line);
			sscanf(line.c_str(),"%d %d", &i_H, &i_W);
			i_Size = i_H * i_W;
			if (i_Debug) printf("H=%d; W=%d; Siz=%d\n",i_H,i_W,i_Size);
			ai_Alts = new int[i_Size +1];
			ai_Chrs = new int[i_Size +1];
			i_Basin = 'a';
			
			for (int j=1; j<=i_H; j++)
			{
				getline (myfile,line);
				char* zBuff = new char[line.length()+1];
				strcpy(zBuff,line.c_str());
				char* pch = strtok(zBuff," ");
				for (int k=1; k<=i_W; k++)
				{
					int iSq = i_W*(j-1) + k;
					ai_Alts[iSq] = atoi(pch);
					ai_Chrs[iSq] = EMPTY;
					if (i_Debug) printf ("ai_Alts[%d]=%d\n",iSq,ai_Alts[iSq]);
					pch = strtok (NULL, " ");
				}
			}
						
			// --- Calculate ---
			Traverse();
			printf("Case #%d:\n",i);
			for(int i=1; i<=i_H; i++)
			{
				for(int j=1; j<=i_W; j++)
					printf("%c ",ai_Chrs[i_W*(i-1) + j]);
				printf("\n");
			}
		}
		myfile.close();
	}
	else 
		printf("Unable to open file\n"); 
}

int main(int argc, char* argv[])
{
	if (argc == 3)
	{
		i_Debug = atoi(argv[2]);
		Start(argv[1]);
	}
	else 
		printf("usage: $> <app> <filename> <debug print: 1|0>\n");
		
	return 0;
}
