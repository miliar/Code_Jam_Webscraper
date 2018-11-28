#include <stdio.h>
#include <iostream>
#include <fstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>
#include <climits>

using namespace std;

int main(int argc, char* argv[]) {
	fstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}
	string ln; 
	inf >> ln;
	int caseNum = atoi(ln.c_str());
	for (int cn = 0; cn<caseNum; cn++) {
		// read data
		inf >> ln;
		int N = atoi(ln.c_str());
		inf >> ln;
		int low = atoi(ln.c_str());
		inf >> ln;
		int high = atoi(ln.c_str());
		vector<int> others; 
		for (int i=0; i<N; i++) {
			inf >> ln;
			others.push_back(atoi(ln.c_str()));
		}

		int freq = 0; 
		for (int i=low; i<=high; i++) {
			bool possible = true;
			for (int j=0; j<N; j++) {
				if (i / others[j] * others[j] == i){
					continue;
				}
				else if (others[j] / i * i == others[j]) {
					continue;
				}
				else {
					possible = false;
					break;
				}
			}
			if (possible) {
				freq = i;
				break;
			}
		}
		// find solution

		// output
		if (freq == 0)
			cout << "Case #" << cn+1 << ": NO" << endl;
		else
			cout << "Case #" << cn+1 << ": " << freq << endl;
	}
	return 0; 
}