#include <stdio.h>
#include <map>
#include <string.h>

using namespace std;

int main ()
{
	map<char, char> m;
	
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
	m[' '] = ' ';
	
	
	int T, x, len, i;
	char input[50], c;
	
	scanf("%d", &T);
	fgetc(stdin);
	
	for(x=1; x<=T; x++)
	{
		gets(input);
		len = strlen(input);
		printf("Case #%d: ", x);
		for (i=0; i<len; i++)
			printf("%c", m[input[i]]);
		printf("\n");
	}
	
	return 0;
}
