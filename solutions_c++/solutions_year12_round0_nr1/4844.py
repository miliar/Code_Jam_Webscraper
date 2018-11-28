
#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	
	char map[256];

	map[' '] = ' ';
	map['a'] = 'y';
	map['b'] = 'h';
	map['c'] = 'e';
	map['d'] = 's';
	map['e'] = 'o';
	map['f'] = 'c';
	map['g'] = 'v';
	map['h'] = 'x';
	map['i'] = 'd';
	map['j'] = 'u';
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
	//map[' '] = ' ';

	string s;
	

	int n;
	cin >> n;

	getline(cin, s);
	for (int i = 0; i < n; i++){
		getline(cin, s);

		for (int j = 0; j < s.length(); j++){
			s[j] = map[s[j]];
		}

		cout << "Case #" << (i+1) << ": " << s << endl;
	}
	



	return 0;
}

