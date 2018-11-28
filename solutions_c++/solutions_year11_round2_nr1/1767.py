#ifndef _WIN32_WINNT            // Specifies that the minimum required platform is Windows Vista.
#define _WIN32_WINNT 0x0600     // Change this to the appropriate value to target other versions of Windows.
#endif

#include <stdio.h>
#include <tchar.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <assert.h>
#include <algorithm>
#include <iomanip>

enum EResult
{
	LOST,
	WIN,
	NA
};

EResult ctor( const char ch )
{
	switch(ch)
	{
	case '0':
		return LOST;
	case '1':
		return WIN;
	case '.':
	default:
		return NA;
	}
}

typedef std::vector< EResult > TMatches;
typedef std::vector< TMatches > TTMatches;


double wp( 
	const TTMatches& allMatches, 
	const size_t nr,
	const size_t exclude )
{
	double retVal = 0.0;
	const TMatches& matches = allMatches[nr];
	double dv = 0.0;
	for( size_t i = 0; i < matches.size(); ++i )
	{
		if( i != exclude )
		{
			switch( matches[i] )
			{
			case LOST:
				dv+=1.0;
				break;
			case WIN:
				dv+=1.0;
				retVal += 1.0;
				break;
			}
		}
	}
	return retVal / dv;
}

double owp( const TTMatches& allMatches, const size_t nr )
{
	double retVal = 0.0;
	const TMatches& matches = allMatches[nr];
	double dv = 0.0;
	for( size_t i = 0; i < matches.size(); ++i )
	{
		switch( matches[i] )
		{
		case LOST:
		case WIN:
			dv+=1.0;
			retVal += wp( allMatches, i , nr );
			break;
		}
	}
	return retVal / dv;
}

double oowp( const TTMatches& allMatches, const size_t nr )
{
	double retVal = 0.0;
	const TMatches& matches = allMatches[nr];
	double dv = 0.0;
	for( size_t i = 0; i < matches.size(); ++i )
	{
		switch( matches[i] )
		{
		case LOST:
		case WIN:
			dv+=1.0;
			retVal += owp( allMatches, i );
			break;
		}
	}
	return retVal / dv;
}

double rpi( const TTMatches& allMatches, const size_t nr )
{
	return 0.25 * wp( allMatches, nr, -1 ) + 
		0.5 * owp( allMatches, nr ) + 
		0.25 * oowp( allMatches, nr );
}

int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;
	if( argc != 3 )
	{
		cerr << "Invalid amount of arguments!";
		return 1;
	}

	ifstream input_file( argv[1] );
	if( !input_file.is_open() )
	{
		cerr << "Cannot open input file!";
		return 2;
	}

	ofstream output_file( argv[2] );
	if( !output_file.is_open() )
	{
		cerr << "Cannot open output file!";
		return 3;
	}

	string sLine;
	getline( input_file, sLine );
	int iLines = atoi( sLine.c_str() );
	for( int i = 0; i < iLines; ++i )
	{
		output_file << "Case #"<< i + 1 <<":\n";
		getline( input_file, sLine );
		int iTeams = atoi( sLine.c_str() );

		TTMatches allMatches;
		allMatches.reserve( iTeams );

		for( int j = 0; j < iTeams; ++j )
		{
			TMatches matches;
			matches.reserve( iTeams );
			getline( input_file, sLine );
			for( std::string::const_iterator it = sLine.begin(); 
				it != sLine.end(); ++it )
				matches.push_back( ctor( *it ) );
			allMatches.push_back( matches );
		}
		
		for( int j = 0; j < iTeams; ++j )
		{
			output_file << setprecision(12) << fixed << rpi( allMatches, j ) << endl;
		}
	}
	return 0;
}
