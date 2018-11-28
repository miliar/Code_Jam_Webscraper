// SavingTheUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <set>
#include <string>


int getNumEngineSwitches( std::ifstream& in )
{
	const int MAX_ENGINE_NAME_SIZE = 100;
	int numEngines;
	in >> numEngines;
	
	char curStr[ MAX_ENGINE_NAME_SIZE ];
	std::set<std::string> enginesArray;
	in.getline( curStr, MAX_ENGINE_NAME_SIZE );
	
	for( int i = 0; i < numEngines; ++i )
	{		
		in.getline( curStr, MAX_ENGINE_NAME_SIZE );
		enginesArray.insert( curStr );		
	}	

	int numQ;
	in >> numQ;
	in.getline( curStr, MAX_ENGINE_NAME_SIZE );

	int numSwithes = 0;	
	std::set<std::string> usedEngines;	
	usedEngines.insert( enginesArray.begin( ), enginesArray.end( ) );
	std::set<std::string>::iterator enginesIter;

	for( int i = 0; i < numQ; ++i )
	{
		in.getline( curStr, MAX_ENGINE_NAME_SIZE );
		std::string curQuery( curStr );			
		enginesIter = usedEngines.find( curQuery );
		if( enginesIter != usedEngines.end( ) )
		{
			usedEngines.erase( enginesIter );
			if( usedEngines.empty( ) )
			{
				usedEngines.insert( enginesArray.begin( ), enginesArray.end( ) );
				usedEngines.erase( curQuery );
				++numSwithes;
			}
		}
	}

	return numSwithes;
}


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-large.in" );

	int numCases;
	in >> numCases;

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );		
	for( int i = 0; i < numCases; ++i )
	{
		out << "Case #" << i + 1 << ": " << getNumEngineSwitches( in ) << std::endl;
	}

	out.close( );
	
	return 0;
}

