// codejamtemplate.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>  // I/O 
#include <fstream>   // file I/O
#include <iomanip>   // format manipulation
#include <ios>
#include <string>
#include <sstream>
#include <math.h>
#include <set>
#include <map>

using namespace std;

template<typename RT, typename T, typename Trait, typename Alloc>
RT ss_atoi(const basic_string<T, Trait, Alloc>& the_string)
{
    basic_istringstream< T, Trait, Alloc> temp_ss(the_string);
    RT num;
    temp_ss >> num;
    return num;
}

void ProcessCase(int caseIndex, ifstream &inFile, ofstream &outFile)
{
	int R, C;
	inFile >> R >> C;

	char matrix[50][50];
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			inFile >> matrix[i][j];
		}
	}
	bool good = true;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (matrix[i][j] == '#')
			{
				if (i == R-1 || j == C-1)
				{
					good = false;
					goto end;
				}
				if(matrix[i][j+1] == '.' || matrix[i+1][j] == '.' || matrix[i+1][j+1]=='.')
				{
					good = false;
					goto end;
				}
				matrix[i][j] = '/';
				matrix[i][j+1] = '\\';
				matrix[i+1][j] = '\\';
				matrix[i+1][j+1]='/';


			}
		}
	}
end:
	outFile << "Case #" << caseIndex << ":" << endl;
	if (!good)
		outFile << "Impossible" << endl;
	else
	{
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				outFile << matrix[i][j];
			}
			outFile << endl;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	
	inFile.open("A-large.in", ios::in);    // open the streams
	outFile.open("A-large.out", ios::out);

	int N; // the number of cases
	inFile >> N;

	for (int i = 0; i < N; i++)
	{
		ProcessCase(i + 1, inFile, outFile);
	}

	inFile.close();   // close the streams
	outFile.close(); 

	return 0;
}
