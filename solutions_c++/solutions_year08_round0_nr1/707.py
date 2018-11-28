// SavingUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <list>
#include <string>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <sstream>
#include <iterator>
#include <vector>

typedef std::list<std::string> Engines;
typedef std::vector<std::string> Queries;
//typedef std::list<std::string> Queries;


size_t tosize_t(const std::string& str)
{
	std::stringstream strm(str);
	size_t result = 0;
	strm >> result;

	return result;
}

size_t CountSwitches(const Engines& ens, const Queries& qs, Queries::const_iterator begin, Queries::const_iterator end)
{
	if (begin == end)
		return 0;	

	Queries::const_iterator last = end;

	for (Engines::const_iterator it = ens.begin(); it != ens.end(); ++it)
	{
		if (*it == *begin)
			continue;

		Queries::const_iterator qit = std::find(begin, end, *it);
		if (qit == end)
			return 0;

		if (last == end)
			last = qit;
		else
			last = last < qit ? qit : last;		
	}

	return 1 + CountSwitches(ens, qs, last, end);
}

/*size_t CountSwitches(const Engines& ens, const Queries& qs, Queries::const_iterator begin, Queries::const_iterator end)
{
	if (begin == end)
		return 0;

	size_t minCount = static_cast<size_t>(-1);

	for (Engines::const_iterator it = ens.begin(); it != ens.end(); ++it)
	{
		if (*it == *begin)
			continue;

		Queries::const_iterator qit = std::find(begin, end, *it);
		if (qit == end)
			return 0;

		size_t curCount = 1 + CountSwitches(ens, qs, qit, end);
		minCount = std::min(minCount, curCount);
	}

	return minCount;

}*/

int _tmain(int argc, _TCHAR* argv[])
{
	/*Engines ens;
	ens.push_back("Yeehaw");
	ens.push_back("NSM");
	ens.push_back("Dont Ask");
	ens.push_back("B9");
	ens.push_back("Googol");

	Queries qs;
	qs.push_back("Yeehaw");
	qs.push_back("Yeehaw");
	qs.push_back("Googol");
	qs.push_back("B9");
	qs.push_back("Googol");
	qs.push_back("NSM");
	qs.push_back("B9");
	qs.push_back("NSM");
	qs.push_back("Dont Ask");
	qs.push_back("Googol");

	std::cout << CountSwitches(ens, qs) << std::endl;*/

	//std::ifstream file("A-small-attempt3.in");
	//std::ifstream file("data.txt");
	std::ifstream file("A-large.in");	
	std::ofstream result("result.txt");

	std::string str;
	std::getline(file, str);

	size_t countTests = tosize_t(str);

	for (size_t i = 1; i <= countTests; ++i)
	{
		Engines ens;
		{
			std::getline(file, str);
			size_t countEns = tosize_t(str);
			
			for (size_t j = 0; j < countEns; ++j)
			{
				std::getline(file, str);
				ens.push_back(str);
			}
		}

		Queries qs;
		{
			std::getline(file, str);
			size_t countQs = tosize_t(str);

			for (size_t j = 0; j < countQs; ++j)
			{
				std::getline(file, str);
				qs.push_back(str);
			}
		}

		//bool ismin = false;
		//size_t count = CountSwitches(ens, qs, qs.begin(), qs.end(), ismin);

		size_t count = CountSwitches(ens, qs, qs.begin(), qs.end());

		std::cout << "Case #" << i <<": " << count << std::endl;
		result << "Case #" << i <<": " << count << std::endl;
	}

	return 0;
}

