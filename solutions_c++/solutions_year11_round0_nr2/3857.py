// \author martin.trenkmann@gmail.com
// $ g++ -Wall --std=c++0x gcj2011-r0-pB.cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <map>


void
apply_combinations(std::string& list,
                   const std::map<std::string, char>& combinations)
{
	const unsigned suffix_len(2);
	if (list.size() < suffix_len) return;
	std::string suffix = list.substr(list.size() - suffix_len);
	std::sort(suffix.begin(), suffix.end());
	for (auto it(combinations.begin()); it != combinations.end(); ++it)
	{
		if (it->first == suffix)
		{
			list.replace(list.size() - suffix_len, suffix_len, 1, it->second);
			break;
		}
	}
}

void
apply_opposites(std::string& list, const std::map<char, char>& opposites)
{
	if (list.empty()) return;
	for (auto it(opposites.begin()); it != opposites.end(); ++it)
	{
		if (*list.rbegin() == it->first &&
		    list.find(it->second) != std::string::npos)
		{
			list.clear();
			break;
		}
	}
}

const std::string
print_list(const std::string& list)
{
	std::string list_str;
	list_str.push_back('[');
	for (auto it(list.begin()); it != list.end(); ++it)
	{
		if (it != list.begin()) list_str.append(", ");
		list_str.push_back(*it);
	}
	list_str.push_back(']');
	return list_str;
}

int
main(int argc, char* argv[])
{
	unsigned t;
	std::cin >> t;
	for (unsigned i = 0; i != t; ++i)
	{
		unsigned c; 
		std::cin >> c;
		const unsigned suffix_len(2);
		std::string combination, lhs;
		std::map<std::string, char> combinations;
		for (unsigned j = 0; j != c; ++j)
		{
			std::cin >> combination;
			lhs = combination.substr(0, suffix_len);
			std::sort(lhs.begin(), lhs.end());
			combinations[lhs] = combination.at(suffix_len);
		}
		
		unsigned d;
		std::cin >> d;
		std::string opposite;
		std::map<char, char> opposites;
		for (unsigned j = 0; j != d; ++j)
		{
			std::cin >> opposite;
			opposites[opposite.at(0)] = opposite.at(1);
			opposites[opposite.at(1)] = opposite.at(0);
		}
		
		unsigned n;
		std::string elements, list;
		std::cin >> n >> elements;
		for (auto it(elements.begin()); it != elements.end(); ++it)
		{
			list.push_back(*it);
			apply_combinations(list, combinations);
			apply_opposites(list, opposites);
		}		
		
		std::cout << "Case #" << i+1 << ": " << print_list(list) << std::endl;
	}
	
	return 0;
}

