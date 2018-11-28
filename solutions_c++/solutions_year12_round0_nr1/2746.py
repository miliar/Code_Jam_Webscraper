#include <stdio.h>

int main(int argc, char *argv[])
{
	char map[26];

	map['e' - 'a'] = 'o';
	map['j' - 'a'] = 'u';
	map['p' - 'a'] = 'r';
	map['m' - 'a'] = 'l';
	map['y' - 'a'] = 'a';
	map['s' - 'a'] = 'n';
	map['l' - 'a'] = 'g';
	map['c' - 'a'] = 'e';
	map['k' - 'a'] = 'i';
	map['d' - 'a'] = 's';
	map['x' - 'a'] = 'm';
	map['v' - 'a'] = 'p';
	map['n' - 'a'] = 'b';
	map['r' - 'a'] = 't';
	map['i' - 'a'] = 'd';
	map['b' - 'a'] = 'h';
	map['t' - 'a'] = 'w';
	map['a' - 'a'] = 'y';
	map['h' - 'a'] = 'x';
	map['w' - 'a'] = 'f';
	map['f' - 'a'] = 'c';
	map['o' - 'a'] = 'k';
	map['u' - 'a'] = 'j';
	map['g' - 'a'] = 'v';
	map['z' - 'a'] = 'q';
	map['q' - 'a'] = 'z';

	freopen ("A-small-attempt0.in", "r", stdin);
	freopen ("A-small.out", "w", stdout);

	int T;
	scanf ("%d\n", &T);
	for (int i = 1; i <= T; ++i)
	{
		char line[10000];
		gets (line);
		printf ("Case #%d: ", i);
		for (int j = 0; line[j] != '\0'; ++j)
		{
			if ('a' <= line[j] && line[j] <= 'z')
			{
				putchar (map[line[j] - 'a']);
			} else
				putchar (line[j]);
		}
		putchar ('\n');
	}
	
	
	return 0;
}
