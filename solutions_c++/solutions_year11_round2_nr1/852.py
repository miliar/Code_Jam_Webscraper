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

		int N = atoi(line.c_str());
		vector<string> outcome;

		for (int j = 0; j < N; ++j)
		{
			getline(infile, line);		
			outcome.push_back(line);
		}

		vector<int> ngames(N, 0);
		vector<int> wgames(N, 0);
		vector<double> wp(N, 0);
		vector<double> owp(N, 0);		
		vector<double> oowp(N, 0);	
		vector<double> res(N);

		for (int j = 0; j < N; ++j)
		{
			string str = outcome[j];
			for (int k = 0; k < N; ++k)
			{
				char c = str[k];
				if (c == '.')
					continue;

				ngames[j]++;
				if (c == '1')
					wgames[j]++;
			}
			wp[j] = wgames[j] / ((double) ngames[j]);
		}

		for (int j = 0; j < N; ++j)
		{
			string str = outcome[j];
			double wpsum = 0.0;
			int cnt = 0;
			for (int k = 0; k < N; ++k)
			{
				char c = str[k];
				if (c == '.')
					continue;
				
				if (c == '0')
					wpsum += (wgames[k] - 1) / (ngames[k] - 1.0);
				else
					wpsum += wgames[k] / (ngames[k] - 1.0);				 

				cnt++;
			}
			owp[j] = wpsum / cnt;
		}

		for (int j = 0; j < N; ++j)
		{
			string str = outcome[j];
			double owpsum = 0.0;
			int cnt = 0;
			for (int k = 0; k < N; ++k)
			{
				char c = str[k];
				if (c == '.')
					continue;
				
				owpsum += owp[k];
				cnt++;
			}
			oowp[j] = owpsum / cnt;
			res[j] = 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j];
		}


		outfile << "Case #" << i + 1 << ": " << endl;
		for (int j = 0; j < N; ++j)
		{
			ostringstream os;
			os.precision(12);
			os << res[j];			
			outfile << os.str() << endl;				 
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

