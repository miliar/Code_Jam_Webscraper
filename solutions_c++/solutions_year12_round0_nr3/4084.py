/* Hezekiah's Google Code Jam Solution
 * Usage: codejam < file.in > file.out
 */

#include <string>
#include <vector>
#include <iostream>
#include <sstream>

unsigned digit(unsigned d) {
	return d == 1u ? 10u : 10u * digit(d - 1u);
}

std::string solve(const std::vector<std::string>& input) {
	unsigned a, b, digits = 1u, pairs = 0u;
	std::istringstream(input[0u]) >> a >> b;
	while(a / digit(digits)) {
		++digits;
	}

	for(unsigned n = a; n < b; ++n) {
		for(unsigned m = n + 1u; m <= b; ++m) {
			for(unsigned d = 1u; d < digits; ++d) {
				unsigned digitD = digit(d);
				unsigned switched = n / digitD + (n % digitD) * digit(digits - d);
				if(switched == m) {
					++pairs;
					break;
				}
			}
		}
	}

	std::ostringstream output;
	output << pairs << '\n';
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

