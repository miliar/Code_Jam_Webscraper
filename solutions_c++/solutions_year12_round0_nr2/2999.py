//============================================================================
// Name        : jam_test.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>
//#include <sstream>
//#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


int main(int argc, char** argv)
{

	if(argc!=3)
	{
		cout << "Usage:" << endl;
		cout << "jam_test infile outfile" << endl;
		return 0;
	}

	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	if(!infile)
		cout << "Input file open error!" << endl;

	if(!outfile)
		cout << "Output file open error!" << endl;

	int nCase;

	int i,j;
	int score[100];
	int n,s,p;
	int count = 0;
	int min;

	infile >> nCase ;
	//cout << "Case Num:" << nCase << endl;

	for(int iCase=0; iCase<nCase; iCase++)
	{
		cout << "Case #" << iCase+1 << ": " << endl;
		outfile << "Case #" << iCase+1 << ": ";

		infile >> n;
		infile >> s;
		infile >> p;

		count = 0;

		if(p == 0)
			min = 0;
		else
			if(p == 1)
				min = 1;
			else
				min = p-2;

		int supMin = p + min + min;
		if(p == 0)
			min = 0;
		else
			min = p-1;
		int norMin = p + min + min;

		for(i=0; i<n; i++)
		{
			infile >> score[i];

			if(score[i] >= norMin)
			{
				count++;
			}
			else
			{
				if(score[i] >= supMin && s>0)
				{
					count++;
					s--;
				}
			}
		}

		outfile << count << endl;
		//outfile << endl;

	}

	return 0;
}
