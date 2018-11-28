#include <iostream>
#include <string>

using namespace std;

int main (void) {
	int cases;
	static string translation = "yhesocvxduiglbkrztnwjpfmaq";
	string currentLine;
	int currentChar;
	int googlers;
	int surprises;
	int threshold;

	cin >> cases;
	getline(cin, currentLine);
	int tmpSum;
	int certainMatch;
	int possibleMatch;

	for (int i = 0; i < cases; i++) {
		certainMatch = 0;
		possibleMatch = 0;
		cin >> googlers >> surprises >> threshold;
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < googlers; j++) {
			cin >> tmpSum;
			if (tmpSum > 0 && (tmpSum == threshold*3 - 3 || tmpSum == threshold*3 - 4)) {
				possibleMatch++;
			} else if (tmpSum > threshold*3 -3) {
				certainMatch++;
			}
		}

		cout << (certainMatch + ((possibleMatch > surprises) ? surprises : possibleMatch)) << endl;
	}
}