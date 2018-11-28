// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <vector>
#include <iostream>

using std::cin;
using std::cout;

#include <string.h>

struct Game
{
	Game()
	{
		memset(CombineElements, 0, sizeof(CombineElements));
		memset(OpposingElements, 0, sizeof(OpposingElements));
	}

	void AddCombining( char a, char b, char c )
	{
		CombineElements[(unsigned)a][(unsigned)b] = c;
		CombineElements[(unsigned)b][(unsigned)a] = c;
	}
	void AddOpposing( char a, char b )
	{
		OpposingElements[(unsigned)a][(unsigned)b] = true;
		OpposingElements[(unsigned)b][(unsigned)a] = true;
	}

	bool ReduceStack()
	{
		if( ElementStack.size() >= 2 )
		{
			char a = ElementStack[ElementStack.size()-2];
			char b = ElementStack[ElementStack.size()-1];
			char c = CombineElements[(unsigned)a][(unsigned)b];
			if( c != 0 )
			{
				ElementStack.pop_back();
				ElementStack.pop_back();
				ElementStack.push_back( c );
				return true;
			}
		}


		for( size_t i = 0; i < ElementStack.size(); ++i )
		{
			char a = ElementStack[i];
			for( size_t j = i+1; j < ElementStack.size(); ++j )
			{
				char b = ElementStack[j];
				if( OpposingElements[(unsigned)a][(unsigned)b] )
				{
					ElementStack.clear();
					return true;
				}
			}
		}
		return false;
	}

	void Apply( char e )
	{
		ElementStack.push_back( e );

		while( ReduceStack() )
			;
	}

	char CombineElements[256][256];
	bool OpposingElements[256][256];

	std::vector<char>		ElementStack;

};

std::vector<char> Process()
{
	Game game;
	int num_elements;
	std::cin >> num_elements;
	for( int i = 0; i < num_elements; ++i )
	{
		std::string element;
		std::cin >> element;
		game.AddCombining( element[0], element[1], element[2] );
	}

	std::cin >> num_elements;
	for( int i = 0; i < num_elements; ++i )
	{
		std::string element;
		std::cin >> element;
		game.AddOpposing( element[0], element[1] );
	}

	std::cin >> num_elements;
	std::string elements;
	std::cin >> elements;

	for( int i = 0; i < num_elements; ++i )
	{
		game.Apply( elements[i] );
	}

	std::vector<char>	result;
	result.swap( game.ElementStack );
	return result;
}

int main(int argc, char* argv[])
{
	int num_tests;
	cin >> num_tests;
	
	for( int i = 0; i < num_tests; ++ i )
	{
		std::vector<char> res = Process();
		printf( "Case #%d: [", i+1 );
		for( size_t i = 0; i < res.size(); ++i )
		{
			if( i > 0 ) printf( ", " );
			printf( "%c", res[i] );
		}
		printf( "]\n" );
	}

	return 0;
}

