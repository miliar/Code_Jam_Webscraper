#include <iostream>
#include <map>
#include <fstream>
#include <vector>
#include <sstream>

template <class T, class U>
T cast(const U& in) {
	std::stringstream ss;
	ss << in;
	T out;
	ss >> out;
	return out;
}

void read_cases(const std::string& from, std::vector<std::string>& to) {
	std::ifstream inp(from);
	std::string s;
	std::getline(inp, s);
	int cases = cast<int>(s);
	//
	for (int i = 0; i < cases; i++) {
		std::getline(inp, s);
		to.push_back(s);
	}
	//
	inp.close();
}

int main(int argc, char* argv[]) {
	char map[128];
	map['a'] = 'y';	//
	map['b'] = 'h'; //
	map['c'] = 'e'; //
	map['d'] = 's'; //
	map['e'] = 'o'; //
	map['f'] = 'c'; //
	map['g'] = 'v'; //
	map['h'] = 'x'; //
	map['i'] = 'd'; //
	map['j'] = 'u'; //
	map['k'] = 'i'; //
	map['l'] = 'g'; //
	map['m'] = 'l'; //
	map['n'] = 'b'; //
	map['o'] = 'k'; //
	map['p'] = 'r'; //
	map['q'] = 'z';
	map['r'] = 't'; //
	map['s'] = 'n'; //
	map['t'] = 'w'; //
	map['u'] = 'j'; //
	map['v'] = 'p'; //
	map['w'] = 'f'; //
	map['x'] = 'm'; //
	map['y'] = 'a'; //
	map['z'] = 'q';
	map[' '] = ' ';

	std::vector<std::string> a;
	read_cases(argv[1], a);

	std::ofstream out("problema.out");
	for (int i = 0; i < a.size(); i++) {
		out << "Case #" << (i+1) << ": ";
		//
		auto str = a[i];
		for (int c = 0; c < str.length(); c++) {
			out << map[str[c]];
		}
		out << "\n";
	}
	out.close();

	return 0;
}