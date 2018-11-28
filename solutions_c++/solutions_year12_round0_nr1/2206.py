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
#include <vector>

using namespace std;

template<typename RT, typename T, typename Trait, typename Alloc>
RT ss_atoi(const basic_string<T, Trait, Alloc>& the_string)
{
    basic_istringstream< T, Trait, Alloc> temp_ss(the_string);
    RT num;
    temp_ss >> num;
    return num;
}

map<char, char> charmap;

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

int best;
set<int> goal;
set<set<int>> globSS;

void Hanoy(set<int> current, vector<int> v[3], set<set<int>> ss, int step)
{
	if (step > best)
		return;

	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			if (j == i)
				continue;
			if (v[i].size() == 0)
				continue;
			int k = v[i].back();
			int p = v[j].size() > 0 ? v[j].back() : INT_MAX;
			if (k < p)
			{
				//move
				set<int> nc;
				for (set<int>::iterator it = current.begin(); it != current.end(); it++)
				{
					nc.insert(*it);
				}
				int erK = k * pow(10.0, i);
				nc.erase(erK);
				int insK = k * pow(10.0, j);
				nc.insert(insK);
				globSS.insert(nc);
				int sameCount = ss.count(nc);
				if (sameCount > 0)
					continue;
				ss.insert(nc);

				if (ss.count(goal) > 0)
				{
					if ((step+1) < best)
						best = step + 1;
					continue;
				}

				vector<int> n[3];
				for (int in = 0; in < 3; in++)
				{
					for (int din = 0 ; din < v[in].size(); din++)
						n[in].push_back(v[in][din]);
				}
				n[i].pop_back();
				n[j].push_back(k);
				Hanoy(nc, n, ss, step + 1);
			}
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;  // declarations of streams fp_in and fp_out
	ofstream outFile;
	
	ifstream preFileOut("preOut.in", ios::in);
	ifstream preFileIn("preIn.in", ios::in);

	inFile.open("A-small-attempt3.in", ios::in);
	outFile.open("A-small.out", ios::out);

	//inFile.open("A-large.in", ios::in);    // open the streams
	//outFile.open("A-large.out", ios::out);


	charmap['y'] = 'a';
	charmap['e'] = 'o';
	charmap['q'] = 'z';
	charmap['z'] = 'q';

	char inbuf[200];
	char prebuf[200];
	for (int i = 0; i < 3; i++)
	{
		preFileIn.getline(inbuf, 199);
		preFileOut.getline(prebuf, 199);

		for (int j = 0; inbuf[j] != 0; j++)
		{
			if (charmap.count(inbuf[j]) == 0)
			{
				charmap[inbuf[j]] = prebuf[j];
			}
		}

	}

	map<char, char> test;
	for (map<char, char>::iterator it = charmap.begin(); it != charmap.end(); it++)
	{
		test[it->second] = it->first;
	}

	int N; // the number of cases
	inFile >> N;
	inFile.getline(inbuf, 199);
	for (int i = 0; i < N; i++)
	{
		char inbuf[200];
		char prebuf[200];
		inFile.getline(inbuf, 199);
		int j;
		for (j = 0; inbuf[j] != 0; j++)
		{
			if (charmap.count(inbuf[j]) == 0)
				int k=0;
			prebuf[j] = charmap[inbuf[j]];
		}
		prebuf[j] = 0;
		outFile << "Case #" << i+1 << ": " << prebuf;
		if (i+1 < N)
			outFile << endl;
	}
//	inFile.close();   // close the streams
	outFile.close(); 

	return 0;
}
