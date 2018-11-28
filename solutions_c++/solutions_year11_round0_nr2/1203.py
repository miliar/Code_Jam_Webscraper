#include <map>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>

#include <unistd.h>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>

using namespace std;

std::vector< std::string > test_cases;
std::vector< std::string > results;

void read(std::string const & filename);
void write(std::string const & filename);

int main(int argc, char* argv[])
{
	read(argv[1]);

	BOOST_FOREACH (std::string input, test_cases)
	{
		std::vector< std::string > strs;
		boost::split(strs, input, boost::is_any_of("\t "));

		typedef std::map< char, char > opposes_type;
		opposes_type opposes;
		typedef std::map< char, std::map< char, char > > combines_type;
		combines_type combines;

		int current = 0;

		int combines_total = boost::lexical_cast< int >(strs[ current++ ]);
		// List of combines
		for(int i = 0; i < combines_total; ++i, ++current)
		{
			char first_ele(strs[ current ][0]);
			char second_ele(strs[ current ][1]);
			char combined_ele(strs[ current ][2]);

			if (combines.find(first_ele) == combines.end()) { combines[ first_ele ] = std::map< char, char >(); }
			if (combines.find(second_ele) == combines.end()) { combines[ second_ele ] = std::map< char, char >(); }

			combines[ first_ele ].insert( std::make_pair(second_ele, combined_ele) );
			combines[ second_ele ].insert( std::make_pair(first_ele, combined_ele) );
		}

		int opposes_total = boost::lexical_cast< int >(strs[ current++ ]);
		
		// List of opposes
		for (int i = 0; i < opposes_total; ++i, ++current)
		{
			char first_ele(strs[ current ][0]);
			char second_ele(strs[ current ][1]);
			
			opposes[ first_ele ] = second_ele;
			opposes[ second_ele ] = first_ele;
		}

		int ele_total = boost::lexical_cast< int >(strs[ current++ ]);
		std::string elements = strs[ current ];
		std::string invokes  = "";

		// Cast a spell
		for (int i = 0; i < elements.size(); ++i)
		{
			if (invokes.size() == 0) { invokes += elements[ i ]; continue; }

			char ele = elements[ i ];
		
			// Check for combination
			char last_ele = *(invokes.rbegin());
			combines_type::const_iterator ci = combines.find(last_ele);
			if (ci != combines.end())
			{
				std::map< char, char >::const_iterator iter = ci->second.find(ele);
				if (iter != ci->second.end())
				{
					std::string tmp = invokes.substr(0, invokes.size() - 1);
					invokes = tmp + iter->second;

					continue ;
				}
			}

		
			// Check for opposition
			if (invokes.find(opposes[ ele ]) != string::npos)
			{
				invokes = "";
			}
			else
			{
				invokes += ele;	
			}
		}

		results.push_back(invokes);
	}

	write("102.out");

	return (EXIT_SUCCESS);
}

void read(std::string const & filename)
{
	std::ifstream fin(filename.c_str());

	std::string line;
	// First line is the number of testcase
	getline(fin, line);

	while (getline(fin, line))
	{
		test_cases.push_back(line);
	}

	fin.close();
}

void write(std::string const & filename)
{
	std::ofstream fout(filename.c_str());

	int c = 1;
	BOOST_FOREACH (std::string spell, results)	
	{
		fout << "Case #" << c++ << ": [";
		
		for (int i = 0; i < int(spell.size()) - 1; ++i)
		{
			fout << spell[ i ] << ", ";
		}

		if (spell.size() != 0)
		{
			fout << spell[ spell.size() - 1 ] << "]" << std::endl;
		}
		else
		{
			fout << "]" << std::endl;
		}
	}

	fout.close();
}

