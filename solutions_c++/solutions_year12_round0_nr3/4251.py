#include <memory>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>

void solveCase(std::ifstream& in, std::ofstream& out)
{
	int A,B;
	in >> A;
	in >> B;
	int n = A,m = B;
	int r = 0;

	while(n < m) {
		std::stringstream ss;
		ss << n;
		std::string sn = ss.str();

		std::size_t sz = sn.size();
		for (std::size_t i = 0 ; i < sz; i++) {
			std::string test = sn.substr(i, sz-i) + sn.substr(0, i);
			int toTest = atoi(test.c_str());
			if (toTest <= B && n < toTest) {
				//std::cout << sn << " " << test << std::endl;
				r++;
			}
		}

		n++;
	}

	out << r;
}

int main()
{
	std::string baseDir = "problems/";
	std::string testFile = "C-small-attempt0";

	std::ifstream in(baseDir + testFile + ".in");
	std::ofstream out(baseDir + testFile + ".out");
	std::string t = baseDir + testFile + ".in";

	std::cout << "Starting solving cases..." << std::endl;

	int numberOfCases = 0;
	int currCase = 0;

	in >> numberOfCases;

	while(currCase++ < numberOfCases) {
		out << "Case #" << currCase << ": ";
		try {
			solveCase(in, out);
		} catch (std::exception e) {

		}
		out << std::endl;
		std::cout << "Cases solved (" << currCase << "/" << numberOfCases << ")" << std::endl;
	}

	std::cout << "All cases solved!";
	return 0;
}
