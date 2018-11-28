#include <iostream>
#include <cstdio>

using namespace std;

void solve(int test) {
	long long n;
	int pD, pG;

	cin >> n >> pD >> pG;

	cout << "Case #" << test << ": ";

	if (pG == 100 && pD < 100) {
		cout << "Broken" << endl;
		return;
	}
	if (pG == 100 && pD == 100) {
		cout << "Possible" << endl;
		return;
	}
	if (pG == 0 && pD == 0) {
		cout << "Possible" << endl;
		return;
	}
	if (pG == 0 && pD > 0) {
		cout << "Broken" << endl;
		return;
	}
	int m = 100;
	while (pD % 2 == 0 && m % 2 == 0) {
		pD /= 2;
		m /= 2;
	}
	while (pD % 5 == 0 && m % 5 == 0) {
		pD /= 5;
		m /= 5;
	}
	if (m <= n) {
		cout << "Possible" << endl;
		return;
	}
	cout << "Broken" << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	cin >> nTest;

	for (int i = 0; i < nTest; i++) {
		solve(i + 1);
	}
	return 0;
}
