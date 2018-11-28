#include <list>
#include <cmath>
#include <vector>
#include <iostream>

int main()
{
	int cases;

	std::cin >> cases;


	for( int I = 0; I < cases; I++ )
	{
		int K, answers;
		std::cin >> K >> answers;
	
		std::list< int > answ;
		while( answers --> 0 )
		{
			int i;
			std::cin >> i;
			answ.push_back( i );
		}

		std::list< int > cards;

		cards.push_back( K );
		K--;
		while( K > 0 )
		{
			cards.push_front( K );
			int j = K-1;
			while( j --> 0 )
			{
				int t = *( cards.rbegin() );
				cards.pop_back();
				cards.push_front( t );
			}
			K--;
		}

		std::vector<int> vc;
		for( std::list<int>::iterator i = cards.begin(); i != cards.end(); i++ )
			vc.push_back( *i );
		
		std::cout << "Case #" << ( I + 1 ) << ": ";
		for( std::list<int>::iterator j = answ.begin(); j != answ.end(); j++ )
			std::cout << vc[ *j - 1 ] << ' ';
		std::cout << std::endl;
	}
	return 0;
}

