#include <string>
#include <iostream>
#include <cstdlib>

using namespace std;




int main () {
	int cases;
	cin >> cases;

	for (int i0 = 1; i0 <= cases; ++i0) {
		int stepsB = 0,
			stepsO = 0,
			posB   = 1,
			posO   = 1;
			
		int buttons;
		cin >> buttons;

		//init
		string	who;
		int		pos;
		cin >> who >> pos;
		string last = who;
		while (last == who && buttons > 0) {
			if (who == "B") {
				stepsB += abs(pos - posB) + 1;
				posB	= pos;
			}
			else {
				stepsO += abs(pos - posO) + 1;
				posO	= pos;
			}
			if (--buttons > 0)
				cin >> who >> pos;
		}

		for (int j = 0; j < buttons;) {
			if (who == "B") {
				stepsB += abs(pos - posB);
				posB	= pos;
				if (stepsB < stepsO)
					stepsB = stepsO;
				stepsB += 1;
			}
			else {
				stepsO += abs(pos - posO);
				posO	= pos;
				if (stepsO < stepsB)
					stepsO = stepsB;
				stepsO += 1;
			}
			if (++j < buttons) {
				cin >> who >> pos;
			}
		}

		int total = stepsB > stepsO ? stepsB : stepsO;
		cout << "Case #" << i0 << ": " << total << endl;
	}
}