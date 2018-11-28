/*
   Built using boost 1.46.1 and gcc 4.4.3 on 10.04

   usage: ./magik <inputname> > <outputname>

   Note: this code is sooo bad :(
*/

#include <iostream>
#include <fstream>
#include <cstdio>
#include <list>
#include <vector>
#include <string>
#include <boost/cstdint.hpp>
#include <boost/spirit/include/qi.hpp>
#include <boost/spirit/include/phoenix_core.hpp>
#include <boost/spirit/include/phoenix_operator.hpp>
#include <boost/spirit/include/phoenix_stl.hpp>
#include <boost/algorithm/string/replace.hpp>

using namespace boost::phoenix;
using namespace boost::spirit;
using namespace boost::spirit::qi;
using namespace boost::spirit::ascii;


int main(int argc, char** argv)
{
	std::string magik;
	std::vector<char> upcoming;
	std::vector<std::pair<std::string, std::string> > m_combined;
	std::vector<std::pair<char, char> > m_empty;

	std::vector<std::string> m_allMagik;
	std::vector<std::vector<char> > m_allUpcoming;
	std::vector<std::vector<std::pair<std::string, std::string> > > m_allCombined;
	std::vector<std::vector<std::pair<char, char> > > m_allEmpty;

	if (argc != 2)
	{
		std::cerr << "You need to provide the .in file as input" << std::endl;
		return 1;
	}

	std::ifstream file;
	file.open(argv[1], std::ios::in);

	if (!file.is_open())
	{
		std::cerr << "Couldn't open specified file" << std::endl;
		return 1;
	}

	boost::uint16_t numberOfTestCases;
	std::string numberOfCases;
	
	std::getline(file, numberOfCases);
	if (!phrase_parse(numberOfCases.begin(), numberOfCases.end(), int_[ref(numberOfTestCases) = _1], boost::spirit::ascii::space))
	{
		std::cerr << "Failed to parse the first line in the file" << std::endl;
		return 1;
	}

	std::string combinedElement;
	std::string result;

	std::string testCase;
	for (std::size_t i = 0; i < numberOfTestCases; ++i)
	{
		std::getline(file, testCase);
		std::string::iterator stringIter = testCase.begin();

		int numberOfCombined = 0;
		if (!phrase_parse(stringIter, testCase.end(), (int_[ref(numberOfCombined)= _1]),
	             boost::spirit::ascii::space))
		{
			std::cerr << "Failed parsing." << std::endl;
			return 1;
		}

		while (numberOfCombined != 0)
		{
			--numberOfCombined;
			//for now assume one...
			std::string combined;
			std::string transform;
			char goodOne = 'a';
			char goodTwo = 'a';
			char final = 'b';
			if (!phrase_parse(stringIter, testCase.end(),
				(boost::spirit::ascii::char_[ref(goodOne) = _1] >>
				 boost::spirit::ascii::char_[ref(goodTwo) = _1] >>
				 boost::spirit::ascii::char_[ref(final) = _1]),
				 boost::spirit::ascii::space))
			{
				std::cerr << "Failed combinational parsing" << std::endl;
				return 1;
			}

			transform.push_back(final);
			combined.push_back(goodOne);
			combined.push_back(goodTwo);
			m_combined.push_back(std::make_pair(combined, transform));
			combined.clear();
			combined.push_back(goodTwo);
			combined.push_back(goodOne);
			m_combined.push_back(std::make_pair(combined, transform));
		}

		int numberOfDeletes = 0;
		if (!phrase_parse(stringIter, testCase.end(), (int_[ref(numberOfDeletes)= _1]),
	             boost::spirit::ascii::space))
		{
			std::cerr << "Failed parsing deletion number" << std::endl;
			return 1;
		}

		while (numberOfDeletes != 0)
		{
			--numberOfDeletes;
			char firstOne = 'a';
			char secondOne = 'a';
			if (!phrase_parse(stringIter, testCase.end(),
			     (boost::spirit::ascii::char_[ref(firstOne) = _1] >>
			      boost::spirit::ascii::char_[ref(secondOne) = _1]),
			      boost::spirit::ascii::space))
			{
				std::cerr << "Failed parsing delete elements" << std::endl;
				return 1;
			}

			m_empty.push_back(std::make_pair(firstOne, secondOne));
		}
			

		if (!phrase_parse(stringIter, testCase.end(), (int_ >> +boost::spirit::ascii::char_[push_back(ref(upcoming), _1)]), boost::spirit::ascii::space))
		{
			std::cerr << "Failed to parse the element list!" << std::endl;
		}

		m_allUpcoming.push_back(upcoming);
		upcoming.clear();

		m_allMagik.push_back(magik);
		magik.clear();

		m_allCombined.push_back(m_combined);
		m_combined.clear();

		m_allEmpty.push_back(m_empty);
		m_empty.clear();
	}

	//triple for loop ftw! ... fail
	for (std::size_t j = 0; j < m_allMagik.size(); ++j)
	{
		for (std::size_t i = 0; i < m_allUpcoming[j].size(); ++i)
		{
			m_allMagik[j].push_back(m_allUpcoming[j][i]);

			for (std::size_t k = 0; k < m_allCombined[j].size(); ++k)
			{
				boost::algorithm::replace_all(m_allMagik[j], m_allCombined[j][k].first, m_allCombined[j][k].second);			
			}

			for (std::size_t k = 0; k < m_allEmpty[j].size(); ++k)
			{
				if ((m_allMagik[j].find(m_allEmpty[j][k].first) != std::string::npos) &&
				    (m_allMagik[j].find(m_allEmpty[j][k].second) != std::string::npos))
				{
					m_allMagik[j].clear();
				}
			}
		}

		std::cout << "Case #" << j + 1 << ": [";

		for (std::size_t i = 0; i < m_allMagik[j].size(); ++i)
		{
			std::cout << m_allMagik[j][i];

			if ((i+1) < m_allMagik[j].size())
			{
				std::cout << ", ";
			}
		}

		std::cout << "]" << std::endl;
	} 
}
