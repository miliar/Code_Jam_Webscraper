#include <iostream>
#include <fstream>
#include <sstream>
#include <boost/format.hpp>
#include <boost/lexical_cast.hpp>
#include <map>
#include <list>
#include <string>
#include <stack>
#include <set>
#include <vector>
#include "matrix.h"
#include <algorithm>


int main(int argc, char *argv[])
{
	std::ofstream file("log.txt");

	std::string line;

	std::getline(std::cin, line);

	int T = boost::lexical_cast<int>(line);

	std::stringstream buf;

	for(int i = 0; i < T; ++i)
	{
		std::getline(std::cin, line);

		std::string orig = "0" + line;

		bool worked = std::next_permutation(orig.begin(), orig.end());

		assert(worked);

		if(orig[0] == '0')
			orig = orig.substr(1);

		buf.str("");
		buf << boost::format("Case #%d: %s\n") % int(i+1) % orig;
		std::cout << buf.str();
		file << buf.str();
	}
}