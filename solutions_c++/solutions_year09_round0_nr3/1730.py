#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

void task3(const char* in_filename, const char* out_filename)
{
	ifstream in(in_filename);
	ofstream out(out_filename);
	//in >> noskipws;
	//out << noskipws;
	if (in.is_open())
	{
		unsigned int N;
		string s;

		in >> N;
		getline (in, s);
		// N - cases count		
		for (unsigned int caseNumber = 1; caseNumber <= N; ++caseNumber) {
			
			//in >> s;
			getline(in,s);
			unsigned int states[19];		
			for (unsigned int i = 0; i < 19; ++i) states[i] = 0;

			// "welcome to  code jam"
			//  01234567891012345678
			for (unsigned int pos = 0; pos < s.size(); ++pos) {
				switch (s[pos]) {
					case 'w':
						states[0] += 1;
						break;
					case 'e':
						states[1] += states[0];
						states[6] += states[5];
						states[14] += states[13];
						break;
					case 'l':
						states[2] += states[1];
						break;
					case 'c':
						states[3] += states[2];
						states[11] += states[10];
						break;
					case 'o':
						states[4] += states[3];
						states[9] += states[8];
						states[12] += states[11];
						break;
					case 'm':
						states[5] += states[4];
						states[18] += states[17];
						break;
					case ' ':
						states[7] += states[6];
						states[10] += states[9];
						states[15] += states[14];
						break;
					case 't':
						states[8] += states[7];
						break;
					case 'd':
						states[13] += states[12];
						break;
					case 'j':
						states[16] += states[15];
						break;
					case 'a':
						states[17] += states[16];
						break;					
				}
				for (unsigned int i = 0; i < 19; ++i) states[i] %= 10000;
			}

			// "welcome to  code jam"
			//  01234567891012345678
			
			out << "Case #" << caseNumber << ": ";
			if (states[18] < 10) out << "000" << states[18];
			else if (states[18] < 100) out << "00" << states[18];
			else if (states[18] < 1000) out << "0" << states[18];
			else out << states[18];

			out << endl;			
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
	task3("D:\\C-.in", "D:\\C-.out");
	//task3("D:\\ccc.in", "D:\\ccc.out");
	return 0;
}

