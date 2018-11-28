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

int i_Cases = 0;
const char z_Msg[] = "welcome to code jam";
int i_MsgLen = strlen(z_Msg);	
char* z_Str;
int i_StrLen;

unsigned long long int ul_Count;
list<int> lst_Temp;
int i_ListSize;

void Calculate()
{
	ul_Count = 0L;
	lst_Temp.clear();
	i_ListSize = 0;
	
	if (i_StrLen < i_MsgLen)
		return;
		
	int iMsgPos = 0;
	int iStrPos = 0;
	while(true)
	{		
		// --- forward ---
		while(iStrPos < i_StrLen)
		{	
			if (i_Debug) printf("z_Str[%d]=%c; z_Msg[%d]=%c\n",
								iStrPos,z_Str[iStrPos],iMsgPos,z_Msg[iMsgPos]);
			if (z_Str[iStrPos] == z_Msg[iMsgPos])
			{
				lst_Temp.push_front(iStrPos);
				i_ListSize++;
				if (i_Debug) printf("pushed=%d; ListSize=%d\n",iStrPos,i_ListSize);
				if (iMsgPos == i_MsgLen-1) // end
				{
					ul_Count++;
					if (i_Debug) printf("ul_Count=%llu\n",ul_Count);
					break;
				}
				iMsgPos++;
			}
			iStrPos++;
		}

		// --- check terminal cond ---
		if (i_ListSize == 0)
			break;
					
		// --- backtrack ---
		while(i_ListSize > 0)
		{
			iMsgPos = i_ListSize - 1;
			iStrPos = lst_Temp.front() + 1;
			lst_Temp.pop_front();
			i_ListSize--;
			if (i_Debug) printf("poped=%d; ListSize=%d\n",iStrPos,i_ListSize);
			if (iStrPos < i_StrLen) // have more to check; break & go forward.
				break;
		}
	}
}

void Start(char* zFile)
{	
	if (i_Debug) printf("Msg=%s; Len=%d\n",z_Msg,i_MsgLen);
	string line;
	ifstream myfile(zFile);
	if (myfile.is_open())
	{
		getline (myfile,line);
		i_Cases = atoi(line.c_str());
		if (i_Debug) printf("Cases=%d\n",i_Cases);

		for (int i=1; i<=i_Cases; i++)
		{	
			getline (myfile,line);
			i_StrLen = line.length();
			z_Str = new char[i_StrLen+1];
			strcpy(z_Str,line.c_str());
			if (i_Debug) printf("Str=%s; Len=%d\n",z_Str,i_StrLen);
			
			// --- Start Processsing ---
			Calculate();
			
			//ul_Count = 333941254; // test
			if (i_Debug) printf("ul_Count = %llu\n",ul_Count);
			int iNum = 0;
			if (ul_Count > 9999)
			{
				char zBuff[500];
				sprintf(zBuff,"%llu",ul_Count);
				char* zNum = zBuff + (strlen(zBuff)-4);
				iNum = atoi(zNum);
			}
			else
				iNum = (int)ul_Count;
				
			printf("Case #%d: %04d\n",i,iNum);
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
