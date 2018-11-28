#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	map <char, char> mp;
	mp['a'] = 'y';
	mp['b'] = 'h';
	mp['c'] = 'e';
	mp['d'] = 's';
	mp['e'] = 'o';
	mp['f'] = 'c';
	mp['g'] = 'v';
	mp['h'] = 'x';
	mp['i'] = 'd';
	mp['j'] = 'u';
	mp['k'] = 'i';
	mp['l'] = 'g';
	mp['m'] = 'l';
	mp['n'] = 'b';
	mp['o'] = 'k';
	mp['p'] = 'r';
	mp['q'] = 'z';
	mp['r'] = 't';
	mp['s'] = 'n';
	mp['t'] = 'w';
	mp['u'] = 'j';
	mp['v'] = 'p';
	mp['w'] = 'f';
	mp['x'] = 'm';
	mp['y'] = 'a';
	mp['z'] = 'q';
	mp[' '] = ' ';

	int t;
	scanf("%d ", &t);
	for (int i = 0; i < t; i++)
	{
		char buf[105] = {0};
		gets(buf);
		for (int i = 0; buf[i]; i++)
			buf[i] = mp[buf[i]];
		printf("Case #%d: %s\n", i + 1, buf);
	}
	return 0;
}
