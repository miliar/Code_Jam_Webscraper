//============================================================================
// Name        : WelcomeToCodeJam.cpp
// Author      : Chaking
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const char *inputFileName = "input.txt";
//const char *inputFileName = "C-large.in";
const char *outputFileName = "output.txt";
const int MAX_OF_LINE = 501;
const char *phrase = "welcome to code jam";
const int LENGTH_OF_PHRASE = strlen( phrase );

void clearLine( char *line );
int process( char *line );

int main() {
	int i;
	int countOfTestCases;
	char line[MAX_OF_LINE];
	ifstream fin( inputFileName );
	ofstream fout( outputFileName );

	fin >> countOfTestCases;
	fin.getline( line, '\n' );

	for( i = 0; i < countOfTestCases; i++ ){
		fin.getline( line, MAX_OF_LINE, '\n' );
		clearLine( line );

		fout << "Case #" << i + 1 << ": ";
		fout.fill('0');
		fout.width(4);
		fout << process( line ) << endl;
	}

	fout.close();
	fin.close();

	return 0;
}

int process( char *line ){
	int i, j, k;
	int sum;
	const int length = strlen( line );
	int count[501][20];

	memset( ( void * )&count, 0, sizeof( int ) * 501 * 20 );

	for( i = 0; i < length; i++ ){
		for( j = 0; j < LENGTH_OF_PHRASE; j++ ){
			if( line[i] == phrase[j] ){
				if( j == 0 ) count[i][j]++;
				else{
					sum = 0;

					for( k = 0; k < length; k++ )
						sum += count[k][j-1];

					count[i][j] = sum + count[i][j];
					if( count[i][j] > 10000 ) count[i][j] %= 10000;
				}
			}
		}
	}

	sum = 0;
	for( i = 0; i < length; i++ ){
		sum += count[i][LENGTH_OF_PHRASE-1];
		if( sum > 10000 ) sum %= 10000;
	}

	return sum;
}

void clearLine( char *line ){
	int i, j;
	bool flag;
	int shift = 0;
	char *characters = "welcome tdja";
	const int sizeOfCharacters = strlen( characters );
	const int sizeOfLine = strlen( line );

	for( i = 0; i < sizeOfLine; i++ ){
		if( shift )	line[i - shift] = line[i];
		flag = false;
		for( j = 0; j < sizeOfCharacters; j++ ){
			if( line[i] == characters[j] ){
				flag = true;
				break;
			}
		}

		if( flag == false ){
			shift++;
		}
	}

	line[sizeOfLine - shift] = '\0';
}
