#include <iostream>
#include <string>
#include <map>

int main()
{
  std::map< char, char > replace;

  replace[ 'a' ] = 'y';
  replace[ 'b' ] = 'h';
  replace[ 'c' ] = 'e';
  replace[ 'd' ] = 's';
  replace[ 'e' ] = 'o';
  replace[ 'f' ] = 'c';
  replace[ 'g' ] = 'v';
  replace[ 'h' ] = 'x';
  replace[ 'i' ] = 'd';
  replace[ 'j' ] = 'u';
  replace[ 'k' ] = 'i';
  replace[ 'l' ] = 'g';
  replace[ 'm' ] = 'l';
  replace[ 'n' ] = 'b';
  replace[ 'o' ] = 'k';
  replace[ 'p' ] = 'r';
  replace[ 'q' ] = 'z';
  replace[ 'r' ] = 't';
  replace[ 's' ] = 'n';
  replace[ 't' ] = 'w';
  replace[ 'u' ] = 'j';
  replace[ 'v' ] = 'p';
  replace[ 'w' ] = 'f';
  replace[ 'x' ] = 'm';
  replace[ 'y' ] = 'a';
  replace[ 'z' ] = 'q';
  replace[ ' ' ] = ' ';

  int count( 0 );
  std::cin >> count;
  std::string s;
  getline( std::cin, s );
  std::map< int, std::string > output;
  for( int i( 0 ) ; i < count ; ++i )
  {
    getline( std::cin, s );
    std::string out;
    for( int c( 0 ) ; c < s.length() ; ++c )
    {
      out.append( &replace[ s[ c ] ] );
    }
    output[ i ] = out;
  }
  for( int i( 0 ) ; i < count ; ++i )
  {
    std::cout << "Case #" << i + 1 << ": " << output[ i ] << std::endl;
  }

  return 0;
}
