#include <string.h>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
	freopen ("A-small-attempt2.in", "r", stdin);
	ofstream cout("A-small-attempt2.out");

	int X;
	char c;
	cin >> X;

	for (int i=0; i<X+1; i++) {
		if (i>0) cout << "Case #" << i << ": ";
		while (c = getchar()) {
			if (c == '\n') { if (i>0) cout << endl; break;}

			switch (c) {
					case ' ': c = ' '; break;
					case 'a': c = 'y'; break;
					case 'b': c = 'h'; break;
					case 'c': c = 'e'; break;
					case 'd': c = 's'; break;
					case 'e': c = 'o'; break;
					case 'f': c = 'c'; break;
					case 'g': c = 'v'; break;
					case 'h': c = 'x'; break;
					case 'i': c = 'd'; break;
					case 'j': c = 'u'; break;
					case 'k': c = 'i'; break;
					case 'l': c = 'g'; break;
					case 'm': c = 'l'; break;
					case 'n': c = 'b'; break;
					case 'o': c = 'k'; break;
					case 'p': c = 'r'; break;
					case 'q': c = 'z'; break;
					case 'r': c = 't'; break;
					case 's': c = 'n'; break;
					case 't': c = 'w'; break;
					case 'u': c = 'j'; break;
					case 'v': c = 'p'; break;
					case 'w': c = 'f'; break;
					case 'x': c = 'm'; break;
					case 'y': c = 'a'; break;
					case 'z': c = 'q'; break;

				}
				cout << c;
			}
		}
	return 0;
}

