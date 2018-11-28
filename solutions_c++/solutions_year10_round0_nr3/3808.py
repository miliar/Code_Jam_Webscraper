#include <iostream>
#include <fstream>

using namespace std;

const int MAX_OF_PEOPLE = 1000;
enum Checker { UNCHECKED, CHECKED };

int getNextPosition( int size, int position );
int getPreviousPosition( int size, int position );

int main ( void ){
	int T;
	int R, k, N;
	char *fileOfInput= "C-small-attempt0.in";
	char *fileOfOutput = "output.txt";
	int loopOfCase;
	int loopOfPeople;
	int sizeOfGroup[MAX_OF_PEOPLE];
	int check[MAX_OF_PEOPLE];
	int euro[MAX_OF_PEOPLE];

	ifstream inputStream( fileOfInput );
	ofstream outputFileStream( fileOfOutput );

	ostream *outputStream;
	//outputStream = &cout;
	outputStream = &outputFileStream;

	inputStream >> T;

	for( loopOfCase = 0; loopOfCase < T; loopOfCase++ ){
		// input
		inputStream >> R >> k >> N;
		for( loopOfPeople = 0; loopOfPeople < N; loopOfPeople++ ){
			inputStream >> sizeOfGroup[loopOfPeople];
			check[loopOfPeople] = -1;
		}

		//process
		int count = 0;
		int position = 0;
		int next = 0;
		int total = 0;
		int sum = sizeOfGroup[0];

		while( true ){
			count++;

			// getNext
			while( true ){
				next = getNextPosition( N, next );

				if( sum + sizeOfGroup[next] > k ) break;
				if( next == position ) break;
				
				sum += sizeOfGroup[next];
			}

			position = next;
			total += sum;
			sum = sizeOfGroup[next];

			if( count == R ) break;
		}

		*outputStream << "Case #" << loopOfCase + 1 << ": ";
		*outputStream << total << endl;
		
	}

	return 0;
}

int getNextPosition( int size, int position ){
	if( position + 1 >= size ) return 0;
	else return position + 1;
}

int getPreviousPosition( int size, int position ){
	if( position - 1 < 0 ) return size - 1;
	else return position - 1;
}