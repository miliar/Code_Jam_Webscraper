#include <iostream>
#include <sstream>
#include <math.h>
#include <set>
#include <vector>
#include <algorithm>


#define UInt64 unsigned long long


int main ()
{
	int	numberOfCases	= 0;
	int	counter			= 0;
	
	std::cin >> numberOfCases;
	while (counter < numberOfCases) {
		int	n	= 0;
		int	l	= 0;
		int	h	= 0;
		
		std::cin >> n;
		std::cin >> l;
		std::cin >> h;
		
		std::vector<bool>	allowedFrequencies (h + 1, true);

		for (int i = 0; i < l; ++i) {
			allowedFrequencies[i] = false;
		}

		for (int i = 0; i < n; ++i) {
			int frequnecy = 0;
			
			std::cin >> frequnecy;
			
			for (int j = l; j <= h; ++j) {
				if (!allowedFrequencies[j])
					continue;
				
				if (frequnecy == j)
					continue;
				
				if (j > frequnecy &&
					j % frequnecy  == 0)
				{
					continue;
				}
				
				if (frequnecy > j &&
					frequnecy % j == 0)
				{
					continue;
				}

				allowedFrequencies[j] = false;
			}
		}
		
		int retValue = 0;
		for (int i = l; i <= h; ++i) {
			if (!allowedFrequencies[i])
				continue;

			retValue = i;
			break;
		}

		if (retValue != 0)
			std::cout << "Case #" << ++counter << ": "  << retValue << std::endl;
		else
			std::cout << "Case #" << ++counter << ": NO" << std::endl;
	}
}