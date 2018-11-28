#include <stdio.h>

char a[105];
int i, j, T;
char b[200], c[200];

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	
	freopen("A-small-attempt1.out", "w", stdout);

	b['a'] = 'y';
	b['b'] = 'h';
	b['c'] = 'e';
	b['d'] = 's';
	b['e'] = 'o';
	b['f'] = 'c';
	b['g'] = 'v';
	b['h'] = 'x';
	b['i'] = 'd';
	b['j'] = 'u';
	b['k'] = 'i';
	b['l'] = 'g';
	b['m'] = 'l';
	b['n'] = 'b';
	b['o'] = 'k';
	b['p'] = 'r';
	b['q'] = 'z';
	b['r'] = 't';
	b['s'] = 'n';
	b['t'] = 'w';
	b['u'] = 'j';
	b['v'] = 'p';
	b['w'] = 'f';
	b['x'] = 'm';
	b['y'] = 'a';
	b['z'] = 'q';
	b[' '] = ' ';

	scanf("%d", &T);
	gets(a);
	for(j = 1; j <= T; j++)
	{
		gets(a);
		printf("Case #%d: ", j);
		for(i = 0; a[i]; i++)
			putchar(b[a[i]]);
		printf("\n");
	}
	
	return 0;
}