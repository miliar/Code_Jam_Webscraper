//============================================================================
// Name        : gcj-round1b-a.cpp
// Author      : Martin Trenkmann
// Description : File Fix-it
// Input       : *.in from std::cin
//============================================================================

#include <stdint.h>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>

int main(int argc, char* argv[])
{
	std::string path;
	std::string line;
	unsigned task_count(0);
	unsigned given_line_count(0);
	unsigned create_line_count(0);
	std::set<std::string> paths;

	std::cin >> task_count;
	for (unsigned t(0); t != task_count; ++t)
	{
		std::cin >> given_line_count >> create_line_count;
		for (unsigned i(0); i != given_line_count; ++i)
		{
			std::cin >> line;
			for (unsigned j(1); j != line.size(); ++j)
			{
				if (line.at(j) == '/')
				{
					path = line.substr(0, j);
					paths.insert(path);
//					std::cout << "present: " << path << std::endl;
				}
			}
			paths.insert(line);
//			std::cout << "present: " << line << std::endl;
		}

		unsigned mkdir_count(0);
		for (unsigned i(0); i != create_line_count; ++i)
		{
			std::cin >> line;
			for (unsigned j(1); j != line.size(); ++j)
			{
				if (line.at(j) == '/')
				{
					path = line.substr(0, j);
					if (paths.find(path) == paths.end())
					{
						paths.insert(path);
//						std::cout << "create: " << path << std::endl;
						++mkdir_count;
					}
				}
			}
			if (paths.find(line) == paths.end())
			{
				paths.insert(line);
//				std::cout << "create: " << line << std::endl;
				++mkdir_count;
			}
		}

		std::cout << "Case #" << t+1 << ": " << mkdir_count << std::endl;
		paths.clear();
	}
	return EXIT_SUCCESS;
}
