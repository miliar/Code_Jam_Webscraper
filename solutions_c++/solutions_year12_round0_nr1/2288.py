#include <iostream>
#include <map>

using namespace std;

typedef map<char, char> Dictionary;

int main()
{
	Dictionary dict;
	dict['a'] = 'y';
	dict['b'] = 'h';
	dict['c'] = 'e';
	dict['d'] = 's';
	dict['e'] = 'o';
	dict['f'] = 'c';
	dict['g'] = 'v';
	dict['h'] = 'x';
	dict['i'] = 'd';
	dict['j'] = 'u';
	dict['k'] = 'i';
	dict['l'] = 'g';
	dict['m'] = 'l';
	dict['n'] = 'b';
	dict['o'] = 'k';
	dict['p'] = 'r';
	dict['q'] = 'z'; //
	dict['r'] = 't';
	dict['s'] = 'n';
	dict['t'] = 'w';
	dict['u'] = 'j';
	dict['v'] = 'p';
	dict['w'] = 'f';
	dict['x'] = 'm';
	dict['y'] = 'a';
	dict['z'] = 'q'; //
	dict[' '] = ' ';

	const int MAX_G = 105;
	int tt = 0;
	
	cin >> tt;
	char c[2]; cin.getline(c, 2);
	for (int t = 1; t <= tt; ++t)
	{
		char input[MAX_G] = {0}, output[MAX_G] = {0};
		cin.getline(input, MAX_G);

		char *pi = input;
		char *po = output;
		while (*pi)
			*po++ = dict[*pi++];

		cout << "Case #" << t << ": " << output << endl;
	} 
	return 0;
}