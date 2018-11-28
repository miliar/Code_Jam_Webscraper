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

typedef std::vector< int > T_Values;

std::string Solve( int l, int h, const T_Values& values )
{
	for( int i = l; i <= h; ++i )
	{
		int j = 0;
		for( j = 0;j < values.size(); ++j )
		{
			int v = values[j];

			if( v % i != 0 && i % v != 0 )
				break;
		}
		if( j == values.size() )
		{
			std::ostringstream ostr;

			ostr << i;

			return ostr.str();
		}
	}
	return "NO";
}

int main( int argc, char** argv )
{
	const std::string inputStr = "C-small-attempt1.in";

	const std::string outputStr( inputStr + "-result" );
	std::ifstream ifs( inputStr.c_str() );
	std::ofstream file( outputStr.c_str() );
	std::ostringstream output;

	int nbTest = 0;

	ifs >> nbTest;

	for( int i = 1; i <= nbTest; ++i )
	{
		int n,l,h ;

		ifs >> n >> l >> h;

		T_Values values;
		for( int j = 0; j < n; ++j )
		{
				int n1, n2;
			ifs >> n1;
			values.push_back( n1 );
		}

		std::string result = Solve( l, h, values );
		output << "Case #" << i << ": " << result << std::endl;
	}
	file << output.str();
	std::cout << output.str();
	std::cout << "Finish" << std::endl;
 	return 0;
}
