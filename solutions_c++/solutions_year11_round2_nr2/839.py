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

double distance(double pos, vector<pair<int, int> >& PV, double len, int D)
{
	double res = len;
	double tmp = 0;	 
	for (int j = 0; j < PV.size(); ++j)
	{
		for (int k = 0; k < PV[j].second; ++k)
		{
			if (pos > PV[j].first)
				tmp = max(tmp, pos - PV[j].first);
			else
				tmp = max(tmp, PV[j].first - pos);
			 
			pos += D;
		}
	}
	res = min(tmp, res);

	return res;
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

		int C = atoi(vline[0].c_str());
		int D = atoi(vline[1].c_str());
		  
		vector<int> P;

		int total = 0;
		
		for (int j = 0; j < C; ++j)
		{
			getline(infile, line);				
			vline = tokenize(line);				
			for (int k = 0; k < atoi(vline[1].c_str()); ++k)
				P.push_back(atoi(vline[0].c_str()));			

			total += atoi(vline[1].c_str());
		}
		
		double res = 0;

		for(int j = 0; j < P.size(); ++j)
		{
			for (int k = j + 1; k < P.size(); ++k)
			{
				double required = (k - j) * D;
				res = max(res, (required - (P[k] - P[j])) / 2.0);
			}
		}		
	 		 

		outfile << "Case #" << i + 1 << ": " << res << endl;
		 
	}

	infile.close();
	outfile.close();
}


int _tmain(int argc, _TCHAR* argv[])
{ 
	codejam();

	return 0;
}

