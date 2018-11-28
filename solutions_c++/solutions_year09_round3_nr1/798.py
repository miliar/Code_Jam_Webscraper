#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>

int
main ( )
{
	int T ;
	std::cin >> T ;
	int t = 1 ;
	while ( t <= T )
	{
		std::string s ;
		std::cin >> s ;
		std::map < char, int > map ;
		map[s[0]] = 1 ;
		int j = 1 ;
		while ( s[j] == s[0] and j < s.size()) ++j ;
		map[s[j]] = 0 ;
		int next = 2;
		for ( size_t i = j+1 ; i < s.size() ; ++i )
		{
			if ( map.find(s[i]) == map.end() )
			{
				map[s[i]] = next++ ;
			}
		}
		int64_t time = 0;
		for ( int i = 0; i < s.size() ; ++i )
		{
			time = time*next+ map[s[i]] ;
		}
		std::cout << "Case #" << t++ << ": " << time << std::endl ;
	}
}
