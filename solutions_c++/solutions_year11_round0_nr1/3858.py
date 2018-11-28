#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

void calculate( ifstream& input, ofstream& output )
{
	unsigned items = 0;
	input >> items;
	unsigned posO = 1, posB = 1;
	unsigned timeO = 0, timeB = 0;
	unsigned currentPos;
	char currentButtom;

	for (unsigned i = 0; i < items; ++i)
	{ 
		input >> currentButtom;
		input >> currentPos;

		if ( currentButtom == 'O'  )
		{
			timeO += abs( currentPos - posO ) + 1;
			if ( timeO <= timeB ) timeO = timeB + 1; 
			posO = currentPos;
		}
		else
		{
			timeB += abs( currentPos - posB ) + 1;
			if ( timeB <= timeO ) timeB = timeO + 1; 
			posB = currentPos;
		}
	}

	output << max(timeO, timeB) << endl;
}

int main( int argc, char *argv[] )
{

	if ( argc != 3 )
	{
		cerr << "Usage: Calculate <Input_File_Name> <Output_File_Name>";
		return EXIT_FAILURE;
	}
	else
	{
		string inputFile( argv[1] ), outputFile ( argv[2] );
		cout << "Get input from: " << inputFile << endl;
		cout << "Output file is: " << outputFile << endl;
		
		ifstream input( inputFile.c_str() );
		unsigned cases;
		input >> cases;
		cout << "We have got " << cases << " cases to cover" << endl;

		ofstream output( outputFile.c_str() );

		for ( unsigned i = 1; i <= cases; ++i )
		{
			output << "Case #" << i << ": "; 
			calculate( input, output );
		}

	}
	return EXIT_SUCCESS;
}
