#include <iostream>
#include <cmath>

bool is_on(int pos, int times)
{
//	std::cerr << (times % (2 << pos)) << ":" << ((2 << pos) - 1) << std::endl;
	return (times % (2 << (pos - 1))) == (2 << (pos - 1)) - 1;
}

int main()
{
	int num_cases;
	std::cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
	{
		int pos, times;
		std::cin >> pos >> times;
		std::cerr << "pos: " << pos << ", times: " << times << std::endl;

		std::cout << "Case #" << (i + 1) << ": "
			<< (is_on(pos, times) ? "ON" : "OFF") << std::endl;
	}

	return 0;
}
