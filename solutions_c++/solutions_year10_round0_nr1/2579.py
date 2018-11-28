#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

void snap(vector<bool>& states) {
	int i = 0;
	while (i < states.size() && states[i++]);
	while (i--) {
		states[i] = !states[i];
	}
}

bool isPowerOn(const vector<bool>& states) {
	for (int i = 0; i < states.size(); ++i) {
		if (!states[i])
			return false;
	}

	return true;
}

int main(int argc, char* argv[]) {
	
	string token;
	istream& in = cin;

	in >> token;
	int numTestCases = atoi(token.c_str());

	for (int testCase = 1; testCase <= numTestCases; ++testCase) {

		int n = 0, k = 0;
		in >> token; n = atoi(token.c_str());
		in >> token; k = atoi(token.c_str());

		vector<bool> states(n);
		while (k--) {
			snap(states);
		}

		cout << "Case #" << testCase << ": " << (isPowerOn(states)?"ON":"OFF") << endl;
	}

	return 0;
}
