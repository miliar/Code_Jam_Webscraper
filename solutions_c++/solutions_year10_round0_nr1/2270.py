#include<iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int k, n;
		cin >> n;
		cin >> k;
		bool on = true;
		for (int j = 0; j < n; ++j) {
			if (k % 2 == 0) {
				on = false;
				break;
			}
			k /= 2;
		}
		if (on) {
			cout << "Case #" << i + 1 << ": ON" << endl;
		} else {
			cout << "Case #" << i + 1 << ": OFF" << endl;
		}
	}

	return 0;
}