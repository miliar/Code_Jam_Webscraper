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
	int A, B;
	inFile >> A >> B;

	int dim = 0;	
	int t;
	do 
	{
		dim++;
		t = A / pow(10.0, dim);
	} while (t > 0);
		
	if (dim < 2)
	{
		outFile << "Case #" << caseIndex << ": 0" << endl;
		return;
	}
	
	map<int, set<int>> rec;

	int found = 0;

	for (int n = A; n < B; n++)
	{
		for (int d = 1; d < dim; d++)
		{
			int divisor = pow(10.0, d);
			int back = n % divisor;
			if (back == 0)
				continue;
			int front = n / divisor;
			
			int mul = pow(10.0, dim - d);
			int m = back * mul + front;
			if (n < m && m <= B)
			{
				//got a recycled pair (n, m)
				if (rec[n].count(m) == 0)
				{
					found++;
					rec[n].insert(m);
				}
			}
		}
	}

	outFile << "Case #" << caseIndex << ": " << found << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	//inFile.open("C-small-attempt1.in", ios::in);    // open the streams
	//outFile.open("C-small.out", ios::out);
	inFile.open("C-large.in", ios::in);    // open the streams
	outFile.open("C-large.out", ios::out);

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
