// gcj2009c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define IncV(i) quant[(i)] = (quant[(i)] + quant[(i - 1)]) % 10000

int _tmain(int argc, _TCHAR* argv[])
{
	string ss;
	ifstream input_file;
	input_file.open("C-large.in");
	int n_tests;
	input_file >> n_tests;
	getline(input_file, ss);
	ofstream output_file;
	output_file.open("c-large.out");
	for (int i = 0; i < n_tests; ++i)
	{
		vector<int> quant;
		quant.resize(19, 0);
		getline(input_file, ss);
		for (int j = 0; j < ss.size(); ++j)
		{
			switch(ss[j])
			{
			case 'w':
				quant[0] = (quant[0] + 1) % 10000;
				break;
			case 'e':
				IncV(1);
				IncV(6);
				IncV(14);
				break;
			case 'l':
				IncV(2);
				break;
			case 'c':
				IncV(3);
				IncV(11);
				break;
			case 'o':
				IncV(4);
				IncV(9);
				IncV(12);
				break;
			case 'm':
				IncV(5);
				IncV(18);
				break;
			case ' ':
				IncV(7);
				IncV(10);
				IncV(15);
				break;
			case 't':
				IncV(8);
				break;
			case 'd':
				IncV(13);
				break;
			case 'j':
				IncV(16);
				break;
			case 'a':
				IncV(17);
				break;
			}
		}
		output_file << "Case #" << i + 1 << ": ";
		output_file.fill('0');
		output_file.width(4);
		output_file << quant[18];
		if (i != n_tests - 1)
			output_file << endl;
	}
	input_file.close();

	output_file.close();
	return 0;
}

