#include <iostream>
#include <vector>
#include <fstream>
#include <exception>
#include <math.h>
#include <cstdlib>

class ColorPos
{
public:
	char color;
	int pos;
};

int Solve( std::vector< ColorPos >& colorPosList )
{
	int actualPos[2] = {1, 1};
	int nbSeconds = 0;
	int timeAvailableFor[2] = {0, 0};


	for( std::vector< ColorPos >::const_iterator it = colorPosList.begin(); it != colorPosList.end(); ++it )
	{
		if( it->color == 'O')
		{
			int t = abs( it->pos - actualPos[0]) + 1;
			int diff = std::min( t, timeAvailableFor[ 0 ] );

			t -= diff;
			if( t == 0 )
				t = 1;
			nbSeconds += t;
			actualPos[0] = it->pos;
			timeAvailableFor[ 0 ] = 0;
			timeAvailableFor[1] += t;
		}
		else if (it->color == 'B')
		{
			int t = abs( it->pos - actualPos[1]) + 1;
			int diff = std::min( t, timeAvailableFor[ 1 ] );

			t -= diff;
			if( t == 0 )
				t = 1;
			nbSeconds += t;
			actualPos[1] = it->pos;
			timeAvailableFor[ 1 ] = 0;
			timeAvailableFor[0] += t;
		}
		else
			throw std::exception();
	}

	return nbSeconds;
}

int main( int argc, char** argv )
{
	std::ifstream ifs( "A-large.in" );
	std::ofstream output( "ouput.txt");

	int nbTest = 0;
	int n = 0;

	ifs >> nbTest;

	for( int i = 1; i <= nbTest; ++i )
	{
		ifs >> n;

		std::vector< ColorPos > colorPosList;
		for( int j = 0; j < n; ++j )
		{
			ColorPos colorPos;
			ifs >> colorPos.color;
			ifs >> colorPos.pos;
			colorPosList.push_back( colorPos );
		}
		int nbSecond = Solve( colorPosList );
		output << "Case #" << i << ": " << nbSecond << std::endl;
	}
	std::cout << "Finish" << std::endl;
 	return 0;
}
