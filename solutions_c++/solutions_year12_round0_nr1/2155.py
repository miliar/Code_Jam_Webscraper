#include <iostream>
#include <string>
#include <stdio.h>
#include <map>

using namespace std;

void init()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
}

int main()
{
	init();
	map <char, char> voc;
	voc['a'] = 'y';
	voc['b'] = 'h';
	voc['c'] = 'e';
	voc['d'] = 's';
	voc['e'] = 'o';
	voc['f'] = 'c';
	voc['g'] = 'v';
	voc['h'] = 'x';
	voc['i'] = 'd';
	voc['j'] = 'u';
	voc['k'] = 'i';
	voc['l'] = 'g';
	voc['m'] = 'l';
	voc['n'] = 'b';
	voc['o'] = 'k';
	voc['p'] = 'r';
	voc['q'] = 'z';
	voc['r'] = 't';
	voc['s'] = 'n';
	voc['t'] = 'w';
	voc['u'] = 'j';
	voc['v'] = 'p';
	voc['w'] = 'f';
	voc['x'] = 'm';
	voc['y'] = 'a';
	voc['z'] = 'q';
	int T;
	cin >> T;
	string str;
	getline(cin, str);
	for (int i = 0; i < T; ++i)
	{
		getline(cin, str);
		for (int j = 0; j < (int) str.length(); ++j)
		{
			if (str[j] != ' ')
			{
				str[j] = voc[str[j]];
			}
		}
		cout << "Case #" << i + 1 << ": " << str << endl;
	}
	return 0;
}
