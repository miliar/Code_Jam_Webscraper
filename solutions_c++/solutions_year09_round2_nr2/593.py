// gcj2009r1a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input_file;
	ofstream output_file;
	input_file.open("B-large.in");
	output_file.open("B-large.out");
	int n_tests;
	input_file >> n_tests;
	string aa;
	getline(input_file, aa);
	for (int test = 1; test <= n_tests; ++test)
	{
		string number;
		bool next = false;
		getline(input_file, number);
		for (int i = number.size() - 1; i > 0; --i)
		{
			if (number[i] > number[i - 1])
			{
				for (int n = 1; n < number.size() - i; ++n)
					for (int j = i; j < number.size() - n; ++j)
						if (number[j] > number[j + 1])
						{
							char c = number[j];
							number[j] = number[j + 1];
							number[j + 1] = c;
						}
				int j = i;
				while (number[j] <= number[i - 1])
					++j;
				char c = number[j];
				number[j] = number[i - 1];
				number[i - 1] = c;
				next = true;
				break;
			}
		}
		if (!next)
		{
			for (int n = 1; n < number.size(); ++n)
				for (int i = 0; i < number.size() - n; ++i)
					if (number[i] > number[i + 1])
					{
						char c = number[i];
						number[i] = number[i + 1];
						number[i + 1] = c;
					}
			char res;
			int pos;
			for (int i = number.size() - 1; i >= 0; --i)
				if (number[i] != '0')
				{
					res = number[i];
					pos = i;
				}
			number[pos] = '0';
			number.insert(number.begin(), res);
		}

		output_file << "Case #" << test << ": " << number << endl;
	}
	input_file.close();
	output_file.close();
	return 0;
}

