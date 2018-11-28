#include <iostream>
#include <stdio.h>
using namespace std;

int i, j, k, n, m, T, tt, x, y, z;

int main() {
	freopen("big.in", "r", stdin);	freopen("big.out", "w", stdout);
	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		cin >> n >> k;
		k = k % (1 << n);
		cout << "Case #" << tt << ": ";
		if (k != (1 << n)-1) {
			cout << "OFF" << endl;
		} else {
			cout << "ON" << endl;
		}
	}
	return 0;
}



