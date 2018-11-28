#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <iomanip>

#include <unistd.h>
#include <boost/foreach.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>

using namespace std;

std::vector< std::string > scores;
std::vector< double > results;
std::vector< double > wp;
std::vector< double > owp;
std::vector< double > oowp;

void process(std::string const & filename);

int main (int argc, char * argv[])
{
	process(argv[ 1 ]);

	return (EXIT_SUCCESS);
}

void process(std::string const & filename)
{
	std::ifstream fin(filename.c_str());

	std::string line;
	// First line is the number of testcast
	getline(fin, line);
	size_t test_case = boost::lexical_cast< size_t >( line );

	std::ofstream fout ("foobar");

	for (size_t i = 0; i < test_case; i++)
	{
		getline(fin, line);
		size_t teams = boost::lexical_cast< size_t >( line );
	
		scores.clear();
		results.clear();
		wp.clear();
		owp.clear();
		oowp.clear();

		for (size_t j = 0; j < teams; j++)
		{
			getline(fin, line);

			scores.push_back(line);
		}

		// WP
		for (size_t counter	= 0; counter < teams; counter++)
		{
			size_t won = 0;
			size_t total = 0;

			for(size_t x = 0; x < scores[ counter ].size(); x++)
			{
				if (scores[ counter ][ x ] == '1')
				{
					won++;
					total++;
				}
				else if (scores[ counter ][ x ] == '0')
				{
					total++;
				}
			}

			if (total == 0)
			{
				wp.push_back (0);
			}
			else
			{
				wp.push_back( double(won) / total);
			}
		}

		// OWP
		for (size_t counter = 0; counter < teams; counter++)
		{
			double average = 0;
			size_t team_count = 0;

			for (size_t x = 0; x < teams; x++)
			{
				if (scores[ x ][ counter ] == '.') { continue; }

				size_t won = 0;
				size_t total = 0;

				for (size_t y = 0; y < scores[ x ].size(); y++)
				{
					if (y == counter) { continue; }

					if (scores[ x ][ y ] == '1')
					{
						won++;
						total++;
					}
					else if (scores[ x ][ y ] == '0')
					{
						total++;
					}
				}

				if (total == 0)
				{
					average += 0;
				}
				else
				{					
					average += (double) won / total;
				}

				team_count++;
			}

			if (team_count == 0)
			{
				owp.push_back( 0 );
			}
			else
			{
				owp.push_back( average / team_count );
			}
		}
	
		// OOWP
		for (size_t counter = 0; counter < teams; counter++)
		{
			double average = 0;
			size_t team_count = 0;

			for (size_t x = 0; x < scores[ counter ].size(); x++)
			{
				if (scores[ counter ][ x ] != '.')
				{
					average += owp[ x ];
					team_count++;
				}
			}

			if (team_count == 0)
			{
				oowp.push_back( 0 );
			}
			else
			{
				oowp.push_back( average / team_count );
			}
		}

		// Result
		for (size_t counter = 0; counter < teams; counter++)
		{
			results.push_back( wp[ counter ] * 0.25 + owp[ counter ] * 0.5 + oowp[ counter ] * 0.25 );
		}

		
		fout << "Case #" << i + 1 << ":" << std::endl;

		for (size_t counter = 0; counter < teams; counter++)
		{
			fout << setprecision( 6 ) << results[ counter ] << std::endl;
		}
	}

	fout.close();
	fin.close();
}


