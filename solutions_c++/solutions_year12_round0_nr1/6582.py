#include <iostream>
#include <string>
#include <stdio.h>
#include<fstream>
#include <map>


static std::map< char, char> translate_map;

void pInit_Map( void )
{
	std::string normal_english = "our language is impossible to understand"
															 "there are twenty six factorial possibilities"
															 "so it is okay if you want to just give up";

  std::string googelrese = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
													 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
													"de kr kd eoya kw aej tysr re ujdr lkgc jv";

	
	translate_map.insert( std::make_pair( 'y', 'a' ) );
	translate_map.insert( std::make_pair( 'e', 'o' ) );
	translate_map.insert( std::make_pair( 'q', 'z' ) );
	translate_map.insert( std::make_pair( 'z', 'q' ) );

	for ( size_t i = 0; i < normal_english.length() ; i++ )
	{
		if (! translate_map.count (  googelrese.at(i) ) )
		{
			translate_map.insert( std::make_pair( googelrese.at(i), normal_english.at(i) ) );
			
		}
	}



}
std::string pTranslate_To_Normal( const std::string & _input )
{
	std::string output = "";
	for ( size_t i = 0; i < _input.length() ; i++ )
	{
		std::map< char, char >::iterator iter =  translate_map.find ( _input.at(i) );
		if ( iter != translate_map.end() )
		{
			output += iter->second;
		}
		else
		{
			std::cerr<< "no equivalent for '"<< _input.at(i)<<"' ." << std::endl;
		  output += _input.at(i);
		}
	}
	return output;
}

int main( int argc, const char* argv[] )
{

	pInit_Map();
	std::ifstream my_input_File;
	std::ofstream my_output_File;

	my_output_File.open("output.txt");

	my_input_File.open(argv[1]);
	if ( my_input_File.is_open() ) 
	{
		int number_tests = 0;
		my_input_File >> number_tests;
		std::string line;
		std::getline(my_input_File,line);

		for ( int current_case = 1; current_case <= number_tests ; current_case++ )
		{
			std::getline(my_input_File,line);
			std::string translated = pTranslate_To_Normal( line );
			
			my_output_File<<"Case #"<<current_case<<":"<<" "<<translated<<std::endl;
			//std::cout<<"Case #"<<current_case<<":"<<" "<<translated<<std::endl;
		}

	}

	my_input_File.close();
	my_output_File.close();
	std::cout << "Done!\n";

	return 0;
}

