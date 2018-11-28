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
		const int N = atoi(svec[++counter].c_str());
		vector<int> ax;
		vector<int> bx;
		for (int j = 0; j < N ;++j) {
			int valuea = atoi(svec[++counter].c_str());
			int valueb = atoi(svec[++counter].c_str());
			ax.push_back(valuea);
			bx.push_back(valueb);
		}
		long long unsigned int intercount = 0;
		for (int j = 0; j < N; j++) {
			for (int k = j+1; k < N; ++k) {
				if( (ax[j] > ax[k]) && (bx[j] < bx[k]))
					intercount++;
				if( (ax[j] < ax[k]) && (bx[j] > bx[k]))	
					intercount++;
			}
		}
			

		ofile << "Case #" << i+1 << ": " << intercount << endl;
	}

	return 0;
}

