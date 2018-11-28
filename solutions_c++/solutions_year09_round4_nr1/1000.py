#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main()
{
	int num_cases = 0;
	std::cin >> num_cases;
	for (int i = 1; i <= num_cases; ++i)
	{
		int num_rows = 0;
		(std::cin >> num_rows).ignore();

		std::vector<int> matrix;
		std::string line;
		for (int j = 0; j < num_rows; ++j)
		{
			std::getline(std::cin, line);
			std::string::size_type last_one_pos = line.find_last_of('1');
			if (last_one_pos == std::string::npos)
				matrix.push_back(0);
			else
				matrix.push_back(last_one_pos + 1);
			std::cerr << j << ": " << matrix.back() << std::endl;
		}

		int total = 0;
		for (int y = 0; y < num_rows; ++y)
		{
			if (matrix[y] <= y + 1)
				continue;

			int target = y + 1;
			while (target < num_rows)
			{
				++total;
				if (matrix[target] <= y + 1)
					break;
				++target;
			}

			for (int y2 = target; y2 > y; --y2)
				std::swap(matrix[y2], matrix[y2 - 1]);
		}

		std::cout << "Case #" << i << ": " << total << std::endl;
	}
	return 0;
}
