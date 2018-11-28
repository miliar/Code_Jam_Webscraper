/* Hezekiah's Google Code Jam Solution
 * Usage: codejam < file.in > file.out
 */

#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>

std::map<char, char> map;

void initialize() {
	//                 a    b    c    d    e    f    g    h    i    j    k    l    m    n    o    p    q    r    s    t    u    v    w    x    y    z
	char letters[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	for(unsigned letter = 0u; letter < 26u; ++letter) {
		map['a' + letter] = letters[letter];
	}
	map[' '] = ' ';
}

std::string solve(const std::vector<std::string>& input) {
	std::string text = input[0u];
	for(std::string::iterator character = text.begin(); character != text.end(); ++character) {
		*character = map[*character];
	}
	return text + '\n';
}

unsigned moreLines(const std::string& line) {
	return 0u;
}

int main() {
	initialize();

	std::string line;
	std::getline(std::cin, line);
	unsigned cases;
	std::istringstream(line) >> cases;

	std::getline(std::cin, line);
	for(unsigned caseNumber = 1u; caseNumber <= cases; ++caseNumber) {

		unsigned lines = 1u + moreLines(line);
		std::vector<std::string> input(lines);
		for(std::vector<std::string>::iterator inputLine = input.begin(); inputLine != input.end(); ++inputLine) {
			*inputLine = line;
			std::getline(std::cin, line);
		}

		std::cout << "Case #" << caseNumber << ": " << solve(input);
	}
	return 0;
}

