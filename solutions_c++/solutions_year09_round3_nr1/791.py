// Qual 3.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>


int main(int argc, char * argv[])
{
	std::ostream * pOut;
	std::ofstream outFile;
	std::ifstream inFile;

	switch( argc ) {
		case 2:
		{
			pOut = &std::cout;
			break;
		}

		case 3:
		{
			outFile.open( argv[2] );
			pOut = &outFile;
			break;
		}

		default:
		{
			std::cout << "Usage: qual3 INPUT_FILE [OUTPUT_FILE]" << std::endl;
			
			return 0;
		}
	}

	inFile.open( argv[1] );

	if( !inFile.good() ) {
		std::cerr << "Failed to open input file" << std::endl;
		return -1;
	}
	if( !pOut->good() ) {
		std::cerr << "Failed to open output file" << std::endl;
		return -1;
	}
	
	//// Processing begins

	unsigned N, i, j;
	

	inFile >> N;

	std::clog << " N = " << N << std::endl;

	char buf[1024];
	char outBuf[64];

	inFile.getline( buf, 1024 );
	for( i = 0; i < N; i++ ) {
		int assign[256];
		int currAssign;
		long long value;
		inFile.getline( buf, 1024 );

		
//		std::clog << buf << "\n(" << strlen(buf) << ")" << std::endl;

		// Assign values to each digit
		memset( assign, -1, sizeof(assign) );
		assign[buf[0]] = 1;
		
		for( j = 1; buf[j] && (buf[j] == buf[0]); j++) {};

		currAssign = 2;
		if( buf[j] ) {
			assign[buf[j]] = 0;
			for( ++j; buf[j]; j++ ) {
				if( assign[buf[j]] == -1 ) assign[buf[j]] = currAssign++;
//				std::clog << buf[j] << " = " << assign[buf[j]] << std::endl;
			}
		}

		// Base = currAssign - calculate value
		value = 0;
		for( j = 0; buf[j]; j++ ) {
			value *= currAssign;
			value += assign[buf[j]];
		}

		sprintf( outBuf, "%llu", value );
		*pOut << "Case #" << i + 1 << ": " << outBuf << std::endl;
	}

	if(outFile.is_open()) outFile.close();
	inFile.close();
	return 0;
}

