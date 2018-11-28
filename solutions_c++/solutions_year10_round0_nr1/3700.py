//using namespace System;
#include <iostream>

using namespace std;

int t, n, k;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> t;
	for (int i = 0; i<t; i++) {
		cin >> n >> k;
		int b = 1;
		for (int j = 0; j<n; j++) {
			b <<= 1;
		}
		cout << "Case #" << i+1 << ": ";
		if ((k+1)%b == 0)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
};