#ifndef CONFIG_H
#define CONFIG_H

#include <iostream>
#include <fstream>
#include <cstdlib>

#define BUFFER_SIZE 1024

#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "ouput.txt"

using namespace std;

struct Cases
{
	Cases() : numTestCases( 0 ) {}
	~Cases()
	{
		if ( numTestCases && testCase )
		{
			for ( int i = 0; i < numTestCases; ++i )
			{
				if ( testCase[i] )
				{
					delete testCase[i];
				}
			}
		}
	}

	int numTestCases;
	char** testCase;
};

ifstream* openFileForInput( char* file )
{
	ifstream* ifs = new ifstream;

	ifs->open( file, ios_base::in );

	if ( !ifs->is_open() )
	{
		cout << "Failed to open " << file << endl;
		return NULL;
	}

	return ifs;
}

ofstream* openFileForOutput( char* file )
{
	ofstream* ofs = new ofstream;

	ofs->open( file, ios_base::out );

	if ( !ofs->is_open() )
	{
		cout << "Failed to open " << file << endl;
		return NULL;
	}

	return ofs;
}

Cases readFile( ifstream*& ifs )
{
	Cases* c = new Cases;

	char line[1024];

	ifs->getline( line, BUFFER_SIZE-1 );

	c->numTestCases = atoi( line );

	if ( c->numTestCases > 0 )
	{
		c->testCase = new char*[c->numTestCases];
		for ( int i = 0; i < c->numTestCases; ++i )
		{
			c->testCase[i] = new char[BUFFER_SIZE];
			ifs->getline( c->testCase[i], BUFFER_SIZE-1 );
		}
	}
	return *c;
}

void prepareTestCase( ofstream*& ofs, int caseNum )
{
	char tmp[12] = {0};
	_itoa_s( caseNum, tmp, 11, 10 );
	ofs->write( "Case #", 6 );
	ofs->write( tmp, strlen(tmp) );
	ofs->write( ": ", 2 );
}

void writeTestCase( ofstream*& ofs, int caseNum, char* caseData )
{
	char tmp[12] = {0};
	_itoa_s( caseNum, tmp, 11, 10 );
	ofs->write( "Case #", 6 );
	ofs->write( tmp, strlen(tmp) );
	ofs->write( ": ", 2 );
	ofs->write( caseData, strlen( caseData ) );
	ofs->put('\n');
}

void closeInputFile( ifstream*& ifs )
{
	if ( !ifs ) return;
	ifs->close();
	delete ifs;
	ifs = 0;
}
void closeOutputFile( ofstream*& ofs )
{
	if ( !ofs ) return;
	ofs->close();
	delete ofs;
	ofs = 0;
}

#endif
