/*
 * warning.cpp
 *
 *  Created on: 08/mag/2010
 *      Author: mesh
 */

#include <iostream>

using namespace std;

int g[10000000];
int groups[10000000];
unsigned long long sums[10000000];

int main() {
	int t;
	cin >> t;

	for (int cas3 = 1; cas3 <= t; cas3++) {
		int r, k, n;
		cin >> r >> k >> n;

		for (int i = 0; i < n; i++) {
			cin >> g[i];
		}

		for (int i = 0; i < n; i++) {
			int j = i, sum = 0;

			while (sum + g[j] <= k) {
				sum += g[j];
				j = (j + 1) % n;

				if (j == i)
					break;
			}
			groups[i] = j;
			sums[i] = sum;
		}

		unsigned long long earn = 0LL;
		int i = 0;
		for (int _i = 0; _i < r; _i++) {
			earn += sums[i];
			i = groups[i];
		}

		cout << "Case #" << cas3 << ": " << earn << endl;
	}
}
