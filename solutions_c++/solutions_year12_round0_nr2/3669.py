#include <iostream>
using namespace std;


void a() {
	int n, s, p;
	cin >> n;
	cin >> s;
	cin >> p;
	int scores[n];

	int tally = 0;

	for (int i = 0; i < n; i++) {
		cin >> scores[i];
	}

	for (int i = 0; i < n; i++) {
		if (scores[i] % 3 == 0) {
			if (scores[i]/3 < p) {
				if (scores[i]/3 + 1 >= p && s >= 1) {
					if (scores[i]/3 != 0) {
						s--;
						tally++;
					}
				}
			} else {
				tally++;
			}
		} else if (scores[i] % 3 == 1) {
			if (scores[i]/3 + 1 >= p) {
				tally++;
			}
		} else if (scores[i] % 3 == 2) {
			if (scores[i]/3 + 1 >= p) {
				tally++;
			} else if (scores[i]/3 + 2 >= p && s >= 1) {
				s--;
				tally++;
			}
		}
	}
	
	cout << tally;
	return;
}




			




int main() {
	int cases;
	cin >> cases;

	int i;
	for (i = 1; i <= cases; i++) {
		cout << "Case #" << i << ": ";
		a();
		cout << endl;
	}

	return 0;
}
