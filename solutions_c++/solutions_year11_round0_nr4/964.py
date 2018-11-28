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
	vector<unsigned int> arr(N);
	for (unsigned int i = 0; i < N; ++i) {
		cin >> arr[i];
	}

	unsigned int onPlace = 0;
	for (unsigned int i = 0; i < N; ++i) {
		if (arr[i] == i+1) {
			++onPlace;
		}
	}	
	unsigned int r = N - onPlace;
	cout << (r) << endl;
}

int main() {
	unsigned int T; cin >> T;
	for (unsigned int t = 0; t < T; ++t) {		
		outCase(t);
		testCase();		
	}

	return 0;
}