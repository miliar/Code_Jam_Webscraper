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

using namespace std;

template<typename RT, typename T, typename Trait, typename Alloc>
RT ss_atoi(const basic_string<T, Trait, Alloc>& the_string)
{
    basic_istringstream< T, Trait, Alloc> temp_ss(the_string);
    RT num;
    temp_ss >> num;
    return num;
}

double RPI(double WP, double OWP, double OOWP)
{
	return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
}

void ProcessCase(int caseIndex, ifstream &inFile, ofstream &outFile)
{
	int N;
	inFile >> N;

	int matrix[100][100];
	double out[100];
	
	char c;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			inFile >> c;
			if (c == '1')
				matrix[i][j] = 1;
			else if (c == '0')
				matrix[i][j] = -1;
			else
				matrix[i][j] = 0;
		}
	}
	double wps[100];
	double gamesNumber[100];
	for (int i = 0; i < N; i++)
	{
		wps[i] = 0;
		gamesNumber[i] = 0;
		for (int j = 0; j < N; j++)
		{
			if (matrix[i][j] != 0)
			{
				gamesNumber[i]++;
				if (matrix[i][j] > 0)
					wps[i] += matrix[i][j];
			}
		}
	}

	double owps[100];
	for (int i = 0; i < N; i++)
	{
		owps[i] = 0;
		for (int j = 0; j < N; j++)
		{
			if (matrix[i][j] != 0)
			{
				double minusOne = 0, minusgame = 0;
				if (matrix[j][i] == 1)
				{
					minusOne = 1;
					minusgame = 1;
				}
				if (matrix[j][i] == -1)
					minusgame = 1;
				owps[i] += (wps[j] - minusOne) / (gamesNumber[j] - minusgame);
			}
		}
		owps[i] = owps[i] / gamesNumber[i];
	}

	double oowps[100];
	for (int i = 0; i < N; i++)
	{
		oowps[i] = 0;
		for (int j = 0; j < N; j++)
		{
			if (matrix[i][j] != 0)
			{
				oowps[i] += owps[j];
			}
		}
		oowps[i] = oowps[i] / gamesNumber[i];
	}

	outFile << "Case #" << caseIndex << ": " << endl;
	for (int i = 0; i < N; i++)
	{
		outFile << setprecision(12) << RPI(wps[i] / gamesNumber[i], owps[i], oowps[i]) << endl;
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
