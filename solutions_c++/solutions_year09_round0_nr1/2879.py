#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <algorithm>

void parse( const std::string& filename )
{
	std::ifstream ifs( filename.c_str() );
	if( ifs )
	{
		int L, D, N;

		ifs >> L;
		ifs >> D;
		ifs >> N;

		std::set<std::string> dict;
		for( int i = 0; i < D; ++i )
		{
			std::string word;
			ifs >> word;
			dict.insert( word );
		}

		std::ofstream ofs( "qualif-a.sh" );
		ofs << "#!/bin/sh" << std::endl;
		
		for( int i = 0; i < N; ++i )
		{
			std::string pattern;
			ifs >> pattern;

			ofs << "echo -n \"Case #" << i+1 << ": \";" << "echo \"";
			for( std::set<std::string>::iterator it = dict.begin(); it != dict.end(); ++it )
			{
			  ofs << *it << "\\n";
			}
			std::replace( pattern.begin(), pattern.end(), '(', '[' );
			std::replace( pattern.begin(), pattern.end(), ')', ']' );
			ofs <<  "\" | grep " << pattern << " | wc -l" << std::endl;
		}
	}
}

int main( int argc, char* argv[] )
{
	if( argc == 2 )
	{
		parse( argv[1] );
		return 0;
	}
	else
	{
		return 1;
	}
}
