#include <iostream>
#include <sstream>
#include <math.h>
#include <set>
#include <vector>

#define UInt32 unsigned long int


int main ()
{
	UInt32	numberOfCases	= 0;
	UInt32	counter			= 0;
	
	std::cin >> numberOfCases;
	while (counter < numberOfCases) {
		UInt32	numberOfCandies = 0;
		UInt32	minimum			= 0;
		UInt32	sum				= 0;
		UInt32	xorResult		= 0;

		std::cin >> numberOfCandies;
		for (UInt32 i = 0; i < numberOfCandies; ++i) {
			UInt32 candy = 0;
			
			std::cin >> candy;

			xorResult	^= candy;
			sum			+= candy;

			if (candy <= minimum || minimum == 0)
				minimum = candy;
		}
		
		if (xorResult == 0)
			std::cout << "Case #" << ++counter << ": " << sum - minimum << std::endl;
		else
			std::cout << "Case #" << ++counter << ": NO" << std::endl;
	}
}