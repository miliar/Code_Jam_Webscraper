#include <cstdio>
using namespace std;

int main()
{
	int map[128];
	int ans, i, n, c;
	map[' '] = ' ';
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
	scanf("%d", &n);
	while(getchar() != '\n');
	for (i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		while ((c = getchar()) != '\n')
			putchar(map[c]);
		putchar('\n');
	}
	return 0;
}