//============================================================================
// Name        : TheNextNumber.cpp
// Author      : Chaking
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

void sort( char *data, const int size );
void swap( int &a, int &b );

//const char *nameOfInput = "input.txt";
const char *nameOfInput = "B-large.in";
const char *nameOfOutput = "output.txt";
const int MaxOfBase = 12;
const int MaxOfString = 1024;
const int MaxOfCount = 90000;

int main() {
	int countOfTestCases;
	int i;
	ifstream fin( nameOfInput );
	ofstream fout( nameOfOutput );

	char line[MaxOfString];
	int length;

	fin >> countOfTestCases;
	fin.getline( line, MaxOfString, '\n' );

	for( i = 0; i < countOfTestCases; i++ ){
		memset( line, 0, MaxOfString );
		//input
		{
			fin.getline( line, MaxOfString, '\n' );
			length = strlen( line );
		}

		cout << "Case #" << i + 1 << ": ";
		//process
		{
			int i, j;
			int position;
			int min;

			for( i = length - 2; i >= 0; i-- ){
				min = '0' + 10;

				for( j = i + 1; j < length; j++ ){
					if( line[i] < line[j] ){
						if( min > line[j] ){
							min = line[j];
							position = j;
						}
					}
				}

				if( min != '0' + 10 ) break;
			}

			if( i == -1 ){
				min = '0' + 10;
				for( j = 0; j < length; j++ ){
					if( min > line[j] && line[j] != '0' ){
						min = line[j];
						position = j;
					}
				}

				line[length++] = '0';
				line[length] = '\0';

				if( min != '0' ) {
					swap( line[0], line[position] );

					sort( &line[1], length - 1 );
				}
			}
			else{
				swap( line[i], line[position] );

				sort( &line[i + 1], length - i - 1 );
			}
			cout << line << endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}



void sort( char *data, const int size ){
	int i, j;

	for( i = 0; i < size - 1; i++ ){
		for( j = i + 1; j < size; j++ ){
			if( data[i] > data[j] ){
				swap( data[i], data[j] );
			}
		}
	}
}

void swap( int &a, int &b ){
	int temp;
	temp = a;
	a = b;
	b = temp;
}