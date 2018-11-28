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
	long long n, pd, pg;
	cin >> n >> pd >> pg;

	if ( (pg == 100) && (pd != 100) ) {
		cout << "Broken" << endl;
		return;
	}

	if ( (pg == 0) && (pd != 0)) {
		cout << "Broken" << endl;
		return;
	}

	long long limit = 100;

	for (long long i = 1; i <= min(limit, n); i++) {
		if ((i * pd) % 100 == 0) {
			long long j = (i * pd) / 100;
				cout << "Possible" << endl;
				return;
		}
	}
	cout << "Broken" << endl;
}
