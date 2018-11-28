#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main (void) {
	int cases;
	cin >> cases;
	int lowerBound;
	int tmpBound;
	int length;
	int lengthMult;
	int upperBound;
	int possibilities;
	unordered_map<int, bool> hitMap;

	int tmpNum;
	int tmpVal;
	int tmpVal_old;
	for (int i = 0; i < cases; i++) {
		possibilities = 0;
		length = 1;
		lengthMult = 1;
		cout << "Case #" << i + 1 << ": ";
		cin >> lowerBound >> upperBound;
		tmpBound = lowerBound;
		while (tmpBound >= 10) {
			length++;
			lengthMult*=10;
			tmpBound /= 10;
		}
		while(lowerBound < upperBound) {
			tmpVal_old = lowerBound;
			hitMap.clear();
			for (int i = 0; i < length - 1; i++) {
				tmpNum = tmpVal_old % 10;
				tmpVal = (tmpVal_old / 10) + (tmpNum * lengthMult);
				if (tmpVal != tmpVal_old && tmpVal > lowerBound && tmpVal <= upperBound && hitMap.count(tmpVal) == 0) {
					possibilities++;
					hitMap[tmpVal] = true;
				}
				tmpVal_old = tmpVal;
			}
			lowerBound++;
			if (lowerBound == lengthMult * 10) {
				length++;
				lengthMult *= 10;
			}
		}
		cout << possibilities << endl;
	}
}