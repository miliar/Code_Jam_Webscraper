// Qual 1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <fstream>

class DictNode {
	DictNode * succ[256];
	
public:
	DictNode() {
		memset(succ, 0, sizeof(*succ) * 256);
	}

	void addWord( const char *word )
	{
		if( *word ) {
			DictNode *pSucc = succ[*word];
			if( pSucc == NULL ) pSucc = succ[*word] = new DictNode();
			pSucc->addWord( word + 1 );
		}
	}

	unsigned countWords( std::vector<char> const * vOptions )
	{
		unsigned uOptions = 0;

		if( !(vOptions + 1)->empty() ) {
			for( std::vector<char>::const_iterator i = vOptions->begin(); i != vOptions->end(); i++ ) {
				DictNode *pSucc = succ[*i];
				if(pSucc) uOptions += pSucc->countWords( vOptions + 1 );
			}
		} else {
			for( std::vector<char>::const_iterator i = vOptions->begin(); i != vOptions->end(); i++ ) {
				uOptions += succ[*i] ? 1 : 0;
			}
		}
		return uOptions;
	}
};

DictNode gDict;

int main(int argc, char * argv[])
{
	const char *inPath = NULL;
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
			std::cout << "Usage: qual1 INPUT_FILE [OUTPUT_FILE]" << std::endl;
			
			return 0;
		}
	}

	if(!inPath) inPath = argv[1];
	inFile.open( inPath );

	if( !inFile.good() ) {
		std::cerr << "Failed to open input file" << std::endl;
		return -1;
	}
	if( !outFile.good() ) {
		std::cerr << "Failed to open output file" << std::endl;
		return -1;
	}
	
	//// Processing begins

	unsigned L, D, N, i, j;

	inFile >> L;
	inFile >> D;
	inFile >> N;

	std::clog << "L = " << L << ", D = " << D << ", N = " << N << std::endl;

	// Add words to dict
	char buf[1024];
	
	for( i = 0; i < D; i++ ) {
		inFile >> buf;
		//std::clog << buf << std::endl;

		gDict.addWord( buf );
	}


	// Process patterns
	std::vector<char> * vOptions = new std::vector<char> [L + 1];
	for( i = 0; i < N; i++ ) {
		const char *patt = buf;
		inFile >> buf;
		
		//std::clog << buf << " - ";

		for( j = 0; j < L; j++ ) {
			vOptions[j].clear();
			if( *patt == '(' ) {
				while( *++patt != ')' ) {
					vOptions[j].push_back(*patt);
				}
			} else {
				vOptions[j].push_back(*patt);
			}
			patt++;

			//std::clog << vOptions[j].size() << " ";
		}

		*pOut << "Case #" << i + 1 << ": " << gDict.countWords( vOptions ) << std::endl;
		//std::clog << std::endl;
	}
	delete [] vOptions;

	if(outFile.is_open()) outFile.close();
	inFile.close();
	return 0;
}

