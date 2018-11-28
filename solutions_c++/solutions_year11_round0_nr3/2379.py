#include <iostream>
#include <vector>
#include <fstream>
#include <exception>
#include <math.h>
#include <cstdlib>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>

std::string Solve( std::vector< int > ciList )
{
	int binaryOr = 0;

	for( size_t i = 0; i < ciList.size(); ++i )
	{
		binaryOr ^= ciList[i];
	}
	if( binaryOr != 0 )
		return "NO";

	std::sort( ciList.begin(), ciList.end() );
	if ( !ciList.empty())
		ciList[0] = 0;

	int sum = std::accumulate( ciList.begin(), ciList.end(), 0 );
	std::ostringstream ostr;

	ostr << sum;
	return ostr.str();
}

int main( int argc, char** argv )
{
	std::ifstream ifs( "C-large.in" );
	std::ofstream output( "ouput.txt");

	int nbTest = 0;
	int n = 0;

	ifs >> nbTest;

	for( int i = 1; i <= nbTest; ++i )
	{
		ifs >> n;

		std::vector< int > ciList;
		for( int j = 0; j < n; ++j )
		{
			int ci = 0;
			ifs >> ci;
			ciList.push_back( ci );
		}
		std::string answer = Solve( ciList );
		output << "Case #" << i << ": " << answer << std::endl;
	}
	std::cout << "Finish" << std::endl;
 	return 0;
}
