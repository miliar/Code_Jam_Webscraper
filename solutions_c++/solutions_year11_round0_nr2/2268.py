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
#include <set>

struct Combine
{
	char c1;
	char c2;
	char res;
};

struct Oppose
{
	char c1;
	char c2;
};

std::string Solve( const std::vector<Combine>& combineList,
				   const std::vector< Oppose >& opposeList,
				   const std::vector<char>& str  )
{
	std::vector<char> result;

	for( std::vector<char>::const_iterator it = str.begin(); it != str.end(); ++it )
	{
		result.push_back( *it );

		if( result.size() >=2 )
		{
			std::vector<Combine>::const_iterator itComb;
			for( itComb = combineList.begin(); itComb != combineList.end(); ++itComb )
			{
				size_t size = result.size();

				if( ( result[ size -1 ] == itComb->c1 && result[ size -2 ] == itComb->c2 )
			     || ( result[ size -1 ] == itComb->c2 && result[ size -2 ] == itComb->c1 ) )
			     {
					result.pop_back();
					result.back() = itComb->res;
					break;
			     }
			}
			if( itComb == combineList.end())
			{
				std::set<char> resultSet( result.begin(), result.end() );

				for( std::vector< Oppose >::const_iterator itOpp = opposeList.begin(); itOpp != opposeList.end(); ++itOpp )
				{
					if( resultSet.find( itOpp->c1 ) != resultSet.end() && resultSet.find( itOpp->c2 ) != resultSet.end() )
					{
						result.clear();
						break;
					}
				}
			}
		}
	}
	std::ostringstream ostr;

	ostr << '[';
	for( size_t i = 0; i < result.size(); ++i )
	{
		ostr << result[i];
		if ( i != result.size() - 1 )
			ostr << ", ";
	}
	ostr << "]";
	return ostr.str();
}


int main( int argc, char** argv )
{
	std::ifstream ifs( "B-large.in" );
	std::ofstream output( "ouput.txt");

	int nbTest = 0;

	ifs >> nbTest;

	for( int i = 1; i <= nbTest; ++i )
	{
		int c = 0;
		ifs >> c;
		std::vector<Combine> combineList;

		for( int j = 0; j < c; ++j)
		{
			Combine combine;

			ifs >> combine.c1;
			ifs >> combine.c2;
			ifs >> combine.res;

			combineList.push_back(combine);
		}

		int d;
		ifs >> d;
		std::vector< Oppose > opposeList;

		for( int j = 0; j < d; ++j)
		{
			Oppose oppose;
			ifs >> oppose.c1;
			ifs >> oppose.c2;

			opposeList.push_back(oppose);
		}

		int n =0;

		ifs >> n;

		std::vector< char > str;
		for( int j = 0; j < n; ++j )
		{
			char c;

			ifs >> c;
			str.push_back( c );
		}
		std::string answer = Solve( combineList, opposeList, str  );
		output << "Case #" << i << ": " << answer << std::endl;
	}
	std::cout << "Finish" << std::endl;
 	return 0;
}
