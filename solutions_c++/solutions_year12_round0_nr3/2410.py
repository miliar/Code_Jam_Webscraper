#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdint>

std::ifstream infile("input.txt");
std::ofstream outfile("output.txt");

#define DEBUG false

int main(int argc, char *argv[]) {
	uint64_t testcases, iteration;
	infile >> testcases;
	for(iteration = 0; iteration < testcases; iteration++) {
		uint64_t A, B, size;
		infile >> A >> B;

		if(DEBUG) std::cout << "A, B: " << A << ", " << B << std::endl;

		if(A < 10 && B < 10) { // 1 digit - no recycled numbers
			outfile << "Case #" << (iteration + 1) << ": 0" << std::endl;
			continue;
		}

		uint64_t value, pairs = 0;
		std::string n, m;
		std::stringstream ss;
		for(value = A; value <= B; value++) {
			ss << value;
			n = ss.str();
			m = ss.str();

			std::rotate(m.begin(), m.end() - 1, m.end());

			unsigned int length = n.length();

			uint64_t nValue;
			std::istringstream(n) >> nValue;

			while(n != m) {
				if(m[0] != '0') {
					uint64_t mValue;
					std::istringstream(m) >> mValue;

					if(mValue <= B && mValue > nValue && mValue >= A) {
						pairs++;

						if(DEBUG) std::cout << "\t(n, m): (" << n << ", " << mValue << ")" << std::endl;

					}
				}

				std::rotate(m.begin(), m.end() - 1, m.end());
			}

			ss.str("");
		}

		outfile << "Case #" << (iteration + 1) << ": " << pairs << std::endl;
	}
	
	infile.close();
	outfile.close();
	return 0;
}
