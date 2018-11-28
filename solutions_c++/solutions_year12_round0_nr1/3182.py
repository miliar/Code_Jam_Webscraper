#include <fstream>
#include <map>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	ifstream file("problem_a.txt");
	map<char,char> mapping;

	mapping[' '] = ' ';
	mapping['a'] = 'y';
	mapping['y'] = 'a';
	mapping['o'] = 'k';
	mapping['e'] = 'o';
	mapping['z'] = 'q';
	mapping['j'] = 'u';
	mapping['p'] = 'r';
	mapping['m'] = 'l';
	mapping['s'] = 'n';
	mapping['l'] = 'g';
	mapping['c'] = 'e';
	mapping['k'] = 'i';
	mapping['d'] = 's';
	mapping['x'] = 'm';
	mapping['v'] = 'p';
	mapping['n'] = 'b';
	mapping['r'] = 't';
	mapping['b'] = 'h';
	mapping['w'] = 'f';
	mapping['f'] = 'c';
	mapping['g'] = 'v';
	mapping['h'] = 'x';
	mapping['i'] = 'd';
	mapping['q'] = 'z';
	mapping['t'] = 'w';
	mapping['u'] = 'j';

	if (file.is_open())
	{
		int T;
		file >> T;

		string line;
		getline (file, line);

		for (int i = 1; i <= T; i++)
		{
			getline (file, line);

			cout << "Case #" << i << ": ";
			for (size_t j = 0; j < line.size(); j++)
			{
				cout << mapping[line[j]];
			}
			cout << endl;
		}

		file.close();
	}
}
