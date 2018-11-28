#include <iostream>
#include <vector>
#include <fstream>
#include <exception>
#include <math.h>
#include <cstdlib>
#include <set>
#include <algorithm>
#include <map>
#include <sstream>

typedef std::vector< std::string > T_Values;

T_Values* Solve( T_Values& values )
{
	for( int i = 0; i < values.size(); ++i )
	{
		std::string line = values[i];
		for( int j = 0; j < line.size(); ++j  )
		{
			if( line[j] == '#'
		    &&  j + 1 < line.size() && line[j + 1] == '#'
		    &&	i  + 1 < values.size() && values[i+1][j] == '#'
		    && 	values[i+1][j+1] == '#' )
			{
				values[i][j] = '/';
				values[i][j+1] = '\\';
				values[i+1][j] = '\\';
				values[i+1][j+1] = '/';
			}
		}
	}

	for( int i = 0; i < values.size(); ++i )
	{
		std::string line = values[i];
		for( int j = 0; j < line.size(); ++j  )
		{
			if( line[j] == '#')
				return 0;
		}
	}
	return &values;
}

int main( int argc, char** argv )
{
	const std::string inputStr = "A-large.in";

	const std::string outputStr( inputStr + "-result" );
	std::ifstream ifs( inputStr.c_str() );
	std::ofstream file( outputStr.c_str() );
	std::ostringstream output;

	int nbTest = 0;

	ifs >> nbTest;

	for( int i = 1; i <= nbTest; ++i )
	{
		int r, c;

		ifs >> r,c ;

		T_Values values;
		std::string line;
		std::getline( ifs, line);
		for( int j = 0; j < r; ++j )
		{
			std::getline( ifs, line);
			values.push_back( line);
		}

		std::vector<std::string>* result = Solve( values );
		output << "Case #" << i << ": " << std::endl;

		if( result )
		{
			for( int i = 0; i < result->size(); ++i )
				output << (*result)[i] << std::endl;
		}
		else
			output << "Impossible" << std::endl;
	}
	file << output.str();
	std::cout << output.str();
	std::cout << "Finish" << std::endl;
 	return 0;
}
