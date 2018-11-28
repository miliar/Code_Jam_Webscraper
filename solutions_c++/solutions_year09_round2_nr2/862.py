//============================================================================
// Name        : ProblemB.cpp
//============================================================================

#include <algorithm>
#include <bitset>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <utility>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

inline void skipNL() {
	string line;
	getline(cin, line);
}

string solveTestCase(string x) {
	bool flag = next_permutation(x.begin(), x.end());
	if (!flag) {
		x += "0";
		sort(x.begin(), x.end());
		string::iterator it;
		for (it = x.begin(); (it != x.end()) && (*it == '0'); it++) ;
		if (it != x.end()) {
			swap(*(x.begin()), *it);
		}
	}
	return x;
}

int main(int argc, const char *argv[]) {
	if (argc != 1) {
		cerr << "Redundant arguments!" << endl;
		return 0;
	}

	int testCount;
	cin >> testCount;
	skipNL();

	for (int testNo = 1; testNo <= testCount; testNo++) {
		string N;
		getline(cin, N);
		cout << "Case #" << testNo << ": " << solveTestCase(N) << endl;
	}

	return 0;
}
