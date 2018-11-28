#include <iostream>
#include <map>
#include <stdio.h>

using namespace std;

int main()
{
	map<char,char> charMap;
	charMap['a'] = 'y';
	charMap['b'] = 'h';
	charMap['c'] = 'e';
	charMap['d'] = 's';
	charMap['e'] = 'o';
	charMap['f'] = 'c';
	charMap['g'] = 'v';
	charMap['h'] = 'x';
	charMap['i'] = 'd';
	charMap['j'] = 'u';
	charMap['k'] = 'i';
	charMap['l'] = 'g';
	charMap['m'] = 'l';
	charMap['n'] = 'b';
	charMap['o'] = 'k';
	charMap['p'] = 'r';
	charMap['q'] = 'z';
	charMap['r'] = 't';
	charMap['s'] = 'n';
	charMap['t'] = 'w';
	charMap['u'] = 'j';
	charMap['v'] = 'p';
	charMap['w'] = 'f';
	charMap['x'] = 'm';
	charMap['y'] = 'a';
	charMap['z'] = 'q';

	int T;
	scanf("%d",&T);
	char str[100];
	gets(str);
	for (int t = 1; t <= T; t++)
	{
		gets(str);
		int len = strlen(str);

		for (int i = 0; i < len; i++)
		{
			if (str[i] == ' ') continue;
			str[i] = charMap[str[i]];
		}

		printf("Case #%d: %s\n",t,str);
	}



}