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
		UInt64	l	= 0;
		UInt64	t	= 0;
		UInt64	n	= 0;
		UInt64	c	= 0;
		
		std::cin >> l;
		std::cin >> t;
		std::cin >> n;
		std::cin >> c;

		std::vector<UInt64>	distances (n, 0);
		UInt64 i;
		for (i = 0; i < c; ++i) {
			UInt64 distance = 0;
			
			std::cin >> distance;
			distances[i] = distance;
		}
		for (; i < n; ++i)
			distances[i] = distances[i - c];
		
		std::vector<UInt64>	booster (n, 0);
		UInt64 sumTime = 0;
		UInt64 halfOfT = t / 2;
		for (i = 0; i < n; ++i) {
			UInt64 timeToAdd = distances[i];
			if (sumTime >= halfOfT) {
				booster[i] = distances[i];
			} else if (sumTime + timeToAdd > halfOfT) {
				booster[i] = sumTime + timeToAdd - halfOfT;
			}

			sumTime += timeToAdd;
		}
		sumTime *= 2;

		std::sort (booster.begin (), booster.end ());
		for (i = 0; i < n; ++i) {
			if (i == l)
				break;

			UInt64 reverseIndex = n - i - 1;
			sumTime -= booster[reverseIndex];
		}

		std::cout << "Case #" << ++counter << ": "  << sumTime << std::endl;
	}
}