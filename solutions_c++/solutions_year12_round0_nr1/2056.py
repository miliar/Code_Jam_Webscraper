
#include <Windows.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define STRING_SIZE		( 101 )

static CHAR replacmentTable[]			= "yhesocvxduiglbkrztnwjpfmaq";
static CHAR replacmentCapitalTable[]	= "YHESOCVXDUIGLBKRZTNWJPFMAQ";

int main(int argc, char* argv[])
{
	UINT32		numOfStrings	= 0;
	UINT32		iIndex			= 0;
	UINT32		jIndex			= 0;
	ifstream	inputFile;

	do 
	{
		//DebugBreak();

		if (argc != 2)
		{
			printf("Need input file...\n");
			break;
		}

		inputFile.open(argv[1]);
		if (!(inputFile.is_open()))
		{
			printf("Problem opening input file (%s)...\n", argv[1]);
			break;
		}

		string firstLine;
		getline(inputFile, firstLine);
		numOfStrings = atoi(firstLine.c_str());

		for (iIndex=0; iIndex<numOfStrings && inputFile.good(); ++iIndex)
		{
			string	oldString;
			CHAR	newString[STRING_SIZE] = {0};

			getline(inputFile, oldString);

			for (jIndex=0; jIndex<oldString.size(); ++jIndex)
			{
				if (('a' <= oldString[jIndex]) && (oldString[jIndex] <= 'z'))
				{
					newString[jIndex] = replacmentTable[oldString[jIndex] - 'a'];
				}
				else if (('A' <= oldString[jIndex]) && (oldString[jIndex] <= 'Z'))
				{
					newString[jIndex] = replacmentCapitalTable[oldString[jIndex] - 'A'];
				} 
				else
				{
					newString[jIndex] = oldString[jIndex];
				}
			}

			newString[jIndex] = '\0';

			printf("Case #%d: %s\n", iIndex+1, newString);
		}

	} while (FALSE);

	if (inputFile.is_open())
	{
		inputFile.close();
	}

	return 0;
}

