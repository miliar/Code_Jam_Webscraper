#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

std::ostream& outCase(unsigned int tc) {
	std::cout << "Case #" << (tc + 1) << ": ";
	return std::cout;
}

void testCase() {
	unsigned int N; cin >> N;
	unsigned int sum = 0;
	unsigned int xsum = 0;
	unsigned int min = -1u;
	unsigned int c;
	for (unsigned int i = 0; i < N; ++i) {
		cin >> c;
		sum += c;
		xsum ^= c;
		if (c < min) {
			min = c;
		}
	}
	if (xsum != 0) {
		cout << "NO" << endl;
	} else {
		unsigned int r = sum - min;
		cout << r << endl;
	}
}

int main() {
	unsigned int T; cin >> T;
	for (unsigned int t = 0; t < T; ++t) {		
		outCase(t);
		testCase();		
	}

	return 0;
}