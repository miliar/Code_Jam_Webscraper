#include <iostream>
#include <string>

using namespace std;

int main (void) {
	int cases;
	static string translation = "yhesocvxduiglbkrztnwjpfmaq";
	string currentLine;
	int currentChar;
	cin >> cases;
	getline(cin, currentLine);
	for (int i = 0; i < cases; i++) {
		cout << "Case #" << i + 1 << ": ";
		getline(cin, currentLine);
		for (int j = 0; j < currentLine.length(); j++) {
			currentChar = (int) currentLine[j] ;
			if (currentChar != 32) {
			cout << translation[currentChar - ((int) 'a')];
			} else {
				cout << " ";
			}
		}
		cout << endl;
	}
}