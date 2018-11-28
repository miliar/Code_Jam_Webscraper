#include <iostream>
#include <fstream>
#include <list>

int main()
{
	std::ifstream fin( "C:/Users/0xc0deface/Desktop/A-large.in" );
	std::ofstream fout( "C:/Users/0xc0deface/Desktop/test.out" );

	int testCases;
	fin >> testCases;

	std::list< char > order;
	std::list< int > O,B;

	for ( int i = 0; i < testCases; ++i )
	{

		int numButtons;
		fin >> numButtons;

		for ( int i = 0; i < numButtons; ++i )
		{
			char robot;
			int button;
			fin >> robot >> button;

			order.push_back( robot );

			if ( robot == 'O' )
				O.push_back( button );
			else
				B.push_back( button );
		}

		int oPos = 1, bPos = 1;

		int steps = 0;

		for( ; ; )
		{
			char orderVal = order.front();

			if ( orderVal == 'O' && oPos == O.front() )
			{
				order.pop_front();
				O.pop_front();
			}
			else
			{
				if( !O.empty() )
				{
					if ( oPos < O.front() )
						++oPos;
					else if ( oPos > O.front() )
						--oPos;
				}
			}

			if ( orderVal == 'B' && bPos == B.front() )
			{
				order.pop_front();
				B.pop_front();
			}
			else
			{
				if( !B.empty() )
				{
					if ( bPos < B.front() )
						++bPos;
					else if ( bPos > B.front() )
						--bPos;
				}
			}
			
			++steps;

			if ( order.empty() )
				break;
		}

		fout << "Case #" << i+1 << ": " << steps << std::endl;
	}
	return 0;
}
