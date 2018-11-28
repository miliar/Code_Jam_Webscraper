// Krzysztof Czainski
// gcc version 4.3.1 (Gentoo 4.3.1 p1.0)
// using boost-1.35.0: www.boost.org

#include <iostream>
#include <map>
#include <iterator>

void processLine( std::istream& is, std::ostream& os, unsigned case_no );

int main()
{
	unsigned n;
	std::cin >> n;
	for ( unsigned i = 0 ; i < n ; ++i )
		processLine( std::cin, std::cout, i+1 );
}

void processLine( std::istream& is, std::ostream& os, unsigned case_no )
{
	unsigned s;
	is >> s >> std::ws;
	
	std::map< std::string, unsigned > map;
	
	for ( unsigned i = 0 ; i < s ; ++i )
	{
		std::string query;
		std::getline( is, query );
		map[query] = 0;
	}
	
	unsigned q, sRemaining = s, nSwitches = 0;
	is >> q >> std::ws;
	
	for ( unsigned i = 0 ; i < q ; ++i )
	{
		std::string query;
		std::getline( is, query );
		unsigned& qVal = map[query];
		if ( qVal == nSwitches )
		{
			if ( sRemaining > 1 )
			{
				--sRemaining;
				++qVal;
			}
			else
			{
				sRemaining = s-1;
				qVal += 2;
				++nSwitches;
			}
		}
	}
	
	os << "Case #" << case_no << ": " << nSwitches << "\n";
}
