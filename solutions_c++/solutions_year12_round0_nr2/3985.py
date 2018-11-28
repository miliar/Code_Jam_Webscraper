#include <iostream>
#include <fstream>

using namespace std;

void process( const int caseNumber, ifstream &inputStream );
void print( const int caseNumber, long long int answer );

//const char* nameOfInput = "input.txt";
const char* nameOfInput = "B-large.in";

#define MAX ( 101 )

int main ( void ){
	int i;
	int n;
	ifstream inputStream( nameOfInput );

	inputStream >> n;

	for( i = 0; i < n; i++ ){
		process( i, inputStream );
	}
	
	return 0;
}

int compare( const void *a, const void *b ){
	return ( *( int * )a - *( int * )b );
}

void process( const int caseNumber, ifstream &inputStream  ){
	int numberOfGooglers, numberOfSurprising, numberOfMax;
	int i;
	int point[MAX];
	int max[MAX][2]; // 0 is without surprising, 1 is with surprising;
	int result, rest;
	int count = 0;

	inputStream >> numberOfGooglers >> numberOfSurprising >> numberOfMax;

	for( i = 0; i < numberOfGooglers; i++ ) inputStream >> point[i];

	qsort( point, numberOfGooglers, sizeof( int ), compare );

	for( i = 0; i < numberOfGooglers; i++ ){
		result = point[i] / 3;
		rest = point[i] % 3;

		if( point[i] == 0 ){
			max[i][0] = 0;
			max[i][1] = -1;
		}
		else if( point[i] == 1 ){
			max[i][0] = 1;
			max[i][1] = -1;
		}
		else{
			if( rest == 0 ){
				max[i][0] = result;
				max[i][1] = result + 1;
			}
			else if( rest == 1 ){
				max[i][0] = result + 1;
				max[i][1] = result + 1;
			}
			else if( rest == 2 ){
				max[i][0] = result + 1;
				max[i][1] = result + 2;
			}
		}
	}

	for( i = 0; i < numberOfGooglers; i++ ){
		if( numberOfSurprising ){
			if( max[i][0] >= numberOfMax ){
				count++;
			}
			else if( max[i][1] >= numberOfMax ){
				count++;
				numberOfSurprising--;
			}
		}
		else{
			if( max[i][0] >= numberOfMax ) count++;
		}
	}

	cout << "Case #" << caseNumber + 1 << ": ";
	cout << count;
	cout << endl;
}