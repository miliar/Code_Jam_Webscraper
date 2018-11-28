#include <fstream>
//#include <iostream>
#include <cmath>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

#define cin in
#define cout out

unsigned long long n, k;
int t;

int main() {
	cin >> t;

	for (int tt = 0; tt < t; ++tt) {
		cin >> n >> k;
		cout << "Case #" << tt + 1 << ": ";

		unsigned long long x = 1;
		for (int i = 0; i < n; ++i) x *= 2;

		if ((k + 1) % x) cout << "OFF\n";
		else cout << "ON\n";
	}

	return 0;
}
