#include <iostream>
#include <vector>
#include <algorithm>
#include "math.h"

int main(int argc, char* argv[])
{
	int numCases;
	std::cin >> numCases;
	for (int i=0; i<numCases; i++)
	{
		int numGooglers, numSusprise, score;
		std::cin >> numGooglers >> numSusprise >> score;
		std::vector<int> points;
		points.reserve(numGooglers);
		for (int j=0; j<numGooglers; j++)
		{
			int result;
			std::cin >> result;
			points.push_back(result);
		}
		if (score == 0)
		{
			std::cout << "Case #" << (i+1) << ": " << numGooglers << std::endl;
			continue;
		}
		int result = 0;
		int limitValue = score*3 - 2;
		int limitSurprise = score*3 - 2*2;
		if (limitSurprise < 1) limitSurprise = 1;
		sort(points.begin(), points.end());
		std::vector<int>::reverse_iterator it;
		for (it = points.rbegin(); it!=points.rend(); ++it)
		{
			if ((*it) >= limitValue)
				result ++;
			else if ((*it) >= limitSurprise && numSusprise > 0)
			{
				result++;
				numSusprise--;
				if (numSusprise == 0) break;
			}
		}
		std::cout << "Case #" << (i+1) << ": " << result << std::endl;
	}
	return 0;
}

