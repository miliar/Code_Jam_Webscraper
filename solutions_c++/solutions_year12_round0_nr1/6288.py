#include <iostream>
#include <map>
using namespace std;

int main()
{
	map<char,char> d;
	d['a'] = 'y';
	d['b'] = 'h';
	d['c'] = 'e';
	d['d'] = 's';
	d['e'] = 'o';
	d['f'] = 'c';
	d['g'] = 'v';
	d['h'] = 'x';
	d['i'] = 'd';
	d['j'] = 'u';
	d['k'] = 'i';
	d['l'] = 'g';
	d['m'] = 'l';
	d['n'] = 'b';
	d['o'] = 'k';
	d['p'] = 'r';
	d['q'] = 'z';
	d['r'] = 't';
	d['s'] = 'n';
	d['t'] = 'w';
	d['u'] = 'j';
	d['v'] = 'p';
	d['w'] = 'f';
	d['x'] = 'm';
	d['y'] = 'a';
	d['z'] = 'q';
	d[' '] = ' ';

	int N;
	int c=1;
	cin >> N;
	cin.ignore();
	while (N--)
	{
		char s[201];
		cin.getline(s, 200);

		for (int i=0; s[i]!='\0'; i++)
			s[i] = d[s[i]];

		cout << "Case #" << c++ << ": " << s << endl;
	}
}
