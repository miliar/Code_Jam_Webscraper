#include <map>
#include <string>
#include <iostream>

using namespace std;
int main()
{
	map<char, char> cmap;
	cmap['e'] = 'o';
	cmap['j'] = 'u';
	cmap['p'] = 'r';
	cmap['m'] = 'l';
	cmap['y'] = 'a';
	cmap['s'] = 'n';
	cmap['l'] = 'g';
	cmap['c'] = 'e';
	
	cmap['k'] = 'i';
	cmap['d'] = 's';
	cmap['x'] = 'm';
	cmap['v'] = 'p';
	cmap['n'] = 'b';
	cmap['r'] = 't';
	cmap['i'] = 'd';
	cmap['g'] = 'v';
	
	cmap['h'] = 'x';
	cmap['a'] = 'y';
	cmap['b'] = 'h';
	cmap['f'] = 'c';
	cmap['o'] = 'k';
	cmap['t'] = 'w';
	cmap['u'] = 'j';
	cmap['w'] = 'f';
	cmap['z'] = 'q';
	cmap['q'] = 'z';
	cmap[' '] = ' ';

	int n;
	string temp;
	cin >> n;
	getline(cin, temp);
	for (int i = 0; i < n; ++i)
	{
		string line;
		getline(cin, line);
		
		for (string::size_type j = 0; j < line.size(); ++j)
			line[j] = cmap[line[j]];
		
		cout << "Case #" << i + 1 << ": " << line << '\n';
	}
}
