// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <map>

using namespace std;


int main()
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

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t;
	char line[1024];
	scanf("%d ", &t);

	for (int test = 1; test <= t; ++test) {
		fgets(line, 110, stdin);
		printf("Case #%d: ", test); 
		for (int i = 0; i < strlen(line); ++i) {
			if (isalpha(line[i])) {
				printf("%c", m[line[i]]);
			} else {
				printf("%c", line[i]);
			}
		}
	}



	return 0;
}

