/* Hezekiah's Google Code Jam Solution
 * Usage: codejam < file.in > file.out
 */

#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cmath>

std::string solve(const std::vector<std::string>& input) {
	unsigned dancers, surprising, target, score, above = 0u;
	std::istringstream inStream(input[0u]);
	inStream >> dancers >> surprising >> target;

	for(unsigned dancer = 0u; dancer < dancers; ++dancer) {
		inStream >> score;
		if(score > 1u) {
			score = std::ceil(score / 3.f);
			if(score >= target) {
				++above;
			} else if(score + 1u == target && surprising) {
				++above;
				--surprising;
			}
		} else if(score >= target) {
			++above;
		}
	}

	std::ostringstream output;
	output << above << '\n';
	return output.str();
}

unsigned moreLines(const std::string& line) {
	return 0u;
}

int main() {
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

