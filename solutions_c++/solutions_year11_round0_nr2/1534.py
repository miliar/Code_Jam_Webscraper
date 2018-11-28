#include <map>
#include <iostream>
#include <string>
#include <boost/format.hpp>
#include <boost/lexical_cast.hpp>
#include <map>
#include <set>
#include <array>
#include <algorithm>
#include <cassert>

std::pair<char, char> min_max(char a, char b)
{
	return std::make_pair(std::min(a, b), std::max(a, b));
}

typedef std::array<int, 256> count_t;

int check_transforms(std::vector<char> & elements, count_t & count, const std::map<std::pair<char, char>, char> & transforms)
{
	if(elements.size() < 2) return 0;

	char a = *(elements.end()-2);
	char b = elements.back();
	auto itr = transforms.find(min_max(a,b));
	if(itr != transforms.end())
	{
		assert(count[a]);
		assert(count[b]);
		count[a]--;
		count[b]--;
		elements.pop_back();
		elements.back() = itr->second;
		count[elements.back()]++;
		return 1;
	}
	return 0;
}

void check_oppose(std::vector<char> & elements, count_t & count, const std::map<char, std::vector<char>> & oppose)
{
	auto itr = oppose.find(elements.back());

	if(itr == oppose.end()) return;

	auto v = std::find_if(itr->second.begin(), itr->second.end(), [&](char c) -> bool
	{
		return count[c] > 0;
	});

	if(v != itr->second.end())
	{
		std::fill(count.begin(), count.end(), 0);
		elements.clear();
		return;
	}
}

int main(int argc, char *argv[])
{
	int T;

	std::string line;

	std::getline(std::cin, line);

	T = boost::lexical_cast<int>(line);

	for(int t = 0; t < T; ++t)
	{
		std::getline(std::cin, line);

		std::stringstream buf;

		buf.str(line);

		int C, D, N;

		std::map<std::pair<char, char>, char> transforms;
		std::map<char, std::vector<char>> oppose;

		buf >> C;

		for(int i = 0; i < C; ++i)
		{
			std::string s;
			buf >> s;

			transforms.insert(std::make_pair(min_max(s[0],s[1]), s[2]));
		}

		buf >> D;

		for(int i = 0; i < D; ++i)
		{
			std::string s;
			buf >> s;

			oppose[s[0]].push_back(s[1]);
			oppose[s[1]].push_back(s[0]);
		}

		buf >> N;

		std::string s;
		buf >> s;

		count_t count;
		std::fill(count.begin(), count.end(), 0);
		std::vector<char> elements;

		for(int i = 0; i < N; ++i)
		{
			count[s[i]]++;
			elements.push_back(s[i]);

			while(check_transforms(elements, count, transforms)) {};

			check_oppose(elements, count, oppose);
		}

		std::cout << boost::format("Case #%d: [") % (t+1);

		if(elements.size() > 0)
		{
			std::cout << elements[0];
		
			for(size_t i = 1; i < elements.size(); ++i)
			{
				std::cout << ", " << elements[i];
			}
		}

		std::cout << "]" << std::endl;
	}

	return 0;
}