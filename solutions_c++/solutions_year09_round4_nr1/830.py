/*
 *  Created on: Sep 26, 2009
 *      Author: Ramesh Rajaby
 */

#include <iostream>

using namespace std;

int values[50];


int main() {
	int T;

	cin >> T;
	for (int t = 0; t < T; t++) {
		int n;

		cin >> n;
		for (int i = 0; i < n; i++) {
			int value = 0;
			for (int j = 0; j < n; j++) {
				char v;
				cin >> v;

				if (v == '1') {
					value = j;
				}
			}

			values[i] = value;
		}

		int swaps = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i; j < n; j++) {
				if (values[j] <= i) {
					swaps += j-i;
					for (int k = j; k > i; k--) {
						values[k] = values[k-1];
					}
					break;
				}
			}

			/**for (int j = 0; j < n; j++) {
				cout << values[j] << " ";
			} cout << " : " << swaps << endl;*/
		}

		cout << "Case #" << t+1 << ": " << swaps << endl;
	}
}

