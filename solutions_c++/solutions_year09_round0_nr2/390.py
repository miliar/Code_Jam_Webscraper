//============================================================================
// Name        : WaterSheds.cpp
// Author      : Chaking
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//const char *inputFileName = "input.txt";
const char *inputFileName = "B-large.in";
const char *outputFileName = "output.txt";
const int MAX_OF_HEIGHT = 100;
const int MAX_OF_WIDTH = 100;
const int MAX_OF_BASINS = 26;
const int MAX_OF_ALTITUDES = 10000;

struct Position{
	int x;
	int y;
	char name;
};

typedef enum Direction { North, West, East, South, Center };
int direction[4][2] = { -1, 0, 0, -1, 0, 1, 1, 0 };

void process( int altitudes[][MAX_OF_WIDTH], const int height, const int width );
Direction getDirection( const int value );
void fillAnswer( Direction directions[MAX_OF_HEIGHT][MAX_OF_WIDTH], char answer[MAX_OF_HEIGHT][MAX_OF_WIDTH], Position basin, const int height, const int width );
bool isFlowToMe( const int next, Direction direction );
void findAnswer( const char name, const int x, const int y, char answer[MAX_OF_HEIGHT][MAX_OF_WIDTH], const int height, const int width );

ofstream fout;

int main() {
	int i, j, k;
	int countOfTestCases;
	int height, width;
	int altitudes[MAX_OF_HEIGHT][MAX_OF_WIDTH];
	ifstream fin( inputFileName );
	fout.open( outputFileName );

	fin >> countOfTestCases;

	for( i = 0; i < countOfTestCases; i++ ){
		fin >> height >> width;

		// input
		for( j = 0; j < height; j++ )
			for( k = 0; k < width; k++ )
				fin >> altitudes[j][k];

		fout << "Case #" << i + 1 << ":" << endl;
		process( altitudes, height, width );
	}

	fout.close();
	fin.close();

	return 0;
}

void process( int altitudes[][MAX_OF_WIDTH], const int height, const int width ){
	int i, j, k;
	Direction directions[MAX_OF_HEIGHT][MAX_OF_WIDTH];
	Position target;
	int min;
	Direction directionOfNow;
	Position basins[MAX_OF_BASINS];
	int countOfBasins = 0;
	char name = 'A';
	char answer[MAX_OF_HEIGHT][MAX_OF_WIDTH];

	memset( ( void * )&answer, 0, sizeof( char ) * MAX_OF_HEIGHT * MAX_OF_WIDTH );

	for( i = 0; i < height; i++ ){
		for( j = 0; j < width; j++ ){
			min = altitudes[i][j];
			directionOfNow = Center;

			for( k = 0; k < 4; k++ ){
				target.x = i + direction[k][0];
				target.y = j + direction[k][1];

				if( target.x < 0 || target.y < 0 || target.x >= height || target.y >= width )
					continue;
				else{
					if( min > altitudes[target.x][target.y] ){
						min = altitudes[target.x][target.y];
						directionOfNow = getDirection( k );
					}
				}
			}

			directions[i][j] = directionOfNow;
			if( directionOfNow == Center ){
				basins[countOfBasins].x = i;
				basins[countOfBasins].y = j;
				basins[countOfBasins++].name = name++;
			}
		}
	}

	for( i = 0; i < countOfBasins; i++ ){
		fillAnswer( directions, answer, basins[i], height, width );
	}

	name = 'a';
	for( i = 0; i < height; i++ ){
		for( j = 0; j < width; j++ ){
			if( isupper( answer[i][j] ) ){
				findAnswer( name, i, j, answer, height, width );
				name++;
			}
		}
	}

	for( i = 0; i < height; i++ ){
		for( j = 0; j < width; j++ ){
			fout << answer[i][j] << ' ';
		}

		fout << endl;
	}
}

void findAnswer( const char name, const int x, const int y, char answer[MAX_OF_HEIGHT][MAX_OF_WIDTH], const int height, const int width ){
	int i;
	Position target;
	char before = answer[x][y];
	answer[x][y] = name;

	for( i = 0; i < 4; i++ ){
		target.x = x + direction[i][0];
		target.y = y + direction[i][1];
		target.name = name;

		if( target.x < 0 || target.y < 0 || target.x >= height || target.y >= width )
			continue;
		else{
			if( answer[target.x][target.y] == before )
				findAnswer( name, target.x, target.y, answer, height, width );
		}
	}

	
}

void fillAnswer( Direction directions[MAX_OF_HEIGHT][MAX_OF_WIDTH], char answer[MAX_OF_HEIGHT][MAX_OF_WIDTH], Position basin, const int height, const int width ){
	int i;
	Position target;
	answer[basin.x][basin.y] = basin.name;

	for( i = 0; i < 4; i++ ){
		target.x = basin.x + direction[i][0];
		target.y = basin.y + direction[i][1];
		target.name = basin.name;

		if( target.x < 0 || target.y < 0 || target.x >= height || target.y >= width )
			continue;
		else{
			if( answer[target.x][target.y] != 0 )
				continue;
			else{
				if( isFlowToMe( i, directions[target.x][target.y] ) ){
					fillAnswer( directions, answer, target, height, width );
				}
			}
		}
	}
}

bool isFlowToMe( const int next, Direction direction ){
	if( next == 0 && direction == South ) return true;
	else if( next == 1 && direction == East ) return true;
	else if( next == 2 && direction == West ) return true;
	else if( next == 3 && direction == North ) return true;
	else return false;
}

Direction getDirection( const int value ){
	if ( value == 0 ) return North;
	if ( value == 1 ) return West;
	if ( value == 2 ) return East;
	if ( value == 3 ) return South;

	fout << "Impossible!!!!!" << endl;
	return North;

}