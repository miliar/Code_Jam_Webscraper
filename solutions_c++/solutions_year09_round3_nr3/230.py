#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <math.h>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("file.out");
	
	int T;
	fin >> T;
	for (int testCase = 1; testCase <= T; ++testCase) {
		fout << "Case #" << testCase << ": ";
		
		int P,Q;
		fin >> P >> Q;
		vector<int> released(Q);
		for (int i = 0; i < Q; ++i)
			fin >> released[i];
		int minResult = 1000000000;
		do {
			int result = 0;
			vi cells(P+2,1);
			cells[0] = cells[P+1] = 0;
			for (int i = 0; i < Q; ++i) {
				cells[released[i]] = 0;
				for (int j = released[i] - 1; cells[j]; --j)
					result++;
				for (int j = released[i] + 1; cells[j]; ++j)
					result++;
			}
			if (result < minResult)
				minResult = result;
		} while(next_permutation(released.begin(), released.end()));
		fout << minResult << endl;

	}
	return 0;
}
