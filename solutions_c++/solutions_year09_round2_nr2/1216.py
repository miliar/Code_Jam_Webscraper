#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <functional>
#include <limits>

using namespace std;

void Inc(vector<int>& digits, int from) {
	if (digits[from] == 0) {
		Inc(digits, from + 1);
		return;
	}
	if (from == static_cast<int>(digits.size() - 1)) {
		int i = 0;
		while (digits[i] == 0)
			++i;
		digits.push_back(digits[i]);
		digits[i] = 0;
		sort(digits.begin(), digits.begin() + from + 1, greater<int>());
		return;
	}
	if (digits[from + 1] == 0) {
		int i = 0;
		while (digits[i] == 0)
			++i;
		digits[from + 1] = digits[i];
		digits[i] = 0;
		sort(digits.begin(), digits.begin() + from + 1, greater<int>());
		return;
	}
	if (digits[from] > digits[from + 1]) {
		int posMin = -1;
		int valMin = numeric_limits<int>::max();
		for (int i = 0; i <= from; ++i) {
			if (digits[i] != 0 && digits[i] > digits[from + 1] && digits[i] < valMin) {
				valMin = digits[i];
				posMin = i;
			}
		}
		swap(digits[posMin], digits[from + 1]);
		sort(digits.begin(), digits.begin() + from + 1, greater<int>());
		return;
	}
	Inc(digits, from + 1);
}

int main(int argc, char* argv[])
{
	if (argc != 2)
		return 1;

	ifstream ifs(argv[1]);
	string dummy;

	int T;
	ifs >> T;
	getline(ifs, dummy);

	for (int testCase = 0; testCase < T; ++testCase) {
		getline(ifs, dummy);

		vector<int> digits;
		for (int i = dummy.size() - 1; i >= 0; --i) {
			digits.push_back(dummy[i] - '0');
		}

		for (size_t i = 0; i < digits.size(); ++i)
			cerr << digits[i] << ", ";
		cerr << endl;

		Inc(digits, 0);

		// output
		cout << "Case #" << testCase + 1 << ": ";
		for (int i = (int)digits.size() - 1; i >= 0; --i)
			cout << digits[i];
		cout << endl;
	}

	return 0;
}
