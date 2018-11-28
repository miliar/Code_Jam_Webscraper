// Google Code Jam 2012 - Qualification Round - Problem A. Speaking in Tongues

#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <string>
#include <tchar.h>
#include <vector>

std::map<char, char>
GetDecryptionKey()
{
	// The encrypted file contains all 26 letters of the alphabet
	// The plaintext file contains the decrypted versions of these characters
	char* inputFileName = "encrypted.txt";
	char* outputFileName = "plaintext.txt";

	std::ifstream encryptedFile( inputFileName );
	std::ifstream plainTextFile( outputFileName );

	std::vector< std::string > encryptedLines;
	std::vector< std::string > plainTextLines;

	std::string line;
	while ( std::getline(encryptedFile, line) )	encryptedLines.push_back( line );
	while ( std::getline(plainTextFile, line) )	plainTextLines.push_back( line );

	// Build a mapping between these two character sets
	std::map< char, char > decryptionKey;

	// z becomes q (the only letters not in the encrypted/plaintext files, respectively)
	decryptionKey.insert( std::pair<char, char>( 'z', 'q' ) );

	// For each line (both files have the same number of lines/chars)
	for ( int l = 0; l < encryptedLines.size(); ++l )
	{
		std::string encryptedLine = encryptedLines[l];
		std::string plainTextLine = plainTextLines[l];

		// For each character in said line
		for ( int c = 0; c < encryptedLine.size(); ++c )
		{
			// Ignore characters we've already decrypted, but add all new ones
			if ( decryptionKey.find( encryptedLine[c] ) == decryptionKey.end() )
			{
				decryptionKey.insert( std::pair<char, char>( encryptedLine[c], plainTextLine[c] ) );
			}
		}
	}

	return decryptionKey;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char* inputFileName  = "A-small-attempt1.in";
	char* outputFileName = "output.txt";

	std::ifstream infile( inputFileName );
	std::ofstream outFile( outputFileName );
	std::string inLine;

	std::map<char, char> decryptionKey = GetDecryptionKey();

	// Read through every line in the file
	int i = 1;
	while ( std::getline(infile, inLine) )
	{
		// Ignore blank lines (and the first line)
		if ( !inLine.empty() && !isdigit(inLine[0]) )
		{
			// Write to the output file
			outFile	<< "Case #" << i << ": ";

			for (auto iter = inLine.begin(); iter != inLine.end(); ++iter )
			{
				outFile	<< decryptionKey.at( *iter );
			}

			outFile << "\n";
			++i;
		}
	}

	std::cout << "Plaintext written out to " << outputFileName << "\n";
	outFile.close();

	return 1;
}