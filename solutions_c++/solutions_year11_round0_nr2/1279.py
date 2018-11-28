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
		map<pair<char, char>, char> basepair;
		set<pair<char, char>> opposepair;

		getline(infile, line);				
		vline = tokenize(line);
		int cnt = 0;
		int n;
		n = atoi(vline[cnt].c_str());		
		cnt++;
		for (int j = 0; j < n; ++j)
		{
			string crt = vline[cnt];
			pair<char, char> p(crt[0], crt[1]);
			basepair[p] = crt[2];
			swap(p.first, p.second);
			basepair[p] = crt[2];			 
			cnt++;
		}
		
		n = atoi(vline[cnt].c_str());		
		cnt++;
		for (int j = 0; j < n; ++j)
		{
			string crt = vline[cnt];
			pair<char, char> p(crt[0], crt[1]);
			opposepair.insert(p);
			swap(p.first, p.second);
			opposepair.insert(p);			 
			cnt++;
		}

		n = atoi(vline[cnt].c_str());
		cnt++;
		string str = vline[cnt];
		//list<char> lst(str.begin(), str.end());
		list<char> rlst;

		string res;	 
				 
		rlst.push_back(str[0]);
		for (int j = 1; j < str.size(); ++j) {			
			rlst.push_back(str[j]);
			while (rlst.size() >= 2) {
				char b = rlst.back();
				list<char>::reverse_iterator it = rlst.rbegin();
				it++;
				char c = *it;
				map<pair<char,char>, char>::iterator iter = basepair.find(pair<char, char>(b, c));
				if (iter !=  basepair.end()) {
					rlst.pop_back();
					rlst.back() = iter->second;
				} 			
				else {
					break;
				}
			}

			char b = rlst.back();
			list<char>::iterator it = rlst.begin();
			while (it != rlst.end()) {
				char c = *it++;
				if (opposepair.find(pair<char, char>(b, c)) != opposepair.end()) {
					rlst.clear();
					break;
				}
			}
			 
		}



		list<char>::iterator it = rlst.begin();
		while (it != rlst.end())
			res += *it++;
	 

		
		outfile << "Case #" << i + 1 << ": [";		
		if (!res.empty()) {
			for (int j = 0; j < (res.size() - 1); ++j)
				outfile << res[j] << ", ";
			outfile << res[res.size() - 1];
		}
		outfile << "]" << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}
