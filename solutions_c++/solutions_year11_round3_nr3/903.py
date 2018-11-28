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
	int N, L, H;
	inFile >> N >> L>>H;

	int vect[100];
	for (int i = 0; i < N; i++)
		inFile >> vect[i];

	for (int i = L; i <= H; i++)
	{
		bool good = true;
		for (int j = 0; j < N; j++)
		{
			if(!(vect[j] % i == 0 || i % vect[j] == 0))
			{
				good = false;
				break;
			}
		}
		if(good)
		{
			outFile << "Case #" << caseIndex << ": " << i<<endl;
			return;
		}
	}

	outFile << "Case #" << caseIndex << ": NO" << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	inFile.open("C-small-attempt0.in", ios::in);    // open the streams
	outFile.open("C-small.out", ios::out);
	//inFile.open("C-large.in", ios::in);    // open the streams
	//outFile.open("C-large.out", ios::out);

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
