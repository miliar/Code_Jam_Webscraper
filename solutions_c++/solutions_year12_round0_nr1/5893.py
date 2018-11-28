//============================================================================
// Name        : CodeJam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;

char translate(char ch) {
	switch (ch) {

	case ' ':
		return ' ';
		break;

	case 'a':
		return 'y';
		break;
	case 'b':
		return 'h';
		break;
	case 'c':
		return 'e';
		break;
	case 'd':
		return 's';
		break;
	case 'e':
		return 'o';
		break;
	case 'f':
		return 'c';
		break;
	case 'g':
		return 'v';
		break;
	case 'h':
		return 'x';
		break;
	case 'i':
		return 'd';
		break;
	case 'j':
		return 'u';
		break;
	case 'k':
		return 'i';
		break;
	case 'l':
		return 'g';
		break;
	case 'm':
		return 'l';
		break;
	case 'n':
		return 'b';
		break;
	case 'o':
		return 'k';
		break;
	case 'p':
		return 'r';
		break;
	case 'q':
		return 'z';
		break;
	case 'r':
		return 't';
		break;
	case 's':
		return 'n';
		break;
	case 't':
		return 'w';
		break;
	case 'u':
		return 'j';
		break;
	case 'v':
		return 'p';
		break;
	case 'w':
		return 'f';
		break;
	case 'x':
		return 'm';
		break;
	case 'y':
		return 'a';
		break;
	case 'z':
		return 'q';
		break;

	}
}

int main() {
	string str[30];
	string mystr;
	int i, j, T;
	cin >> T;

	getline (cin, mystr);	
	for (i = 0; i < T; i++) {

		getline (cin, str[i]);

	}

	for (i = 0; i < T; i++) {
			cout << "Case #" << i + 1 << ": ";
		for (j = 0; str[i][j] != '\0'; j++) {
			cout<<translate(str[i][j]);

		}
		cout << endl;

	}

	return 0;

}
