#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

void task2(const char* in_filename, const char* out_filename)
{
	ifstream in(in_filename);
	ofstream out(out_filename);

	if (in.is_open())
	{
		int T;
		string line;

		getline(in, line);
		T = atoi(line.c_str());	
		
		// T - cases count		
		for (unsigned int caseNumber = 1; caseNumber <= T; ++caseNumber) {
			
			getline(in, line);
			vector<char> digitsChars(line.begin(), line.end());
			vector<int> digits(digitsChars.size());			
			for (int i = 0; i < digits.size(); ++i) {
				digits[i] = atoi(string(1, digitsChars[i]).c_str());
			}
			vector<int> digits_copy(digits);

			if (next_permutation(digits_copy.begin(), digits_copy.end()))
			{
				out << "Case #" << caseNumber << ": ";
				for (int i = 0; i < digits_copy.size(); ++i) {
					out << digits_copy[i];
				}
				out << endl;
			}
			else
			{
				digits.push_back(0);
				sort(digits.begin(), digits.end());
				int zerosCount = count(digits.begin(), digits.end(), 0);
				out << "Case #" << caseNumber << ": ";
				out << digits[zerosCount];
				for (int i = 0; i < zerosCount; ++i) {
					out << "0";
				}
				for (int i = zerosCount + 1; i < digits.size(); ++i) {
					out << digits[i];
				}
				out << endl;
				//out << "0" << digits[digits.size() - 1] << endl;

			}			
		}
	}
	else
	{
		throw "File not found";
	}
	in.close();
	out.close();
}


int _tmain(int argc, _TCHAR* argv[])
{
	//task1("D:\\C-large.in", "D:\\C-large.out");
	task2("D:\\B-small-attempt1.in", "D:\\B-small-attempt1.out");
	//task2("D:\\bbb.in", "D:\\bbb.out");
	return 0;
}

