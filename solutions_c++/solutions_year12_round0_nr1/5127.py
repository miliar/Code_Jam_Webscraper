#include <memory>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <algorithm>

std::map<char, char> map;

void populateMap()
{
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
	map['x'] = 'm';
	map['w'] = 'f';
	map['y'] = 'a';
	map['z'] = 'q';
	map[' '] = ' ';
}

void solveCase(std::ifstream& in, std::ofstream& out)
{
	std::string line;
	std::getline(in, line);

	std::for_each(line.begin(), line.end(),[&out](char c){
		out << map[c];
	});
}

int main()
{
	populateMap();
	std::string baseDir = "problems/";
	std::string testFile = "A-small-attempt2";

	std::ifstream in(baseDir + testFile + ".in");
	std::ofstream out(baseDir + testFile + ".out");
	std::string t = baseDir + testFile + ".in";

	std::cout << "Starting solving cases..." << std::endl;

	int numberOfCases = 0;
	int currCase = 0;

	in >> numberOfCases;
	std::string line;
	std::getline(in, line);
	while(currCase++ < numberOfCases) {
		out << "Case #" << currCase << ": ";
		try {
			solveCase(in, out);
		} catch (std::exception& e) {
			std::cout << "Error on Case #" << currCase << " " << e.what() << std::endl;
		}
		out << std::endl;
		std::cout << "Cases solved (" << currCase << "/" << numberOfCases << ")" << std::endl;
	}

	std::cout << "All cases solved!";
	return 0;
}
