#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <time.h>
#include <iterator>
#include <stdlib.h>

const char *infile = "tmp.in";

std::string get_head( std::ifstream &in ) 
{ 
 std::string instring;
 std::getline( in, instring );
 return instring;
}

template < class T >
const int to_int( T obj )
{
    std::stringstream instr;
    int value;
    instr << obj;
    instr >> value;
    return value;
}

const std::string trim(const std::string istring)
{
    std::string::size_type first = istring.find_first_not_of(" \n\t\r\0xb");
    if (first == std::string::npos)
    {
        return std::string();
    }
    else
    {
        std::string::size_type last = istring.find_last_not_of(" \n\t\r\0xb");
        return istring.substr( first, last - first + 1);
    }
}


const std::vector< std::string > get_words( const std::string &source, const std::string separator = " ", bool trim_him = false )
{//Функция хороша тем что не использует итераторы а поэтому должна работать с любой кодировкой
 //и быть полностью переносимой (трабл с итераторами был в том что для многобайтового символа делается несколько итераций 
 //в цикле поэтому небыло гарантии правильности проверки на равенство
 //теперь нет ни одной проверки на равенство строк, все делается в недрах stl
    std::vector< std::string >  result;
    std::string::size_type fp = source.find( separator, 0 );
    std::string::size_type separator_length = separator.length();
    if( fp != std::string::npos && fp != 0 ) 
    { 
		trim_him ? result.push_back(  trim( source.substr( 0, fp ) ) ) : result.push_back( source.substr( 0, fp ) );
    }
    else if( fp == std::string::npos && source.length() > 0 ) 
    {  
		trim_him ? result.push_back( trim( source ) ) : result.push_back( source );

    } 
		
    while( fp != std::string::npos ) 
    {
    	std::string::size_type nextp = source.find( separator, fp + separator_length  );
	if( nextp == std::string::npos ) 
	{ 
		if( fp + separator_length >= source.length() ) break;
		if( trim_him ) 
		{
			result.push_back( trim( source.substr( fp + separator_length, source.length() - fp - separator_length )  ) );
		} 
		else 
		{  
			result.push_back( source.substr( fp + separator_length, source.length() - fp - separator_length ) );
		}
		break;
	} 
	if( trim_him )
	{ 
		result.push_back( trim( source.substr( fp + separator_length, nextp - fp - separator_length ) )  );
	}
	else 
	{ 
		result.push_back( source.substr( fp + separator_length, nextp - fp - separator_length ) );
	}
   	fp = nextp; 
   } 

   return result;
}

class lex { 
	std::string body;
	size_t active;
public:
	lex( std::string _body ) : body( _body ), active(0) { } 
	bool is_max()
	{ 
		return (active == body.length() - 1);
	}
	char get_value() 
	{ 
		return body[ active ];
	} 
	char set_min() 
	{ 
		active = 0;
		return body[ active ];
	}
	char get_next()
	{ 
		if( is_max() )
		{ 
			active = 0;
		} 
		return body[++active];
	}
	std::string get_body () 
	{ 
		return body; 
	}  
	bool is_have( const char c ) const { 
		return ( body.find( c ) != std::string::npos );
	} 
};

