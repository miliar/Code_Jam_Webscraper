#pragma once
#include "stdafx.h"  
//#include "vec.h"
//#include "BinaryTree.h"
//#include "lib.h"
//#include "exercise.h"
//#include "career_cup.h"


#include <vector>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iterator>
#include <limits>
#include <functional>
#include <cmath>
#include <stdio.h>
#include <time.h>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <cctype>
#include <string>
#include <typeinfo>

using namespace std;

vector<string> tokenize(const string& str, const string& delimiters = " ")
{     
	vector<string> tokens;
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);     
	string::size_type pos  = str.find_first_of(delimiters, lastPos);

	while (string::npos != pos || string::npos != lastPos)
	{         
		tokens.push_back(str.substr(lastPos, pos - lastPos));         
		lastPos = str.find_first_not_of(delimiters, pos);        
		pos = str.find_first_of(delimiters, lastPos);
	}

	return tokens;
}

int gcd(int a, int b)
{
	a = a > 0 ? a : - a;
	b = b > 0 ? b : - b;

	if (a > b)
		return gcd(b, a);

	if (a == 0)
		return b;

	return gcd(b % a, a);
}

void codejam() {
	ifstream infile("E:\\input.txt");
	ofstream outfile("E:\\output.txt");

	int T;
	string line;
	vector<string> vline;

	getline(infile, line);
	T = atoi(line.c_str());

	for (int i = 0; i < T; ++i)
	{
		getline(infile, line);				
		vline = tokenize(line);	

		int R = atoi(vline[0].c_str());
		int C = atoi(vline[1].c_str());

		vector<string> tilt;

		for (int j = 0; j < R; ++j)
		{
			getline(infile, line);			
			tilt.push_back(line);
		}

		string res;
		for (int j = 0; j < R; ++j)
		{
			for (int k = 0; k < C; ++k)
			{
				char c = tilt[j][k];

				if (c == '.')
					continue;

				if (c == '#')
				{
					if ((j == (R - 1)) || (k == (C - 1)))
						res = "Impossible";
					else if (tilt[j + 1][k] != '#' || tilt[j][k + 1] != '#' || tilt[j + 1][k + 1] != '#')
						res = "Impossible";
					else
					{
						tilt[j][k] = '/';
						tilt[j][k + 1] = '\\';
						tilt[j + 1][k] = '\\';
						tilt[j + 1][k + 1] = '/';
					}
							
				}
			}
		}

		 
		ostringstream os;
		os.precision(16);
		//os << res;

		string strres = os.str();

		outfile << "Case #" << i + 1 << ": " << endl;

		if (res == "Impossible")
			outfile << res << endl;
		else {
			for (int j = 0; j < R; ++j)
				outfile << tilt[j] << endl;
		}
		 
	}

	infile.close();
	outfile.close();
}


int _tmain(int argc, _TCHAR* argv[])
{ 
	codejam();

	return 0;
}

