#include <iostream>
#include <sstream>
#include <math.h>

#define UInt32 unsigned long int


int main ()
{
	UInt32		numberOfCases	= 0;
	UInt32		counter			= 0;

	std::cin >> numberOfCases;
	
	while (counter < numberOfCases) {
		UInt32	n			= 0;
		UInt32	k			= 0;
		UInt32	upperLimit	= 0;

		std::cin >> n;
		std::cin >> k;

		upperLimit	= pow (2, n);
		k			= k % upperLimit;

		if (k == (upperLimit - 1))
			std::cout << "Case #" << ++counter << ": ON" << std::endl;
		else
			std::cout << "Case #" << ++counter << ": OFF" << std::endl;
	}
}