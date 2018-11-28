#include <fstream>
#include <iostream>
#include <map>
#include <string>
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
	m[' '] = ' ';

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int N;
	cin >> N;
	cin.get();
	for (int tc = 0; tc < N; tc++)
	{
		string s;
		getline(cin, s);

		cout << "Case #" << tc + 1 << ": ";
		for (int i = 0; i < s.size(); i++)
		{
			cout << m[s[i]];
		}
		cout << endl;
	}
	return 0;
}