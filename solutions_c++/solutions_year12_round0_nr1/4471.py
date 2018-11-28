#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define MAXN 10000
#define MAXC 256

char p[MAXC];
char s[MAXN];

inline void init()
{
	p['a'] = 'y';
	p['b'] = 'h';
	p['c'] = 'e';
	p['d'] = 's';
	p['e'] = 'o';
	p['f'] = 'c';
	p['g'] = 'v';
	p['h'] = 'x';
	p['i'] = 'd';
	p['j'] = 'u';
	p['k'] = 'i';
	p['l'] = 'g';
	p['m'] = 'l';
	p['n'] = 'b';
	p['o'] = 'k';
	p['p'] = 'r';
	p['q'] = 'z';
	p['r'] = 't';
	p['s'] = 'n';
	p['t'] = 'w';
	p['u'] = 'j';
	p['v'] = 'p';
	p['w'] = 'f';
	p['x'] = 'm';
	p['y'] = 'a';
	p['z'] = 'q';
	p[' '] = ' ';
}

int main()
{
	init();
	int tt;
	scanf("%d\n", &tt);
	for (int t = 0; t < tt; ++t)
	{
		gets(s);
		int n = strlen(s);
		for (int i = 0; i < n; ++i)
			s[i] = p[s[i]];
		printf("Case #%d: %s\n", t + 1, s);
	}
	return 0;
}
