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

struct StructOfDefinition{
	double Number;
	StructOfDefinition(){ Number = 5.23607; }
}Definition;

void sort( int *data, const int size );
void swap( int &a, int &b );

//const char *nameOfInput = "input.txt";
const char *nameOfInput = "A-small-attempt5.in";
const char *nameOfOutput = "output.txt";
const int MaxOfBase = 12;
const int MaxOfString = 1024;
const int MaxOfCount = 90000;

class Base{
public:
	Base( int base_ ){ base = base_; }
	~Base(){}
	void start( int number );
	int convertToBase( int number );
	int convertTo10( int number );
	int go( int number, int depth );
private:
	int base;
};

enum Check { FIRST, CHECKED, YES, NO };
int check[MaxOfBase][MaxOfCount];
int back[MaxOfCount];

int main() {
	int countOfTestCases;
	int i;
	ifstream fin( nameOfInput );
	ofstream fout( nameOfOutput );

	char line[MaxOfString];
	int bases[MaxOfBase];
	char *token;
	int countOfBases;
	int j;
	int result;

	memset( (void *)check, FIRST, sizeof( int ) * MaxOfBase * MaxOfCount );
	for( i = 0; i < MaxOfBase; i++ ){
		int now = i + 2;
		memset( ( void * )back, -1, sizeof( int ) * MaxOfCount );

		for( j = 2; j < MaxOfCount; j++ ){
			Base base( now );
			base.go( j, 0 );
		}
	}

	fin >> countOfTestCases;
	fin.getline( line, MaxOfString, '\n' );

	for( i = 0; i < countOfTestCases; i++ ){
		//input
		{
			fin.getline( line, MaxOfString, '\n' );

			countOfBases = 0;

			token = strtok( line, " " );

			while( true ){
				if( token == NULL ) break;

				bases[countOfBases++] = atoi( token );
				token = strtok( NULL, " " );
			}
		}

		cout << "Case #" << i + 1 << ": ";

		//process
		{
			int j, k;
			int countOfTrue;
			for( j = 2; j < MaxOfCount; j++ ){

				countOfTrue = 0;
				for( k = 0; k < countOfBases; k++ ){
					if( check[bases[k]][j] == YES ) countOfTrue++;	
				}

				if( countOfTrue == countOfBases ){
					result = j;
					break;
				}
			}

			cout << result << endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}

int Base::go( int number, int depth ){
	back[depth] = number;
	if( check[base][number] == YES ){
		for( int i = 0; i <= depth; i++ ){
			check[base][back[i]] = YES;
		}

		return 1;
	}
	else if( check[base][number] == NO ){
		for( int i = 0; i <= depth; i++ ){
			check[base][back[i]] = NO;
		}

		return 1;
	}
	else if( check[base][number] == CHECKED ){
		for( int i = 0; i <= depth; i++ ){
			check[base][back[i]] = NO;
		}

		return 1;
	}
	check[base][number] = CHECKED;

	int sum = 0;
	int value;

	while( true ){
		value = number % base;
		sum += value * value;
		number /= base;

		if( number <= 0 ) break;
	}

	/*
	while( true ){
		sum += ( numberOfThis % 10 ) * ( numberOfThis % 10 );
		numberOfThis /= 10;

		if( numberOfThis <= 0 ) break;
	}
	*/

	if( sum == 1 ){
		for( int i = 0; i <= depth; i++ ){
			check[base][back[i]] = YES;
		}
		return 1;
	}
	//else go( convertToBase( sum ) );
	else go( sum, depth + 1 );
}

int Base::convertToBase( int number ){
	int a = base, b = 1, c = 1;
	int result = 0;

	while( true ){
		result += ( ( number % a ) / b ) * c;

		if( number < a ) break;

		b = a;
		a *= base;
		c *= 10;
	}

	return result;
}

int Base::convertTo10( int number ){
	int result = 0;
	int b = 1;

	while( true ){
		result += ( number % 10 ) * b;
		number /= 10;

		if( number <= 0 ) break;

		b *= base;
	}

	return result;
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