#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <map>
#include <list>

using namespace std;

// DEBUG On/Off flag
int i_Debug;

typedef pair<int,int> pairIntInt;

int i_Cases = 0;
int i_L = 0;	
int i_D = 0;
int i_Groups;

map<int,int>map_Chrs[20]; 
char** z_Words;
int i_Count;
char* z_Str;
int i_StrLen;

void Tokenize()
{
	for (int j=0; j<i_Groups; j++)
		map_Chrs[j].clear();
	
	int iGroup = -1;  // make maps 0 index based.
	bool bInGroup = false;
	for(int i=0; i<i_StrLen; i++)
	{
		switch(z_Str[i])
		{
		case '(':
			iGroup++;
			bInGroup = true;
			break;
		case ')':
			bInGroup = false;
			break;
		default:
			if (bInGroup)
			{
				map_Chrs[iGroup].insert( pairIntInt(z_Str[i], 1) );
			}
			else
			{
				iGroup++;
				map_Chrs[iGroup].insert( pairIntInt(z_Str[i], 1) );
			}
			if (i_Debug) printf("Added to Map[%d]: z_Str[%d]=%c(%d);\n",iGroup,i,z_Str[i],z_Str[i]);		
		}
	}
	assert(iGroup == i_Groups-1);
}

void Calculate()
{
	map <int,int>::const_iterator ite;
	i_Count = 0;
	
	for (int i=0; i<i_D; i++)
	{
		bool bMatch = true;
		char* zWord = z_Words[i];
		if (i_Debug) printf("Checking z_Words[%d]: %s\n",i,zWord);
		for (int j=0; j<i_L; j++)
		{
			ite = map_Chrs[j].find(zWord[j]);
			if (ite == map_Chrs[j].end()) // not found
			{
				bMatch = false;
				if (i_Debug) printf("match failed at pos=%d; Chr=%c\n",j,zWord[j]);
				break;
			}
		}
		
		if (bMatch)
		{
			i_Count++;
			if (i_Debug) printf("Count incremented: %d\n",i_Count);
		}
	}
}


void Start(char* zFile)
{	
	string line;
	ifstream myfile(zFile);
	if (myfile.is_open())
	{
		getline (myfile,line);
		sscanf(line.c_str(),"%d %d %d", &i_L, &i_D, &i_Cases);
		i_Groups = i_L;
		z_Words = new char*[i_D];
		
		if (i_Debug) printf("L=%d; D=%d; Cases=%d\n",i_L,i_D,i_Cases);

		for (int j=0; j<i_D; j++)
		{
			getline (myfile,line);
			z_Words[j] = new char[line.length()+1];
			strcpy(z_Words[j],line.c_str());
			if (i_Debug) printf("z_Words[%d] = %s\n",j,z_Words[j]);
		}

		for (int i=1; i<=i_Cases; i++)
		{
			getline (myfile,line);
			i_StrLen = line.length();
			z_Str = new char[i_StrLen+1];
			strcpy(z_Str,line.c_str());
			if (i_Debug) printf("Str=%s; Len=%d\n",z_Str,i_StrLen);
			
			// --- Start Processsing ---
			Tokenize();
			Calculate();
			printf("Case #%d: %d\n",i,i_Count);
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
