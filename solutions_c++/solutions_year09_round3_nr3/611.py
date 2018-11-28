//============================================================================
// Name        : main.cpp
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

void sort( int *data, const int size );
void swap( int &a, int &b );

//const char *nameOfInput = "input.txt";
const char *nameOfInput = "C-small-attempt2.in";
const char *nameOfOutput = "output.txt";
const long long MaxOfQ = 101;
const long long MaxOfString = 1024;
const long long MaxOfMin = 1000000;

bool check[MaxOfQ];
int Q, P;
int positions[MaxOfQ];
int minOfProgram;

int start( int position, int bribe, int count ){
	if( count == Q ) return bribe;
	if( bribe >= minOfProgram ) return bribe;

	check[position] = true;

	int i, j;
	int sum;
	int min = MaxOfMin;
	int result;

	for( i = 0; i < Q; i++ ){
		sum = 0;

		if( check[i] == false ){
			if( i != 0 ){
				for( j = i - 1; j >= 0; j-- ){
					if( check[j] ){
						sum += positions[i] - positions[j] - 1;
						break;
					}
				}	
				if( j == -1 ) sum += positions[i] - 1;
			}
			else{
				sum += positions[i] - 1;
			}

			if( i != Q - 1 ){
				for( j = i + 1; j < Q; j++ ){
					if( check[j] ) {
						sum += positions[j] - positions[i] - 1;
						break;
					}
				}

				if( j == Q ) sum += P - positions[i];
			}
			else{
				sum += P - positions[i];
			}
			result = start( i, sum + bribe, count + 1 );
			if( min > result ) min = result;
		}
	}

	check[position] = false;

	return min;
}

int main() {
	int countOfTestCases;
	int i;
	ifstream fin( nameOfInput );
	ofstream fout( nameOfOutput );
	
	int j;
	
	fin >> countOfTestCases;

	for( i = 0; i < countOfTestCases; i++ ){
		//input
		{
			fin >> P >> Q;
			for( j = 0; j < Q; j++ )
				fin >> positions[j];
		}

		cout << "Case #" << i + 1 << ": ";
		//process
		{
			memset( ( void * )check, false, sizeof( bool ) * MaxOfQ );
			int result;
			minOfProgram = MaxOfMin;

			for( j = 0; j < Q; j++ ){
				result = start( j, P - 1, 1 );
				if( result < minOfProgram ) minOfProgram = result;
				//cout << result << ' ';
			}

			cout << minOfProgram << endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}



void sort( int *data, const int size ){
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