#include <iostream>
#include <string>
#include "stdio.h"
using namespace std;


char translate(char in) {
	switch (in) {
		case 'a':
			return 'y';
		case 'b':
			return 'h';
		case 'c':
			return 'e';
		case 'd':
			return 's';
		case 'e':
			return 'o';
		case 'f':
			return 'c';
		case 'g':
			return 'v';
		case 'h':
			return 'x';
		case 'i':
			return 'd';
		case 'j':
			return 'u';
		case 'k':
			return 'i';
		case 'l':
			return 'g';
		case 'm':
			return 'l';
		case 'n':
			return 'b';
		case 'o':
			return 'k';
		case 'p':
			return 'r';
		case 'q':
			return 'z';
		case 'r':
			return 't';
		case 's':
			return 'n';
		case 't':
			return 'w';
		case 'u':
			return 'j';
		case 'v':
			return 'p';
		case 'w':
			return 'f';
		case 'x':
			return 'm';
		case 'y':
			return 'a';
		case 'z':
			return 'q';
		}
	}



void decode() {
	char c;
	while (scanf("%c", &c) > 0) {
		if (c == ' ')
			cout << " ";
		else if (c == '\n')
			break;
		else
			cout << translate(c);
	}
}

int main() {
	int cases;
	cin >> cases;
	char newline;
	scanf ("%c", &newline); // skip ws

	int i;
	for (i = 1; i <= cases; i++) {
		cout << "Case #" << i << ": ";
		decode();
		cout << endl;
	}
	return 0;
}


