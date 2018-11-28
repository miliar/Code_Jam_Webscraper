//============================================================================
// Name        : gcj-round0-c.cpp
// Author      : Martin Trenkmann
// Description : C. Theme Park
// Input       : *.in from std::cin
//============================================================================

#include <stdint.h>
#include <iostream>
#include <cstdlib>
#include <numeric>
#include <queue>

int main(int argc, char* argv[])
{
	uint64_t R(0);
	uint64_t N(0);
	uint64_t g(0);
	uint64_t T(0);
	uint64_t k_cur(0);
	uint64_t k_max(0);
	uint64_t euros(0);
	std::deque<uint32_t> queue;
	std::vector<uint32_t> passengers;

	std::cin >> T;
	for (unsigned t(0); t != T; ++t)
	{
		std::cin >> R >> k_max >> N;
		for (unsigned n(0); n != N; ++n)
		{
			std::cin >> g;
			queue.push_back(g);
		}
		for (unsigned r(0); r != R; ++r)
		{
			while (!queue.empty() && k_cur + queue.front() <= k_max)
			{
				k_cur += queue.front();
				passengers.push_back(queue.front());
				queue.pop_front();
			}
			euros += k_cur;
			std::copy(passengers.begin(), passengers.end(),
					  std::back_inserter(queue));
			passengers.clear();
			k_cur = 0;
		}
		std::cout << "Case #" << t+1 << ": " << euros << std::endl;
		queue.clear();
		euros = 0;
	}
	return EXIT_SUCCESS;
}
