#include <utility>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <map>
using namespace std;

map<char,char> m;

void init(){
	m[' '] = ' ';
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
}

int main(){
	int repeat, len;
	char line[110];
	scanf("%d", &repeat);
	getchar();
	init();
	for(int re = 1;re <= repeat;re++){
		gets(line);
		len = strlen(line);
		printf("Case #%d: ", re);
		for(int i = 0;i < len;i++){
			putchar(m[line[i]]);
		}
		printf("\n");
	}
	return 0;
}


