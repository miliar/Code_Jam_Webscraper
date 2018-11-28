/*
 * main.cc
 *
 *  Created on: May 22, 2011
 *      Author: wujj
 */

#include <iostream>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>
#include <algorithm>
#include <iomanip>

using namespace std;

void codeJam();

int main() {

	int num_case;
	cin >> num_case;

	for (int i = 0; i < num_case; i++) {
		cout << "Case #" << i+1 << ": ";
		codeJam();
	}

	return 0;
}

void codeJam() {
	int a, b;
	cin >> a >> b;
	double * x = new double[a];
	double low = 1;
	for (int i = 0; i < a; i++) {
		cin >> x[i];
		low *= x[i];
	}

	/* keep typing */
	double best = low * (b - a + 1) + (1 - low) * (b - a + 1 + b + 1);
//	cout << best << endl;
	/* give up */
	best = min(best, (double)b + 2);
//	cout << best << endl;

	/* backspace */
	double back = 0;
	for (int i = a - 1; i >= 0; i--) {
		low /= x[i];
//		cout << "low: " << low << endl;
		back = a - i + low * (b - i + 1) + (1 - low) * (b - i + 1 + b + 1);
		if (back < best) {
			best = back;
		} else {
			break;
		}
	}

	cout << setprecision(10) << best << endl;
}
