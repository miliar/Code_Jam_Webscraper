#include <string>
#include <iostream>
#include <fstream>
#include <boost/lexical_cast.hpp>
#include <sstream>
#include <boost/format.hpp>
#include <stdint.h>

uint64_t descend(const char * cur_target_place, const char * cur_seek_place)
{
	if(*cur_target_place == 0)
	{
		return 1;
	}
	uint64_t acc = 0;
	while(*cur_seek_place != 0)
	{
		if(*cur_target_place == *cur_seek_place)
		{
			acc += descend(cur_target_place+1, cur_seek_place+1);
		}
		++cur_seek_place;
	}
	return acc;
}

int main(int argc, char *argv[])
{
	std::ofstream file("log.txt");

	std::string line;

	std::getline(std::cin, line);

	int N = boost::lexical_cast<int>(line);

	const char target[] = "welcome to code jam";

	for(int i = 0; i < N; ++i)
	{
		std::getline(std::cin, line);

		std::stringstream buf;

		uint64_t count = descend(target, line.c_str());

		buf << boost::format("%04u") % count;

		line = buf.str();

		buf.str("");
		buf << boost::format("Case #%d: %s\n") % int(i+1) % line.substr(line.size()-4);
		std::cout << buf.str();
		file << buf.str();
	}

}