#include <algorithm>
#include <stdio.h>
#include <map>

using namespace std;

int testCases;
char strCit[128];
map <char, char> t;

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	t['y'] = 'a';
	t['n'] = 'b';
	t['f'] = 'c';
	t['i'] = 'd';
	t['c'] = 'e';
	t['w'] = 'f';
	t['l'] = 'g';
	t['b'] = 'h';
	t['k'] = 'i';
	t['u'] = 'j';
	t['o'] = 'k';
	t['m'] = 'l';
	t['x'] = 'm';
	t['s'] = 'n';
	t['e'] = 'o';
	t['v'] = 'p';
	t['z'] = 'q';
	t['p'] = 'r';
	t['d'] = 's';
	t['r'] = 't';
	t['j'] = 'u';
	t['g'] = 'v';
	t['t'] = 'w';
	t['h'] = 'x';
	t['a'] = 'y';
	t['q'] = 'z';
	t[' '] = ' ';

	int i = 1;
	for (scanf("%d\n", &testCases); i <= testCases; i++)
	{
		fgets(strCit, 128, stdin);

		printf("Case #%d: ", i);

		for (int j = 0; strCit[j] != '\n'; j++)
		{
			printf("%c", t[strCit[j]]);
		}

		printf("\n");
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
