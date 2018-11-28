#include<iostream>
#include<cstring>
using namespace std;

#define ll long long
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	char m[256]={0};
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
	int tt, ii, i, l;
	char str[200];
	scanf("%d\n", &tt);;

	for(ii = 1; ii<=tt; ii++)
	{
		gets(str);
		l = strlen(str);
		for(i = 0; i<l; i++)
			str[i] = m[str[i]];
		printf("Case #%d: ", ii);
		puts(str);
	}
	return 0;
}