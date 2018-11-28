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

	int n, s, p;
	cin >> n >> s >> p;
	int * scores = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> scores[i];
	}
	sort(scores, scores+n);
	int result = 0;
	for (int i = n-1; i >= 0; i--) {
		if (scores[i] > 2) {
			if (scores[i] >= p*3-2) {
				result++;
			} else if (scores[i] >= p*3-4) {
				if (s > 0) {
					s--;
					result++;
				} else {
					break;
				}
			} else {
				break;
			}
		} else {
			if (p > scores[i])
				break;
			else if (p == scores[i]) {
				if (scores[i] == 2) {
					if (s > 0) {
						s--;
						result++;
					} else {
						break;
					}
				} else {
					result++;
				}
			} else {
				result++;
			}
		}
	}

	cout << result << endl;
//	for (int i = 0; i < n; i++) {
//		cout << scores[i] << " ";
//	}
//	cout << endl;
}
