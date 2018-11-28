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


int _tmain(int argc, _TCHAR* argv[])
{ 
	ifstream infile("E:\\input.txt");
	ofstream outfile("E:\\output.txt");

	int N;
	string line;
	vector<string> vline;

	getline(infile, line);
	N = atoi(line.c_str());

	for (int i = 0; i < N; ++i)
	{
		getline(infile, line);
		int n;
		n = atoi(line.c_str());
		getline(infile, line);
		vline = tokenize(line);
		vector<int> vInt;
		for (int j = 0; j < vline.size(); ++j)
			vInt.push_back(atoi(vline[j].c_str()) - 1);

		double res = 0;
		vector<int> index(n, 0);
		for (int j = 0; j < n; ++j)
		{
			if (index[j] == 0)
			{
				int len = 0;
				int k = j;
				do
				{
					index[k] = 1;
					len++;
					k = vInt[k];
				}
				while (k != j);

				if (len > 1)
					res += len;
			}
		}
		 
		
		outfile << "Case #" << i + 1 << ": " << res << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}
