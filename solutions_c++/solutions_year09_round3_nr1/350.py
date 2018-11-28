//============================================================================
// Name        : ProblemA.cpp
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

long long solve(string& msg) {
	map<char, int> digits;
	digits.insert(make_pair(msg.at(0), 1));
	int next = 0;
	for (int i = 1; i < msg.size(); i++) {
		char digit = msg.at(i);
		map<char, int>::iterator pos = digits.find(digit);
		if (pos == digits.end()) {
			digits.insert(make_pair(digit, next));
			if (next == 0) {
				next = 2;
			} else {
				next++;
			}
		}
	}
	long long base = digits.size();
	if (base < 2) {
		base = 2;
	}
	long long result = 0;
	for (int i = 0; i < msg.size(); i++) {
		char digit = msg.at(i);
		map<char, int>::iterator pos = digits.find(digit);
		result = result * base + (long long) (pos->second);
	}
	return result;
}

int main(int argc, const char *argv[]) {

	int testCount;
	cin >> testCount;
	skipNL();

	for (int testNo = 1; testNo <= testCount; testNo++) {
		string message;
		getline(cin, message);
		cout << "Case #" << testNo << ": " << solve(message) << endl;
	}

	return 0;
}
