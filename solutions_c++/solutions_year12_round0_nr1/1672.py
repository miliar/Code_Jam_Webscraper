#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	int a[256];
	a['y'] = 'a';
	a['n'] = 'b';
	a['f'] = 'c';
	a['i'] = 'd';
	a['c'] = 'e';
	a['w'] = 'f';
	a['l'] = 'g';
	a['b'] = 'h';
	a['k'] = 'i';
	a['u'] = 'j';
	a['o'] = 'k';
	a['m'] = 'l';
	a['x'] = 'm';
	a['s'] = 'n';
	a['e'] = 'o';
	a['v'] = 'p';
	a['z'] = 'q';
	a['p'] = 'r';
	a['d'] = 's';
	a['r'] = 't';
	a['j'] = 'u';
	a['g'] = 'v';
	a['t'] = 'w';
	a['h'] = 'x';
	a['a'] = 'y';
	a['q'] = 'z';
	a[' '] = ' ';
	fgetc(stdin);
	for(int i = 1; i <= t; i++) {
		char ch;
		printf("Case #%d: ", i);
		while((ch=fgetc(stdin))!='\n' && ch!='\r' && ch!=EOF) {
			fputc(a[ch], stdout);
		}
		fputc('\n', stdout);
	}
	return 0;
}
