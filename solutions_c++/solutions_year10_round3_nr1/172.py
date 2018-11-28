#include <iostream>

int main() {
	int nCases;
	std::cin >> nCases;
	for (int i = 0; i < nCases; ++i) {
		int nWires;
		std::cin >> nWires;
		std::pair<int, int> values[1000];
		int nIntersections = 0;
		for (int j = 0; j < nWires; ++j) {
			std::cin >> values[j].first;
			std::cin >> values[j].second;
			for (int k = 0; k < j; ++k) {
				// check for intersections
				// std::cerr << "Comparing ("
				//           << values[k].first << "," << values[k].second 
				// 		  << ") against ("
				// 		  << values[j].first << "," << values[j].second 
				// 		  << ")" << std::endl;
				if ((values[k].first  < values[j].first &&
				     values[k].second > values[j].second) ||
				    (values[k].first  > values[j].first &&
				     values[k].second < values[j].second))
				{
					++nIntersections;
				}
			}
		}
		std::cout << "Case #" << i + 1 << ": " << nIntersections << std::endl;
	}
}
