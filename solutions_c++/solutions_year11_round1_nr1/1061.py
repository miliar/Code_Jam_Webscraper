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

	int M;
	string line;
	vector<string> vline;

	getline(infile, line);
	M = atoi(line.c_str());

	for (int i = 0; i < M; ++i)
	{
		 
		getline(infile, line);				
		vline = tokenize(line);	
		long long N = atol(vline[0].c_str());
		int pd = atol(vline[1].c_str());
		int pg = atol(vline[2].c_str());
		string res;
		 
		if (pg == 0 || pg == 100)
		{
			if (pd == pg)
				res = "Possible";
			else 
				res = "Broken";			 
			
		}
		else {
			int cdiv = gcd(pd, 100);			 		
			if (100 / cdiv > N)
				res = "Broken";
			else 
				res = "Possible";
		} 

		
		outfile << "Case #" << i + 1 << ": " + res << endl;				 
	}

	infile.close();
	outfile.close();
}


int _tmain(int argc, _TCHAR* argv[])
{ 
	codejam();

	return 0;
}