enum astate { VARIANT, CONSTANT, UNDEF };
const char *n[] = { "VARIANT", "CONSTANT", "UNDEF" }; 
void fill_lex_by_string( std::string &source, std::vector< lex > &vlex ) 
{
	std::string tmpstring;
	astate state = UNDEF;
	astate old_state;

 	std::string result_string;
	for( std::string::iterator it = source.begin(); it != source.end(); ++it ) 
	{
		switch( state ) 
		{ 
			case UNDEF :  
			{
				if( isalpha( *it ) ) 
				{ 
					state = CONSTANT;
				} 
				else if( *it == '(' )
				{
					state = VARIANT;
					continue;
				} 
			} break;

			case CONSTANT : 
			{ 
				if( isalpha( *it ) )
				{ 
					state = CONSTANT;
				} 
				else if( *it == '(' )
				{ 
					state = VARIANT;
					continue;
				} 
			} break;
		
			case VARIANT : 
			{ 
				if( isalpha( *it ) ) 
				{ 
					state = VARIANT;
				}
				else  if( *it == ')' ) 
				{ 
					state = UNDEF;
				} 
			} break;
	
			default : 
			{ 
				std::cout << "undefined state" << std::endl;
				exit( 1 );
			} 	
		} 
		if( state == CONSTANT ) 
		{ 
				result_string.push_back( *it );
				vlex.push_back( lex( result_string ) );	
				result_string.clear();
		} 
		else if( state == VARIANT ) 
		{ 
				result_string.push_back( *it );
		} 
		else if( state == UNDEF && old_state == VARIANT  )
		{ 
			vlex.push_back( lex( result_string ) );
			result_string.clear();
		} 

		old_state = state;
	}
/*	for( std::vector< lex > :: iterator it = vlex.begin() ; it != vlex.end(); ++it ) 
	{ 
		std::cout << it->get_body()  << " ";
	} 
	std::cout << std::endl;
*/
}


bool get_next_permutation( std::vector< lex > &vlex ) 
{ 
	for( std::vector< lex > :: reverse_iterator it = vlex.rbegin(); it != vlex.rend(); ++it ) 
 	{ 
		if( ! it->is_max() )
		{ 
			it->get_next();
			return true; 
		} 
		else 
		{ 
			it->set_min();
		} 
	}

	return false;
}
 
std::string get_string_by_vlex( std::vector< lex > &vlex )
{ 
	std::stringstream instring;
	for( std::vector< lex >::iterator it = vlex.begin(); it != vlex.end(); ++it ) 
	{ 
		instring << it->get_value();
	}
	return instring.str();
}
 

int main( int argc, char **argv ) { 

 std::string _infile( infile );

 if( argc > 1 && std::string( argv[1] ) != "" )
 { 
	_infile = std::string( argv[1] );
 } 

 std::ifstream in( _infile.c_str() );
 if( !infile ) 
 {
	 
	std::cout << " can't open file " << _infile << std::endl;
	exit( 1 ); 
 }

 std::vector< std::string > head_values = get_words( get_head( in ) );
 size_t l_length = to_int( head_values[0] );   
 size_t l_alphabet = to_int( head_values[1] );   
 size_t l_words = to_int( head_values[2] );   
 
 std::set< std::string > alphabet;

 std::string tmp_string;
 while( l_alphabet--  )
 {
	std::getline( in, tmp_string );
	alphabet.insert( tmp_string ); 
 }
 
 std::vector< std::string > words;
 while( l_words-- )
 { 
	std::getline( in, tmp_string );
	words.push_back( tmp_string );
 }
  
 std::ofstream outfile( "outfile.out" );

 size_t index = 0;
 for( std::vector< std::string > :: iterator it = words.begin(); it != words.end(); ++it ) 
 { 
        ++index;
        std::vector< lex > lvariant;
        fill_lex_by_string( *it, lvariant ); 
	size_t count = 0;
   	if( lvariant.size() == l_length ) 
   	{ 

		for( std::set< std::string > :: iterator sit = alphabet.begin(); sit != alphabet.end(); ++sit ) 
		{ 
			size_t count_case = 0;
			for( size_t i = 0; i < l_length; ++i )
			{ 
				if( lvariant[i].is_have( (*sit)[i] ) )
				{ 
					++count_case;
				} 
			} 
			if( count_case == l_length )
			{
				++count;
			}

		}
   	}
	else 
	{ 
		std::cout << " ??? " << index << " size = " << lvariant.size()  << std::endl;
	}  	
	outfile << "Case #" << index << ": " << count << std::endl;
	//outfile << "Case #" << index << ": " << count << " (" << *it << ")" << std::endl;
 }
        
}
























 
