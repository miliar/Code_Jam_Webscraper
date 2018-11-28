/*
 *  Created on: Sep 26, 2009
 *      Author: Ramesh Rajaby
 */

#include <iostream>
#include <cmath>

using namespace std;


struct Plant {
	int x, y, r;
} plants[10];


double sqr(double x) {
	return x*x;
}


int last(int i, int j) {
	if (i != 0 && j != 0) {
		return 0;
	} else if (i != 1 && j != 1) {
		return 1;
	} else {
		return 2;
	}
}


int main() {
	int c;

	cin >> c;
	for (int t = 0; t < c; t++) {
		int n;
		cin >> n;

		for (int i = 0; i < n; i++) {
			cin >> plants[i].x >> plants[i].y >> plants[i].r;
		}

		cout << "Case #" << t+1 << ": ";
		if (n <= 2) {
			int r = 0;
			for (int i = 0; i < n; i++) {
				r = max(r, plants[i].r);
			}
			cout << r << endl;
			continue;
		}

		double r = 1000000;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (i != j) {
					double d = sqrt(sqr(plants[i].x-plants[j].x) + sqr(plants[i].y-plants[j].y));
					r = min(r, max((plants[i].r + plants[j].r + d)/2,
								   (double)plants[last(i, j)].r));
				}
			}
		}

		cout << r << endl;
	}
}

