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

		std::vector< std::string > strs;
		boost::split(strs, line, boost::is_any_of("\t "));

		size_t row = boost::lexical_cast< size_t > (strs[ 0 ]);
		size_t col = boost::lexical_cast< size_t > (strs[ 1 ]);

		std::vector< std::string > tmp;

		for (size_t j = 0; j < row; ++j)
		{
			getline(fin, line);
			tmp.push_back( line );
		}

		bool impossible = false;

		for (size_t j = 0; j < row; ++j)
		{
			
			for (size_t x = 0; x < col; ++x)
			{
				if ((tmp[ j ][ x ] == '.') || (tmp[ j ][ x ] == '/') || (tmp[ j ][ x ] == '\\')) { continue ; }

				if ((x == col - 1) || (tmp[ j ][ x + 1 ] == '.')) { impossible = true; break; }
				if ((j == row - 1) || (tmp[ j + 1 ][ x ] == '.')) { impossible = true; break; }
				if ((j == row - 1) || (x == col - 1) || (tmp[ j + 1 ][ x + 1 ] == '.')) { impossible = true; break; }

				tmp[ j ][ x ] = '/';
				tmp[ j ][ x + 1 ] = '\\';
				tmp[ j + 1 ][ x ] = '\\';
				tmp[ j + 1 ][ x + 1 ] = '/';
			}

			if (impossible) { break; }
		}

		fout << "Case #" << i + 1 << ": " << std::endl;
		if (impossible)
		{
			fout << "Impossible" << std::endl;
		}
		else
		{
			for (size_t j = 0; j < row; ++j)
			{
				fout << tmp[ j ] << std::endl;
			}
		}
	}

	fout.close();
	fin.close();
}
