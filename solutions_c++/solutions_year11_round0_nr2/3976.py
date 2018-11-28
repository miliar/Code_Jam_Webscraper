#include <exception>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <istream>
#include <libgen.h>
#include <stdlib.h>
#include <sys/types.h>
#include <string>
#include <algorithm>
#include <vector>

typedef struct{
	char a;
	char b;
	char transform;
} combo_st;

using namespace std;

void shorten( vector<char> &game, combo_st *combinations, uint num_combos)
{
	if( game.size() < 2 )
		return;
	for( uint i = 0; i < num_combos; ++i )
	{
		if( (game[game.size()-2] == combinations[i].a && game[game.size() - 1] == combinations[i].b) ||
		 (game[game.size()-2] == combinations[i].b && game[game.size() - 1] == combinations[i].a) )
		{
			game.resize( game.size() - 1 );
			game[game.size() - 1] = combinations[i].transform;
		} 
	}
}
void clear( vector<char> &game, combo_st *clearances, uint num_clears)
{
	if( game.size() < 2 )
		return;
	for( uint i = 0; i < num_clears; ++i )
	{
		for( uint j = 0; j < game.size(); ++j )
		{
			for( uint k = j + 1; k < game.size(); ++k )
			{
				if( (game[j] == clearances[i].a && game[k] == clearances[i].b) || 
				 (game[j] == clearances[i].b && game[k] == clearances[i].a) )
				{
					game.clear(); 
					return;
				}
			}
		}
	}
}
void minimize( vector<char> &game, combo_st *combinations, uint num_combos, combo_st *clearances, uint num_clears )
{
	if( game.size() < 2 )
		return;

	shorten(game, combinations, num_combos);
	clear(game, clearances, num_clears);
}

int main( int argc, char **argv )
{
	int err = 0;

	// quick quit if we don't expect this call line
	if( argc != 2 )
	{
		cerr << "Usage: " << basename(*argv) << " <filename>" << endl;
		return -1;
	}

	// quick quit if the file they give us isn't available
	ifstream in(argv[1]);
	if( !in )
	{
		cerr << "could not open " << argv[1] << endl;
		
	}

	uint T = 0, C = 0, D = 0, N = 0;
	char a, b, c;
	// run the tests
	try {
		in >> T;

		for( uint i = 0; i < T; ++i )
		{
			in >> C;
			combo_st *combos = (combo_st *)calloc( C, sizeof(combo_st) );
			
			for( uint j = 0; j < C; ++j )
			{
				in >> a >> b >> c;
				combos[j].a = a;
				combos[j].b = b;
				combos[j].transform = c;
			}

			in >> D;
			combo_st *clears = (combo_st *)calloc( D, sizeof(combo_st) );
			
			for( uint j = 0; j < D; ++j )
			{
				in >> a >> b;
				clears[j].a = a;
				clears[j].b = b;
			}

			in >> N;
			string input;
			in >> input;

			vector<char>elements;

			for( uint j = 0; j < N; ++j )
			{
				elements.push_back(input[j]);
				minimize(elements, combos, C, clears, D);
			}

		cout << "Case #" << i+1 << ": [";
		for( uint j = 0; j < elements.size(); ++j )
		{
			if( j != 0 )
				cout << ", ";
			cout << elements[j];
		}
		cout << "]"<<endl;
		}
	} catch( exception &e ) {
		cerr << "Exception!!\n" << e.what() << endl;
		err = -1;
	}

	return err;
}
