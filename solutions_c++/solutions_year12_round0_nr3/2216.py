#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <set>

int main()
{
	int T;
	std::cin >> T;
	char buffer[7] = {0,};
	for(int i = 0; i < T; ++i)
	{
		int down;
		std::cin >> down;
		int up;
		std::cin >> up;
		int pairs = 0;
		std::set<int> checked;
		for(int j = down; j <= up; ++j)
		{
			if(checked.find(j) != checked.end())
			{
				continue;
			}
			std::stringstream ss;
			ss << j;
			std::string number(ss.str());
			if(number.size() == 1)
			{
				continue;
			}
			std::set<int> unique;
			unique.insert(j);
			for(int k = 1; k < number.size(); ++k)
			{
				std::rotate(number.begin(), number.begin()+1, number.end());
				if(number[0] == '0')
				{
					continue;
				}
				int rotated = std::atoi(number.c_str());
				if(rotated >= down && rotated <= up)
				{
					unique.insert(rotated);
					checked.insert(rotated);
				}
			}
			int elems = unique.size();
			pairs += elems * (elems-1) / 2;
		}
		std::cout << "Case #" << i+1 << ": " << pairs << std::endl;
	}
	return 0;
}

