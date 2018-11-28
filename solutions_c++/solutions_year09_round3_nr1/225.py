#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <math.h>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;

ll power(int a, int b)
{
	ll result = 1;
	for (int i = 0; i < b; ++i)
		result *= a;
	return result;
}

ll convert(vi& num, int base) 
{
	ll result = 0;
	for (int i = num.size() - 1; i >= 0; --i) {
		result += ll(num[i])*power(base, num.size() - 1 - i);
	}
	return result;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("file.out");
	
	int T;
	fin >> T;
	for (int testCase = 1; testCase <= T; ++testCase) {
		fout << "Case #" << testCase << ": ";
		
		int next = 1;
		int zeroUsed = 0;
		vector<int> message;
		map<char, int> meaning;

		string str;
		fin >> str;
		istringstream sin(str);
		char c;
		while (sin >> c, sin) {
			if (meaning.find(c) != meaning.end()) {
				message.push_back(meaning[c]);
			}
			else {
				if (!zeroUsed && next == 2) {
					message.push_back(meaning[c] = 0);
					zeroUsed = 1;
				}
				else {
					message.push_back(meaning[c] = next++);
				}
			}
		}
		int base = meaning.size();
		if (base == 1)
			base = 2;
		ll result = convert(message, base);
		//if (result == 1)
		//	result = 0;
		fout << result << endl;
	}
	return 0;
}
