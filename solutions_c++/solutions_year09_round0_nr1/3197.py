#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int L, D, N;
	unsigned int *uiCurIndex;
	int iStrLength, CurPos;
	int i, j, k ,l;
	char * lineBuffer;	
	char ** strDictionary;
	char ch;
	char *strTest;
	bool bInGroup, bInPattern, bFoundChar;
	unsigned long ulNumMatches;
			
	ifstream inFile;
	
	vector<vector<char> > vecvecPossibleMessageChars;
	vector<char> vecEmpty;
	
	inFile.open("A-large.in");
	
	if (!inFile)
	{
		cerr << "Could not open input file!" << endl;
		exit(1);		
	}
	
	inFile >> L >> D >> N;
	
	//Allocate memory
	//This is the maximum line buffer size since a completely garbled transmission
	//would be 26^2 (=676) in length, with parenthesis around each L groups and 1 char for null
	lineBuffer = new char[676+(2*L)+1];
	//The indexes that we'll use are L long
	uiCurIndex=new unsigned int [L];
	//The testing string that we'll use is L+1 in length
	strTest=new char [L+1];
	//The maximum dictionary size is D
	strDictionary = new char*[D];
	for (i=0; i<D; ++i)
		strDictionary[i]=new char[L+1];

	//Read D lines from input file	
	for (i=0; i<D; ++i)
		inFile >> strDictionary[i];

	//Read N test cases from input file	
	for (i=0; i<N; ++i)
	{
		inFile >> lineBuffer;

		//reset all variables used in determining whether or not this message is in the dictionary
		ulNumMatches=0;
		//reset index info
		for (j=0; j<L; ++j)
			uiCurIndex[j]=0;		
		//set testing string null char
		strTest[L]=0;
		//reset current position
		CurPos=0;
		//reset possible character vector		
		vecvecPossibleMessageChars.clear();

		//Now parse our the string into the appropriate structures
		iStrLength=strlen(lineBuffer);
		
		bInGroup=false;
		for (j=0; j<iStrLength; ++j)
		{
			if (bInGroup==false)
				vecvecPossibleMessageChars.push_back(vecEmpty);
			ch=lineBuffer[j];
			switch(ch)
			{
				case '(':
					bInGroup=true;
					break;
				case ')':
					bInGroup=false;
					break;
				default:
					vecvecPossibleMessageChars.back().push_back(ch);					
			}
		}

		//iterate through each of the dictionary words to check to see if they match the current pattern
		for (j=0; j<D; ++j)
		{
			bInPattern=true;
			for (k=0; ((k<L) && (bInPattern==true)); ++k)
			{
				ch=strDictionary[j][k];
				bFoundChar=false;
				for (l=0; ((l<(int)vecvecPossibleMessageChars[k].size()) && (bFoundChar==false)); ++l)
				{
					if (vecvecPossibleMessageChars[k][l]==ch)
						bFoundChar=true;
				}
				bInPattern=bFoundChar;
			}
			if (bInPattern==true)
				++ulNumMatches;
		}	
		cout << "Case #" << i+1 << ": " << ulNumMatches << endl;
	}
	
	inFile.close();
	
	//deallocate memory
	delete [] lineBuffer;
	delete [] uiCurIndex;
	delete [] strTest;
	for (i=0; i<D; ++i)
	{
		delete [] strDictionary[i];
	}
	delete [] strDictionary;
		
		
	return 0;
}
