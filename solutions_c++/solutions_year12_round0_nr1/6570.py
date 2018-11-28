#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

static map<char, char> trmap;

void init_map();

int main(int argc, char **argv)
{
	init_map();

	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	string buff("");
	string line("");
	getline(fin, buff);

	int n = atoi(buff.c_str());
	for (int i = 0; i < n; i++)
	{
		getline(fin, buff);
		
		for (int j = 0; j < buff.length(); j++)
		{
			if (buff[j] != ' ')
				line += trmap[buff[j]];
			else
				line += ' ';
		}	
		
		fout << "Case #" << (i+1) << ": " << line << endl;
		line = "";
	}

	fin.close();
	fout.close();
	return EXIT_SUCCESS;
}

void init_map()
{
	trmap['a'] = 'y';
	trmap['b'] = 'h';
	trmap['c'] = 'e';
	trmap['d'] = 's';
	trmap['e'] = 'o';
	trmap['f'] = 'c';
	trmap['g'] = 'v';
	trmap['h'] = 'x';
	trmap['i'] = 'd';
	trmap['j'] = 'u';
	trmap['k'] = 'i';
	trmap['l'] = 'g';
	trmap['m'] = 'l';
	trmap['n'] = 'b';
	trmap['o'] = 'k';
	trmap['p'] = 'r';
	trmap['q'] = 'z';
	trmap['r'] = 't';
	trmap['s'] = 'n';
	trmap['t'] = 'w';
	trmap['v'] = 'p';
	trmap['u'] = 'j';
	trmap['w'] = 'f';
	trmap['x'] = 'm';
	trmap['y'] = 'a';
	trmap['z'] = 'q';
	trmap[' '] = ' ';
}
