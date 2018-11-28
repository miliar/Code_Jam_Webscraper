#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

int N;

int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {

		cin >> N;

		int time1 = 0, time2 = 0;
		int at1 = 1, at2 = 1;

		int timez = 0;

		for (int i = 0; i < N; ++i) {
			int dest;
			char col;

			cin >> col >> dest;

			if (col == 'O') {
				int walk = abs(at1 - dest);
				timez = max(timez, time1 + walk);
				at1 = dest;
				time1 = timez + 1;
			} else {
				int walk = abs(at2 - dest);
				timez = max(timez, time2 + walk);
				at2 = dest;
				time2 = timez + 1;
			}
			timez++;
		}

		cout << "Case #" << tt << ": ";

		cout << timez;

		cout << endl;
	}
	return 0;
}

