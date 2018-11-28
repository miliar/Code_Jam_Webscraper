#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;

char temp[1010];

map<char, char> ma;

int main(void)
{
	ma.clear();
	ma['a'] = 'y';
	ma['b'] = 'h';
	ma['c'] = 'e';
	ma['d'] = 's';
	ma['e'] = 'o';
	ma['f'] = 'c';
	ma['g'] = 'v';
	ma['h'] = 'x';
	ma['i'] = 'd';
	ma['j'] = 'u';
	ma['k'] = 'i';
	ma['l'] = 'g';
	ma['m'] = 'l';
	ma['n'] = 'b';
	ma['o'] = 'k';
	ma['p'] = 'r';
	ma['q'] = 'z';//;
	ma['r'] = 't';
	ma['s'] = 'n';
	ma['t'] = 'w';
	ma['u'] = 'j';
	ma['v'] = 'p';
	ma['w'] = 'f';
	ma['x'] = 'm';
	ma['y'] = 'a';
	ma['z'] = 'q';//
	int t;
	freopen("D:/test12.in", "r", stdin);
	freopen("D:/test12.out", "w", stdout);
	while(scanf("%d", &t) != EOF)
	{
		getchar();
		int ca = 0;
		while(t--)
		{
			gets(temp);
			printf("Case #%d: ", ++ca);
			for(int i = 0; i < strlen(temp); ++i)
			{
				if(temp[i] == '\n')
					continue;
				if(temp[i] == ' ')
					printf(" ");
				else
					printf("%c", ma[temp[i]]);
			}
			puts("");
		}
	}
	return 0;
}