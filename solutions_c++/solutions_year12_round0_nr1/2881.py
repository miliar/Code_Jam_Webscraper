#include <iostream.h>
#include <stdio.h>

const int N = 300;

int map[N];
char s[120];

void l_try()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	int cs;
	scanf("%d%*c", &cs);
	int x = 0;
	while (cs--)
	{
		gets(s);
		int i, j;
		printf("Case #%d: ", ++x);
		for (i=0; s[i]; i++) printf("%c", map[s[i]]);
		printf("\n");
	}
}


int main()
{
	map['a'] = 'y';
	map['b'] = 'h';
	map['c'] = 'e';
	map['d'] = 's';
	map['e'] = 'o';
	map['f'] = 'c';
	map['g'] = 'v';
	map['h'] = 'x';
	map['i'] = 'd';
	map['j'] = 'u';
	map['k'] = 'i';
	map['l'] = 'g';
	map['m'] = 'l';
	map['n'] = 'b';
	map['o'] = 'k';
	map['p'] = 'r';
	map['q'] = 'z';
	map['r'] = 't';
	map['s'] = 'n';
	map['t'] = 'w';
	map['u'] = 'j';
	map['v'] = 'p';
	map['w'] = 'f';
	map['x'] = 'm';
	map['y'] = 'a';
	map['z'] = 'q';
	map[' '] = ' ';
	
	l_try();
	return 0;
}

