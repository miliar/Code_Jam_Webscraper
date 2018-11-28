#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <string>

static std::map<char, char> map;

void translate(const std::string& line, int nbUC)
{
	std::stringstream ss;
	ss << "Case #" << nbUC << ": ";

	for (std::string::const_iterator it = line.begin(); it != line.end(); ++it)
	{
		ss << map[*it];
	}

	std::cout << ss.str() << std::endl;
}

int main(int argc, char **argv)
{
	map[' '] = ' ';
	map['a'] = 'y';
	map['c'] = 'e';
	map['b'] = 'h';
	map['e'] = 'o';
	map['d'] = 's';
	map['g'] = 'v';
	map['f'] = 'c';
	map['i'] = 'd';
	map['h'] = 'x';
	map['k'] = 'i';
	map['j'] = 'u';
	map['m'] = 'l';
	map['l'] = 'g';
	map['o'] = 'k';
	map['n'] = 'b';
	map['p'] = 'r';
	map['s'] = 'n';
	map['r'] = 't';
	map['u'] = 'j';
	map['t'] = 'w';
	map['w'] = 'f';
	map['v'] = 'p';
	map['y'] = 'a';
	map['x'] = 'm';
	map['z'] = 'q';
	map['q'] = 'z';

	std::ifstream in(argv[1], std::ifstream::in);

	std::string line;
	std::getline(in, line);

	int nbUC = atoi(line.c_str());
	int curUC = 1;

	while (curUC <= nbUC)
	{
		std::getline(in, line);
		translate(line, curUC);
		curUC++;
	}

	return 0;
}
