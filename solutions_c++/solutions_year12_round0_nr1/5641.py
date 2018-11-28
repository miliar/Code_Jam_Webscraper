#include <iostream>
#include <cstdio>

using namespace std;

const int MXN = 107;

char s[MXN];
char to[356];

int main()
{
	int T;
	scanf("%d\n", &T);
	to['a'] = 'y';
	to['b'] = 'h';
	to['c'] = 'e';
	to['d'] = 's';
	to['e'] = 'o';
	to['f'] = 'c';
	to['g'] = 'v';
	to['h'] = 'x';
	to['i'] = 'd';
	to['j'] = 'u';
	to['k'] = 'i';
	to['l'] = 'g';
	to['m'] = 'l';
	to['n'] = 'b';
	to['o'] = 'k';
	to['p'] = 'r';
	to['q'] = 'z';
	to['r'] = 't';
	to['s'] = 'n';
	to['t'] = 'w';
	to['u'] = 'j';
	to['v'] = 'p';
	to['w'] = 'f';
	to['x'] = 'm';
	to['y'] = 'a';
	to['z'] = 'q';
	to[' '] = ' ';
	int numCase = 0;
	while (T--) {
		gets(s);
		for (int i = 0; s[i]; ++i) {
			s[i] = to[(int) s[i]];
		}
		printf("Case #%d: %s\n", ++numCase, s);
	}
}
