#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int main()
{
	map<char,char> m;
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
	int t;
	scanf("%d",&t);
	char c;
	c = getchar();
	for (int i=1; i<=t; i++) {
		cout << "Case #"<< i <<": ";
		while ((c=getchar())!='\n') {
			cout << m[c];
		}
		cout << endl;
	}
	return 0;
}
