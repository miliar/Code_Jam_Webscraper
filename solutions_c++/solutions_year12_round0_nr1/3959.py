#include<iostream>
#include<string>

using namespace std;

string shift = "yhesocvxduiglbkrztnwjpfmaq";
int main() {
	int K;
	cin >> K >> ws;
	for (int k = 1; k <= K; k++) {
		cout << "Case #" << k << ": ";

		string line;
		getline(cin, line);
		for (int i = 0; i < line.length(); i++) {
			if (line[i] >= 'a' && line[i] <= 'z') cout << shift[line[i] - 'a'];
			else cout << line[i];
		}
		cout << endl;
	}

}
