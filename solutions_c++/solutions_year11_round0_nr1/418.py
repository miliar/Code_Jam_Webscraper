#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cout << "Invalid input parameters!" << endl;
		return -1;
	}

	ifstream in(argv[1]);
	if (in) {
		int count;
		in >> count;
		int caseNo = 1;
		while(count--) {
			int totalSeconds = 0, oStopAt = 0, bStopAt = 0;
			int buttonCount, oPos = 1, bPos = 1;
			in >> buttonCount;
			while (buttonCount--) {
				char robot;
				int newPos;
				in >> robot >> newPos;
				if (robot == 'O') {
					int timeSinceLastStop = totalSeconds - oStopAt;
					int moveRequiredTime = abs(newPos - oPos);
					if (moveRequiredTime > timeSinceLastStop)
						totalSeconds +=  (moveRequiredTime - timeSinceLastStop);
					totalSeconds++;
					oPos = newPos;
					oStopAt = totalSeconds;
				} else {
					int timeSinceLastStop = totalSeconds - bStopAt;
					int moveRequiredTime = abs(newPos - bPos);
					if (moveRequiredTime > timeSinceLastStop)
						totalSeconds +=  (moveRequiredTime - timeSinceLastStop);
					totalSeconds++;
					bPos = newPos;
					bStopAt = totalSeconds;
				}
			}
			
			cout << "Case #" << caseNo++ << ": " << totalSeconds << endl;
		}
	}

	return 0;
}
