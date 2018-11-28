#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {
	ifstream cin(argv[1]);

	int numTests;
	cin >> numTests;

	for (int cc = 0; cc < numTests; cc++) {
		int numButtons;
		cin >> numButtons;

		int oLastPos = 1;
		int oLastAction = 0;
		int bLastPos = 1;
		int bLastAction = 0;

		int lastButtonPressTime = 0;

		for (int i = 0; i < numButtons; i++) {
			char robotToPress;
			cin >> robotToPress;
			int buttonToPress;
			cin >> buttonToPress;

			if (robotToPress == 'O') {
				int spacesToMove = abs(oLastPos - buttonToPress);
				oLastPos = buttonToPress;
				oLastAction += spacesToMove + 1;

				if (oLastAction <= lastButtonPressTime) {
					oLastAction = lastButtonPressTime + 1;
				}
				lastButtonPressTime = oLastAction;
			} else {
				int spacesToMove = abs(bLastPos - buttonToPress);
				bLastPos = buttonToPress;
				bLastAction += spacesToMove + 1;

				if (bLastAction <= lastButtonPressTime) {
					bLastAction = lastButtonPressTime + 1;
				}
				lastButtonPressTime = bLastAction;
			}
		}

		cout << "Case #" << cc + 1 << ": " << lastButtonPressTime << endl;
	}
}
