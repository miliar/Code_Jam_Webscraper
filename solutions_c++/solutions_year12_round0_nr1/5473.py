#include <cstdio>

char map[300];
char line[200];

int main()
{
	map['a'] = 'y'; //
	map['b'] = 'h'; //
	map['c'] = 'e'; //
	map['d'] = 's'; //
	map['e'] = 'o'; //
	map['f'] = 'c'; //
	map['g'] = 'v'; //
	map['h'] = 'x'; //
	map['i'] = 'd'; //
	map['j'] = 'u'; //
	map['k'] = 'i'; //
	map['l'] = 'g'; //
	map['m'] = 'l'; //
	map['n'] = 'b'; //
	map['o'] = 'k'; //
	map['p'] = 'r'; //
	map['q'] = 'z';
	map['r'] = 't'; //
	map['s'] = 'n'; //
	map['t'] = 'w'; //
	map['u'] = 'j'; //
	map['v'] = 'p'; //
	map['w'] = 'f'; //
	map['x'] = 'm'; //
	map['y'] = 'a'; //
	map['z'] = 'q'; //

	map[' '] = ' ';

	int T;

	scanf(" %d", &T);


	for(int _42 = 1; _42 <= T; ++_42) {

		scanf(" %[^\n]\n", line);

		printf("Case #%d: ", _42);
		char *p = line;
		while(*p) {
			printf("%c", map[*p]);
			p++;
		}
		printf("\n");
	}
}
