#include <stdio.h>

char map[128];

void init_map()
{
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
}

int main()
{
	int ccc;
	scanf("%d", &ccc);
	getchar();
	init_map();
	for (int cc = 1; cc <= ccc; ++cc)
	{
		static char buf[1024];
		fgets(buf, 1024, stdin);
		printf("Case #%d: ", cc);
		for (int i = 0; i < 1024; ++i)
		{
			if ((buf[i] < 'a' || buf[i] > 'z') && buf[i] != ' ')
				break;
			putchar(map[(int)buf[i]]);
		}
		putchar('\n');
	}
	return 0;
}