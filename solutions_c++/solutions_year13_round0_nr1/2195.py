#include <Windows.h>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

std::string ReadString;
std::ofstream OutputFile;
std::ifstream InputFile;
std::stringstream StringStream;

int main() {
	//Opens the file and creates an input file
	OutputFile = std::ofstream("outputLarge.out");

	while( !InputFile.is_open() ) {
		std::cout << "Enter input File Name:\n";
		std::string fileName;
		std::cin >> fileName;
		InputFile = std::ifstream( fileName );
	};

	getline( InputFile, ReadString );

	StringStream = std::stringstream( ReadString );
	int numOfCases;
	StringStream >> numOfCases;
	std::cout << numOfCases << "\n";

	// Loop for all the cases
	char boardState[16];
	for( int i = 0; i < numOfCases; i++ ) {
		InputFile.read( &boardState[0], 4 );
		InputFile.get();
		InputFile.read( &boardState[4], 4 );
		InputFile.get();
		InputFile.read( &boardState[8], 4 );
		InputFile.get();
		InputFile.read( &boardState[12], 4 );
		InputFile.get();
		
		InputFile.get(); // Additional Offset

		// Check for lines
		bool XWon = false;
		bool OWon = false;

		//Check horizontal lines
		for( int j = 0; j < 4; j++ ) {
			if(
				( boardState[j*4+0] == 'O' || boardState[j*4+0] == 'T' ) &&
				( boardState[j*4+1] == 'O' || boardState[j*4+1] == 'T' ) &&
				( boardState[j*4+2] == 'O' || boardState[j*4+2] == 'T' ) &&
				( boardState[j*4+3] == 'O' || boardState[j*4+3] == 'T' ) ) {
					OWon = true;
			}
			else if(
				( boardState[j*4+0] == 'X' || boardState[j*4+0] == 'T' ) &&
				( boardState[j*4+1] == 'X' || boardState[j*4+1] == 'T' ) &&
				( boardState[j*4+2] == 'X' || boardState[j*4+2] == 'T' ) &&
				( boardState[j*4+3] == 'X' || boardState[j*4+3] == 'T' ) ) {
					XWon = true;
			}
		}

		//Check vertical lines
		for( int j = 0; j < 4; j++ ) {
			if(
				( boardState[0*4+j] == 'O' || boardState[0*4+j] == 'T' ) &&
				( boardState[1*4+j] == 'O' || boardState[1*4+j] == 'T' ) &&
				( boardState[2*4+j] == 'O' || boardState[2*4+j] == 'T' ) &&
				( boardState[3*4+j] == 'O' || boardState[3*4+j] == 'T' ) ) {
					OWon = true;
			}
			else if(
				( boardState[0*4+j] == 'X' || boardState[0*4+j] == 'T' ) &&
				( boardState[1*4+j] == 'X' || boardState[1*4+j] == 'T' ) &&
				( boardState[2*4+j] == 'X' || boardState[2*4+j] == 'T' ) &&
				( boardState[3*4+j] == 'X' || boardState[3*4+j] == 'T' ) ) {
					XWon = true;
			}
		}

		// Check Diagonals
		if(
			( boardState[0] == 'O' || boardState[0] == 'T' ) &&
			( boardState[5] == 'O' || boardState[5] == 'T' ) &&
			( boardState[10] == 'O' || boardState[10] == 'T' ) &&
			( boardState[15] == 'O' || boardState[15] == 'T' ) ) {
				OWon = true;
		}
		else if(
			( boardState[0] == 'X' || boardState[0] == 'T' ) &&
			( boardState[5] == 'X' || boardState[5] == 'T' ) &&
			( boardState[10] == 'X' || boardState[10] == 'T' ) &&
			( boardState[15] == 'X' || boardState[15] == 'T' ) ) {
				XWon = true;
		}

		else if(
			( boardState[3] == 'O' || boardState[3] == 'T' ) &&
			( boardState[6] == 'O' || boardState[6] == 'T' ) &&
			( boardState[9] == 'O' || boardState[9] == 'T' ) &&
			( boardState[12] == 'O' || boardState[12] == 'T' ) ) {
				OWon = true;
		}
		else if(
			( boardState[3] == 'X' || boardState[3] == 'T' ) &&
			( boardState[6] == 'X' || boardState[6] == 'T' ) &&
			( boardState[9] == 'X' || boardState[9] == 'T' ) &&
			( boardState[12] == 'X' || boardState[12] == 'T' ) ) {
				XWon = true;
		}

		/*	Case #1: X won
			Case #2: Draw
			Case #3: Game has not completed
			Case #4: O won
		*/
		OutputFile << "Case #" << i+1 << ": ";

		if( XWon ) {
			std::cout << "X WON" << "\n";
			OutputFile << "X won";
		} else if ( OWon ) {
			std::cout << "O WON" << "\n";
			OutputFile << "O won";
		} else {
			// Check if the game is over
			bool gameOver = true;
			for( int j = 0; j < 16; j++ ) {
				if( boardState[j] == '.') { gameOver = false; }
			}

			if( gameOver ) {
				std::cout << "Draw" << "\n";
				OutputFile << "Draw";
			} else {
				std::cout << "NO ONE WON" << "\n";
				OutputFile << "Game has not completed";
			}
		}
		
		if( i != numOfCases - 1 ) { OutputFile << "\n"; }
		XWon = false;
		OWon = false;
		//OutputFile.write( outPutMessage, outPutMessage.size() );
	}
	
	OutputFile.close();
	InputFile.close();

	while( true ) {}
	return 0;
}