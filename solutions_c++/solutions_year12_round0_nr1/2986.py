#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	std::ifstream file("A-small-attempt0.in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	map<char,char> t;
	t['a'] = 'y';
	t['b'] = 'h';
	t['c'] = 'e';
	t['d'] = 's';
	t['e'] = 'o';
	t['f'] = 'c';
	t['g'] = 'v';
	t['h'] = 'x';
	t['i'] = 'd';
	t['j'] = 'u';
	t['k'] = 'i';
	t['l'] = 'g';
	t['m'] = 'l';
	t['n'] = 'b';
	t['o'] = 'k';
	t['p'] = 'r';
	t['q'] = 'z';
	t['r'] = 't';
	t['s'] = 'n';
	t['t'] = 'w';
	t['u'] = 'j';
	t['v'] = 'p';
	t['w'] = 'f';
	t['x'] = 'm';
	t['y'] = 'a';
	t['z'] = 'q';
	t[' '] = ' ';

	string nb_t;
	int nb;

	getline(file,nb_t);
	nb = atoi(nb_t.c_str());

	for(int i = 0; i < nb; ++i)
	{
		getline(file,nb_t);

		file2 << "Case #" << i+1 << ": " ;
		for(string::iterator it = nb_t.begin(); it != nb_t.end(); ++it)
		{
			file2 << t[*it];
		}
		file2 << endl;
	}
}