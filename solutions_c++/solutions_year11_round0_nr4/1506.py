// C++ source code file for Problem - Goro Sort
// ANIL SOOD
// anilsood.ucla@gmail.com

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int count = 0;
	int length = 0;
	int answer = 0;
	string inputFile = "C:\\Users\\Anil\\Desktop\\input.in";
	string outputFile = "C:\\Users\\Anil\\Desktop\\output.out";
	string line;
	string filteredLine;
	ifstream myfile (inputFile);
	ofstream myoutfile (outputFile);

	if (myfile.is_open() && myoutfile.is_open())
	{
		int caseIndex = 0;

		// Skip the count
		if(myfile.good())
			getline (myfile,line);

		while ( myfile.good() )
		{
			caseIndex++;			
			getline (myfile,line);

			if(line.length() == 0)
				return -1;

			int temp = 0;
			int l = line.length();
			for (int i = 0; i < l; i++)
			{
				temp = (10 * temp) + line[i] - 48;
			}
			const int numOfElements = temp;
			int arr[1000];

			getline (myfile,line);
			l = line.length();

			temp = 0;
			int j = 0;
			for(int i = 0; i < l; i++)
			{
				if(line[i] != 32)
				{
					temp = (10 * temp) + line[i] - 48;					
				}
				else
				{
					arr[j] = temp;
					temp = 0;
					j++;
				}
			}
			arr[j] = temp;
			temp = 0;

			int countOfUnorderedElements = 0;
			for (int i = 0; i < numOfElements; i++)
			{
				if(arr[i] != i + 1)
					countOfUnorderedElements++;
			}

			myoutfile << "Case #" << caseIndex << ": " << countOfUnorderedElements << "\n";
		}

		myfile.close();
		myoutfile.close();
	}		 		
}