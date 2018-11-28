#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int L, P, C;
		cin >> L >> P >> C;
		int divs, tests;
		for (divs = 0; L*C < P; ++divs) L = L*C;
		for (tests = 0; divs > 0; ++tests) divs = (divs-1)/2 + (divs-1)%2;
		cout << "Case #" << cas << ": " << tests << endl;
	}
}