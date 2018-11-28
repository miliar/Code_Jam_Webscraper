/*
 * snapper.cpp
 *
 *  Created on: 08/mag/2010
 *      Author: mesh
 */

#include <iostream>

#define ull unsigned long long

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		ull n, k;
		cin >> n >> k;

		ull pow = (ull)(2) << (n-1);

		k %= pow;

		bool ok = true;
		for (int j = 0; j < n; j++) {
			if (k % 2 == 0) {
				ok = false;
				break;
			}

			k /= 2;
		}

		cout << "Case #" << i+1 << ": " << (ok ? "ON" : "OFF") << endl;
	}
}
