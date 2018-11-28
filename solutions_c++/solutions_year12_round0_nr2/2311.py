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
	int N, S, p;
	inFile >> N >> S >> p;

	int good = 0;

	if (p > 0)
	{	
		int min = p*3 - 2;
		int minS = min - 2;
		for (int i = 0; i < N; i++)
		{
			int t;
			inFile >> t;
			if (t == 0)
				continue;
		
			if (t >= min)
			{
				good++;
			}
			else
			{
				if (S > 0 && t >= minS)
				{
					S--;
					good++;
				}
			}

															//int best = (t+2) / 3;
		//if (best >= p)
		//{
		//	good++;
		//}
		//else
		//{
		//	if (S > 0 && (best+1) == p)
		//	{
		//		S--;
		//		good++;
		//	}
		//}
		}
	}
	else
	{
		good = N;
		int t;
		for (int i = 0; i < N; i++)	
			inFile >> t;
	}
	outFile << "Case #" << caseIndex << ": " << good << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	//inFile.open("B-small-attempt1.in", ios::in);    // open the streams
	//outFile.open("B-small.out", ios::out);
	inFile.open("B-large.in", ios::in);    // open the streams
	outFile.open("B-large.out", ios::out);

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
