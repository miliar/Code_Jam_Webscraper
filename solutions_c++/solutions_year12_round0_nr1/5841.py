#include <stdio.h>
#include <string.h>
#include <iostream>
#include <map>

using namespace std;

int main () {

	int t, i, n;
	char str[101];
	map<char, char> h;

	h['a'] = 'y';
	h['b'] = 'h';
	h['c'] = 'e';
	h['d'] = 's';
	h['e'] = 'o';
	h['f'] = 'c';
	h['g'] = 'v';
	h['h'] = 'x';
	h['i'] = 'd';
	h['j'] = 'u';
	h['k'] = 'i';
	h['l'] = 'g';
	h['m'] = 'l';
	h['n'] = 'b';
	h['o'] = 'k';
	h['p'] = 'r';
	h['q'] = 'z';
	h['r'] = 't';
	h['s'] = 'n';
	h['t'] = 'w';
	h['u'] = 'j';
	h['v'] = 'p';
	h['w'] = 'f';
	h['x'] = 'm';
	h['y'] = 'a';
	h['z'] = 'q';

	cin >> t;
	n = 1;
	getchar();
	while (t-- > 0) {
		gets(str);
		cout << "Case #" << n++ << ": ";
		for (i = 0; i < strlen(str); i++) {
			if (str[i] == ' ')
				cout << str[i];
			else
				cout << h[str[i]];
		}
		cout << endl;
	}

	return 0;
}
