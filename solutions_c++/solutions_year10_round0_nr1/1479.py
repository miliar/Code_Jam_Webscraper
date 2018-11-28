#include <iostream>
#include <vector>

using namespace std;


int main() {
	int test_cases;
	cin >> test_cases;
	for (int test = 1; test <= test_cases; ++test) {
		int n, k;
		cin >> n >> k;
		int p = 1 << n;
		if (k % p == p - 1) {			
			cout << "Case #" << test << ": " << "ON" << endl;
		}
		else {
			cout << "Case #" << test << ": " << "OFF" << endl;
		}
	}
	return 0;
}

/*

int main() {
	int test_cases;
	cin >> test_cases;
	for (int test = 1; test <= test_cases; ++test) {
		int n, k;
		cin >> n >> k;
		int p = 1;
		p = p << (n-1);
		if ((k / p) % 2 == 1) {
			cout << "Case #" << test << ": " << "ON" << endl;
		}
		else {
			cout << "Case #" << test << ": " << "OFF" << endl;
		}
	}
	return 0;
}

*/