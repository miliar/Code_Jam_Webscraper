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

		long long L = atoi(vline[0].c_str());
		long long t = atoi(vline[1].c_str());
		long long N = atoi(vline[2].c_str());
		long long C = atoi(vline[3].c_str());
		
		
		vector<long long> seq, dist, rm;

		for (int j = 4; j < vline.size(); ++j)
			seq.push_back(atoi(vline[j].c_str()));		
		
		int j = 0;
		int cnt = 0;
		while(j < N)
		{
			cnt = cnt % C;
			dist.push_back(seq[cnt]);
			j++;		
			cnt++;
		}

		long long res = 0;

		long long sofar = 0;
		int id = - 1;
		for (int j = 0; j < dist.size(); ++j)		
		{
			sofar += 2 * dist[j];
			if (sofar > t)
			{
				id = j;
				break;
			}
			//res += 2 * dist[j];
		}		
		 
		res = t;
		dist[id] = (sofar - t) / 2;

		for (int j = id; j < dist.size(); ++j)
		{
			rm.push_back(dist[j]);
			res += 2 * dist[j];
		}

		sort(rm.begin(), rm.end(), greater<long long>());

		for (int j = 0; j < min(L, (long long)rm.size()); ++j)
		{
			res -= rm[j];
		}

		 
		ostringstream os;
		os.precision(16);
		//os << res;

		string strres = os.str();

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

