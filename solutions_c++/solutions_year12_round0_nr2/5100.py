//============================================================================
// Name        : CodeJam1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;

int main() {
	short T, N, S, p, t, ctr;
	cin >> T;
	for (unsigned short i = 0; i < T; i++) {
		ctr = 0;
		cin >> N >> S >> p;
		for (unsigned short i = 0; i < N; i++) {
			cin >> t;
			if (t<3) {if (t>=p) {ctr++; continue;} }
			else if (t % 3 == 0) {
				if (t / 3 >= p) {
					ctr++;
					continue;
				} else if (t / 3 + 2 >= p && S != 0) {
					ctr++;
					S--;
					continue;
				}
			} else if (t / 3 + 1 >= p) {
				ctr++;
				continue;
			} else if (t % 3 == 2) {
				if (t / 3 + 2 >= p && S != 0) {
					ctr++;
					S--;
					continue;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << ctr << endl;
	}
	return 0;
}
