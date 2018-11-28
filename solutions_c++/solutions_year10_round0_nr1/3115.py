//============================================================================
// Name        : gcj-round0-a.cpp
// Author      : Martin Trenkmann
// Description : A. Snapper Chain
// Input       : *.in from std::cin
//============================================================================

#include <stdint.h>
#include <iostream>
#include <cstdlib>
#include <cmath>

int main(int argc, char* argv[])
{
	uint64_t test_count;    // T
	uint64_t snapper_count; // N
	uint64_t toggle_count;  // K
	uint64_t interval_bulb_on;

	std::cin >> test_count;
	for (unsigned i(0); i != test_count; ++i)
	{
		std::cin >> snapper_count >> toggle_count;
		interval_bulb_on = std::pow(2, snapper_count);
		std::cout << "Case #" << i+1 << ": "
				  << ((toggle_count + 1) % interval_bulb_on ? "OFF" : "ON")
				  << std::endl;
	}
	return EXIT_SUCCESS;
}
