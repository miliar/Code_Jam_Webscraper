#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

//                             abcdefghijklmnopqrstuvwxyz
const string decode = string("yhesocvxduiglbkrztnwjpfmaq");

void solveCase(int caseNum) {
	string line;
	getline(cin, line);
	cout << "Case #" << caseNum << ": ";
	for (int i = 0; i < line.size(); ++i) {
		if (line[i] >= 'a' && line[i] <= 'z') {
			cout << decode[line[i] - 'a'];
		} else {
			cout << line[i];
		}
	}
	cout << endl;
}

int main() {
	int t;

	cin >> t;
	cin.ignore();
	for (int i = 1; i <= t; ++i)
		solveCase(i);

	return EXIT_SUCCESS;
}
