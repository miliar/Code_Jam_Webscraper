#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int caseNum = 1; caseNum <= T; caseNum++) {
		int N, K;
		cin >> N >> K;

		int mask = (1<<N)-1;
		bool result = (K & mask) == mask;

		cout << "Case #" << caseNum << ": " << (result ? "ON" : "OFF") << endl;
	}
}
