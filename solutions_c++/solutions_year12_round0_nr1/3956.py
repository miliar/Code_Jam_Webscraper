#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
	int k; 

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

	string str;
	cin >> k;
	getline(cin, str);
	for(int i = 1; i <= k; i++)
	{
		getline(cin, str);

		cout << "Case #" << i << ": ";

		for(int j = 0; j < str.size(); j++)
			cout << m[str[j]];
		cout << endl;
	}
}