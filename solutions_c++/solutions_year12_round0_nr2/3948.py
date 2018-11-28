#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void solveCase(int caseNum) {
	int N, S, p, t, low, high, potential = 0, good = 0;
	cin >> N >> S >> p;
	low = p + 2 * max(0, p - 2);
	high = p + 2 * max(0, p - 1);
	for (int i = 0; i < N; ++i) {
		cin >> t;
		if (low <= t && t < high)
			++potential;
		else if (high <= t)
			++good;
	}
	cout << "Case #" << caseNum << ": " << min(S, potential) + good << endl;
}

int main() {
	int t;

	cin >> t;
	for (int i = 1; i <= t; ++i)
		solveCase(i);

	return EXIT_SUCCESS;
}
