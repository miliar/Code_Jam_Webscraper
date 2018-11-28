#include <iostream>
#include <string>
#include <map>

using namespace std;

map<char, char> gog_en;

void init();

int main()
{
	init();

	freopen("A-small-attempt4.in", "r", stdin);
	freopen("A-small-attempt4.out", "w", stdout);

	int T;
	cin >> T;
	string blabla;

	getline(cin, blabla);

	for (int i = 1; i <= T; i++)
	{
		string str;
		getline(cin, str, '\n');
		cout << "Case #" << i << ": ";
		for (int j = 0; j < str.size(); j++)
		{
			cout << gog_en[str[j]];
		}
		cout << endl;
	}
	return 0;
}

void init()
{
	gog_en['a'] = 'y';
	gog_en['b'] = 'h';
	gog_en['c'] = 'e';
	gog_en['d'] = 's';
	gog_en['e'] = 'o';
	gog_en['f'] = 'c';
	gog_en['g'] = 'v';
	gog_en['h'] = 'x';
	gog_en['i'] = 'd';
	gog_en['j'] = 'u';
	gog_en['k'] = 'i';
	gog_en['l'] = 'g';
	gog_en['m'] = 'l';
	gog_en['n'] = 'b';
	gog_en['o'] = 'k';
	gog_en['p'] = 'r';
	gog_en['q'] = 'z'; // quick!!
	gog_en['r'] = 't';
	gog_en['s'] = 'n';
	gog_en['t'] = 'w';
	gog_en['u'] = 'j';
	gog_en['v'] = 'p';
	gog_en['w'] = 'f';
	gog_en['x'] = 'm';
	gog_en['y'] = 'a';
	gog_en['z'] = 'q'; // quick!!
	gog_en[' '] = ' ';
}
