#include <iostream>
#include <sstream>

#define UInt32 unsigned long int


int main ()
{
	std::string	str;
	UInt32		n				= 1000;
	UInt32		numberOfCases	= 0;
	UInt32		counter			= 0;
	UInt32		groups[n];
	UInt32		values[n];
	UInt32		nextRound[n];

	std::cin >> numberOfCases;

	while (numberOfCases > 0) {
		UInt32	k				= 0;
		UInt32	r				= 0;
		UInt32	numberOfGroups	= 0;
		UInt32	budget			= 0;
		
		std::cin >> r;
		std::cin >> k;
		std::cin >> numberOfGroups;

		for (UInt32 i = 0; i < numberOfGroups; ++i) {
			std::cin >> groups[i];
		}

		for (UInt32 i = 0; i < numberOfGroups; ++i) {
			UInt32 newIndex	= i + 1 < numberOfGroups ? i + 1 : 0;
			values[i]		= groups[i];

			while (newIndex != i && values[i] + groups[newIndex] <= k) {
				values[i]	+= groups[newIndex];
				newIndex	= newIndex + 1 < numberOfGroups ? newIndex + 1 : 0;
			}

			nextRound[i]	= newIndex;
		}

		UInt32 nextIndex = 0;
		for (UInt32 i = nextIndex; i < r; ++i) {
			budget		+= values[nextIndex];
			nextIndex	= nextRound[nextIndex];
		}

		std::cout << "Case #" << ++counter << ": " << budget << std::endl;

		--numberOfCases;
	}
}