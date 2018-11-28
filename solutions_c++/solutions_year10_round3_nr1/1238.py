//============================================================================
// Name        : gcj-round1c-a.cpp
// Author      : Martin Trenkmann
// Description : xxx
// Input       : *.in from std::cin
//============================================================================

#include <stdint.h>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

int main(int argc, char* argv[])
{
	unsigned task_count(0);
	unsigned wire_count(0);
	unsigned intersection(0);

	typedef std::pair<unsigned, unsigned> wire_t;

	std::cin >> task_count;
	for (unsigned t(0); t != task_count; ++t)
	{
		std::cin >> wire_count;
		std::vector<wire_t> wires;
		for (unsigned i(0); i != wire_count; ++i)
		{
			wires.push_back(std::make_pair(0, 0));
			std::cin >> wires.back().first >> wires.back().second;
//			std::cout << wires.back().first << " " << wires.back().second << std::endl;
		}

		for (std::vector<wire_t>::iterator i(wires.begin()); i < wires.end();)
		{
			for (std::vector<wire_t>::iterator j(wires.begin()); j < wires.end(); ++j)
			{
				if ((i->first < j->first && i->second > j->second) ||
					(i->first > j->first && i->second < j->second))
				{
					++intersection;
				}
			}
			i = wires.erase(i);
		}

		// find intersections


		std::cout << "Case #" << t+1 << ": " << intersection << std::endl;
		intersection = 0;
	}
	return EXIT_SUCCESS;
}
