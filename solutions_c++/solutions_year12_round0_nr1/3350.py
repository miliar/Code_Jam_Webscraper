#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

void translate(string input) {
	string alphabet = "ayhesocvxduiglbkrztnwjpfmaq";

	for(int i = 0;i<input.length();i++) {
		char c = input[i];
		if(c != ' ')  c = alphabet[c-96];
		cout << c;
	}

	cout << endl;
}

int main() {
	fstream file;
	file.open("A-small-attempt0.in", fstream::in);

	char input[101];

	file.getline(input, 3);
	int T = atoi(input);

	for(int i=1;i<=T;i++) {
		file.getline(input, 101);
		cout << "Case #" << i << ": ";
		translate(input);
	}
}
