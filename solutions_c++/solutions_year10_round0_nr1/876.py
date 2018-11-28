#include <iostream>

using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++) {
		unsigned int n, k;
		cin >> n >> k;
		bool good = true;
		for (int i = 0; i < n; i++)
			good &= (k >> i) & 1;
		if (good) cout << "Case #" << caseno << ": ON" << endl;
		else cout << "Case #" << caseno << ": OFF" << endl;
	}
	return 0;
}
