// Testing.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[]) {
	ifstream ifile("C:\\Testing\\Debug\\smallest.txt");
	ofstream ofile("C:\\Testing\\Debug\\out.txt");
	vector<string> svec;
	copy(istream_iterator<string>(ifile),
		istream_iterator<string>(),
		back_inserter(svec));

	const int T = atoi(svec[0].c_str());
	int counter = 0;
	for (int i = 0; i < T; ++i) {
		const long long unsigned int L = atoi(svec[++counter].c_str());
		const long long unsigned int P = atoi(svec[++counter].c_str());
		const int C = atoi(svec[++counter].c_str());
		long long unsigned int value = P;
		int count = 0;
		int tmp1 = 0;
		if (value%C)
			tmp1 = 1;
		value = value/C + tmp1;
		while (value > L) {
			++count;
			int tmp = 0;
			if (value%C)
				tmp = 1;
			value = value/C + tmp;
		}
		
		unsigned int result = 0;
		if (count == 0)
			result= 0;
		else if (count == 1)
			result = 1;
		else if (count == 2)
			result = 2;
		else {
			while (count > 2) {
				result++;
				count = count/2;
			}
			result += count;
		}

		ofile << "Case #" << i+1 << ": " << result << endl;
	}

	return 0;
}

