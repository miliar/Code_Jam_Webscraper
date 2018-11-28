
#include <iostream>
#include <cstdlib>

main ()
{
	int cases;
	std::cin >> cases;

	for (int x = 1; x <= cases; ++x) {
		int numCandies;
		std::cin >> numCandies;

		int realTotal = 0;
		int fakeTotal = 0;
		int minimum = 1000001;

		for (int candy = 0; candy < numCandies; ++candy) {
			int value;
			std::cin >> value;
			realTotal += value;
			fakeTotal ^= value;
			minimum = std::min (minimum, value);
		}

		std::cout << "Case #" << x << ": ";
		if (fakeTotal == 0) {
			std::cout << realTotal - minimum;
		} else {
			std::cout << "NO";
		}
		std::cout << std::endl;
	}

}

