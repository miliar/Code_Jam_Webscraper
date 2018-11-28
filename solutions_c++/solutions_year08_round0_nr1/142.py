#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>

std::ifstream in( "A-small.in" );
std::ofstream out( "A-small.out" );


int main(void)
{

	int n = 0;
	in >> n;

	for( int i = 0; i != n; ++i )
	{
		std::map<std::string,int> names;
		int s = 0, q = 0;
		in >> s;
		std::string temp;
		std::getline( in, temp, '\n' );
		for( int j = 0; j != s; ++j )
		{
			std::getline( in, temp, '\n' );
			names[temp] = j;
		}
		in >> q;
		std::map<std::string, int>::iterator it;
		std::vector<int> quer;
		std::getline( in, temp, '\n' );
		for( int j = 0; j != q; ++j )
		{
			std::getline( in, temp, '\n' );
			it = names.find( temp );
			if( it != names.end() )
				quer.push_back( it->second );
		}

		std::set<int> sets;
		for(int j = 0; j != s; ++j)
			sets.insert( j );

		int last;
		int count = 0;
		std::set<int>::iterator sit;
		for( int j = 0; j != q; ++j )
		{
			sit = sets.find( quer[j] );
			if( sit != sets.end() )
			{
				last = *sit;
				sets.erase( sit );
			}
			if( sets.empty() )
			{
				count++;
				for( int j = 0; j != s; ++j )
					if( j != last )
						sets.insert( j );
			}
		}

		out << "Case #" << i+1 << ": " << count << "\n";
	}

	return 0;
}