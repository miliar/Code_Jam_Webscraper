#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <cctype>

using namespace std;

int main()
{
	freopen("tongue.out", "w", stdout);
	freopen("tongue.in", "r", stdin);
	
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
	for (int i = 65; i <= 90; i++) 
		m[((char) i)] = toupper(m[((char) (i+22))]);

	int N;
	string line, trans = "";
	
	cin >> N;
	getline(cin, line);
	for (int i = 1; i <= N; i++) {
		getline(cin, line);
		cout << "Case #" << i << ": ";
		for (int j = 0; j < line.size(); j++)
			trans += m[line[j]];
		cout << trans << endl;
		trans = "";
	}
}
