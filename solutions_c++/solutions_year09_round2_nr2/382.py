#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

int main()
{
	std::string str;
	int cases; std::cin >> cases; getline(std::cin, str);
	for (int t = 1; t <= cases; ++t)
	{
		std::string tnum; getline(std::cin, tnum);
		
		std::vector<int> values;
		//while (tnum) { values.push_back(tnum % 10); tnum /= 10; };
		//std::reverse(values.begin(), values.end());
		for (int i = 0; i < tnum.length(); ++i)
		{ values.push_back(tnum.at(i) - '0'); };
		
		if (!next_permutation(values.begin(), values.end()))
		{
			std::sort(values.begin(), values.end());
			values.insert(values.begin(), 0);
			int zeroes = std::count(values.begin(), values.end(), 0);
			
			std::swap_ranges(values.begin() + zeroes, values.begin() + zeroes + 1, values.begin());
		};
		
		std::cout << "Case #" << t << ": ";
		for (std::vector<int>::iterator i = values.begin(); i != values.end(); ++i) std::cout << *i;
		std::cout << std::endl;
	};
};
