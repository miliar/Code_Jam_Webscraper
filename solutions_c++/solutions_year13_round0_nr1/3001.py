// main project file.

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <hash_map>
#include <algorithm>
using namespace std;
using namespace System;


int main(array<System::String ^> ^args)
{
	string file;
	string path = "C:\\Users\\Ben\\Downloads\\";
	int problemNum = 0;
	cin >> problemNum;
	getline (cin,file);
    ifstream infile;
	ofstream outfile;
	infile.open (path + file + ".in");
	outfile.open (file + ".out");
	if(problemNum == 0) // example for io. sums a list of numbers.
	{
		vector<int> output;
		int size1;
		int size2;
		int val;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{
			output.push_back(0);
			infile >> size2;
			for(int j = 0; j < size2; j++)
			{
				infile >> val;
				output[i] += val;
			}
			outfile << output[i] << endl;
		}


	}
	if(problemNum == 1)
	{
		int size1;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{
			char down[] = {' ',' ',' ',' '};
			char diag[] = {' ',' '};
			string ln;
			char status = '.';
			bool filled = true;
			for(int j = 0; j < 4; j++)
			{
				infile >> ln;
				char first = ln[0];
				if(first == 'T')
					first = ln[1];
				bool good = true;
				for(int k = 0; k < 4; k++)
				{
					if(ln[k] != first && ln[k] != 'T')
						good = false;
					if(ln[k] == '.')
						filled = false;
					if(down[k] == ' ')
						down[k] = ln[k];
					else
					{
						if(down[k] == 'T')
							down[k] = ln[k];
						if(down[k] != ln[k] && ln[k] != 'T')
							down[k] = '-';
					}
					if(k == j)
					{
						if(diag[0] == ' ')
							diag[0] = ln[k];
						else
						{
							if(diag[0] == 'T')
								diag[0] = ln[k];
							if(diag[0] != ln[k] && ln[k] != 'T')
								diag[0] = '-';
						}
					}
					if(k == 3-j)
					{
						if(diag[1] == ' ')
							diag[1] = ln[k];
						else
						{
							if(diag[1] == 'T')
								diag[1] = ln[k];
							if(diag[1] != ln[k] && ln[k] != 'T')
								diag[1] = '-';
						}
					}
				}
				if(good && (first == 'X' || first == 'O'))
					status = first;
			}
			for(int j = 0; j < 4; j++)
				if(down[j] == 'X' || down[j] == 'O')
					status = down[j];
			for(int j = 0; j < 2; j++)
				if(diag[j] == 'X' || diag[j] == 'O')
					status = diag[j];
			if(status == 'X' || status == 'O')
			{
				outfile << "Case #" << i+1 << ": " << status << " won" << endl;
			}
			else if(filled)
			{
				outfile << "Case #" << i+1 << ": Draw" << endl;
			}
			else
			{
				outfile << "Case #" << i+1 << ": Game has not completed" << endl;
			}
		}
	}
	if(problemNum == 2)
	{
		int size1;
		infile >> size1;
		for(int i = 0; i < size1; i++)
		{

		}
	}
	if(problemNum == 3)
	{
		
	}
	if(problemNum == 4)
	{
		
	}
	infile.close();
	outfile.close();
    return 0;
}
