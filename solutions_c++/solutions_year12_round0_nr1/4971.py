#include <iostream>
#include <string>
#include <map>
#include <cassert>

int main() {

	std::map<char, char> m;
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';

	int N; std::cin >> N >> std::ws;

	for (int i = 0; i < N; ++i) {
		std::string s;
		std::getline(std::cin, s);
		for (std::string::iterator it = s.begin(); it != s.end(); ++it) {
			if (*it != ' ') {
				*it = m[*it];
				assert(*it != 0);
			}
		}
		std::cout << "Case #" << (i+1) << ": " << s << std::endl;
	}

	return 0;
}
