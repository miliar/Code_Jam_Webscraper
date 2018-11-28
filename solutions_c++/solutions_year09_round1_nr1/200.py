#include <iostream>
#include <set>
#include <string>
#include <vector>

#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>

std::vector<std::vector<int> > ok_values(11);

bool IsOK(int base, int value)
{
	std::set<int> checked_values;
	while (value > 0)
	{
		if (checked_values.find(value) != checked_values.end())
			return false;
		checked_values.insert(value);

		std::vector<int> values;
		while (value > 0)
		{
			values.push_back(value % base);
			value /= base;
		}

		for (std::size_t i = 0; i < values.size(); ++i)
			value += (values[i] * values[i]);

		if (value == 1)
			return true;
	}
	return false;
}

int Calculate(const std::vector<int> &bases)
{
	for (int value = 2; ; ++value)
	{
		bool is_ok = true;
		for (std::size_t i = 0; i < bases.size(); ++i)
		{
			if (!IsOK(bases[i], value))
			{
				is_ok = false;
				break;
			}
		}
		if (is_ok)
			return value;
	}

	return -1;
}

int main()
{
	int num_cases;
	std::cin >> num_cases;

	std::string line;
	std::getline(std::cin, line);

	int count = 0;
	while (std::getline(std::cin, line))
	{
		std::vector<std::string> base_strings;
		boost::algorithm::split(base_strings, line, boost::is_space());

		std::vector<int> bases;
		for (std::size_t i = 0; i < base_strings.size(); ++i)
			bases.push_back(boost::lexical_cast<int>(base_strings[i]));

		std::cout << "Case #" << ++count << ": "
			<< Calculate(bases) << std::endl;
	}

	return 0;
}
