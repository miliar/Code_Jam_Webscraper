#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

int main() {
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int T;
	cin >> T;

	for (int cc = 1; cc <= T; cc++) {
		cout << "Case #" << cc <<": ";
		int last_time = 0;
		int pO = 1, pB = 1, tO = 0, tB = 0;
		int N;
		cin >> N;
		while (N--) {
			char p; int t;
			cin >> p >> t;
			if (p == 'O') {
				int tt = last_time-tO;
				int need = abs(pO-t);
				last_time += max(0,need-tt)+1;
				pO = t;
				tO = last_time;
			} else {
				int tt = last_time-tB;
				int need = abs(pB-t);
				last_time += max(0,need-tt)+1;
				pB = t;
				tB = last_time;
			}
		}
		cout << last_time << endl;
	}
	return 0;
}