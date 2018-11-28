#include <iostream>
#include <string>

using namespace std;

int main ()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	char map[200];
	map['a'] = 'y';
	map['b'] = 'h';
	map['c'] = 'e';
	map['d'] = 's';
	map['e'] = 'o';
	map['f'] = 'c';
	map['g'] = 'v';
	map['j'] = 'u';
	map['i'] = 'd';
	map['h'] = 'x';
	map['k'] = 'i';
	map['l'] = 'g';
	map['m'] = 'l';
	map['n'] = 'b';
	map['o'] = 'k';
	map['p'] = 'r';
	map['q'] = 'z';
	map['r'] = 't';
	map['s'] = 'n';
	map['t'] = 'w';
	map['u'] = 'j';
	map['v'] = 'p';
	map['w'] = 'f';
	map['x'] = 'm';
	map['y'] = 'a';
	map['z'] = 'q';
	int t; 
	cin >> t;
	string s;
	char c;
	getline(cin, s);
	for (int o = 0; o < t; o++)
	{
		getline(cin, s);
		cout << "Case #" << o+1 << ": ";
		for (int i = 0; i < s.size(); i++)
			if (isalpha(s[i]))
				cout<<map[s[i]];
			else 
				cout<<s[i];
		cout << endl; 
	}
	return 0;
}