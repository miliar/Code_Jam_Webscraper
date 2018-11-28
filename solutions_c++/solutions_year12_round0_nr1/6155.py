#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <map>

int main(int argc, char* argv[])
{
	const char* PLAIN      = "qz our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	const char* GOOGLERESE = "zq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	std::map<char, char> MAPPING;

	for (int i = 0; i < std::strlen(PLAIN); ++i)
	{
		MAPPING[GOOGLERESE[i]] = PLAIN[i];
	}

	std::ifstream input("input.test");

	
	std::string line;
	
	std::getline(input, line);	

	int numberOfTestCases = std::atoi(line.c_str());

	int total = numberOfTestCases;

	while (numberOfTestCases--)
	{		
		std::getline(input, line);

		std::cout << "Case #" << total - numberOfTestCases << ": ";

		for (char c : line)
		{
			std::cout << MAPPING[c];
		}

		std::cout << std::endl;		
	}
	
	return EXIT_SUCCESS;
}