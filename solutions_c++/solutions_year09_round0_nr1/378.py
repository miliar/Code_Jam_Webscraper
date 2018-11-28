#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

//const char *nameOfFile = "A-small-attempt1.in";
const char *nameOfFile = "A-large.in";

//const char *nameOfFile = "input.txt";
const char *nameOfOutput = "output.txt";
const int MAX_OF_L = 16;
const int MAX_OF_D = 5000;
const int MAX_OF_CHARACTER = 'z' - 'a' + 1;

bool isRight( char *word, char alien[MAX_OF_L][MAX_OF_CHARACTER], const int size[MAX_OF_L], const int L );

int main ( void ){
	int L, D, N;
	int i,j;
	ifstream fin( nameOfFile );
	ofstream fout( nameOfOutput );
	char words[MAX_OF_D][MAX_OF_L];
	char line[MAX_OF_CHARACTER * MAX_OF_CHARACTER + 2 * MAX_OF_CHARACTER + 1];
	char alien[MAX_OF_L][MAX_OF_CHARACTER];
	int size[MAX_OF_L];
	int position;
	int count;

	fin >> L >> D >> N;

	for( i = 0; i < D; i++ ){
		fin >> words[i];
	}

	for( i = 0; i < N; i++ ){
		fin >> line;
		
		position = count = 0;

		for( j = 0; j < strlen( line ); j++ ){
			size[position] = 0;

			if( line[j] == '(' ){
				j++;

				while( true ){
					if( line[j] == ')' ) break;
					
					alien[position][size[position]++] = line[j++];
				}

				alien[position][size[position]] = '\0';
			}
			else{
				size[position] = 1;
				alien[position][0] = line[j];
				alien[position][1] = '\0';
			}

			//cout << alien[position] << endl;
			position++;
		}

		for( j = 0; j < D; j++ ){
			if( isRight( words[j], alien, size, L ) ) count++;
		}

		fout << "Case #" << i + 1 << ": " << count << endl;
	}

	fout.close();
	fin.close();

	return 0;
}

bool isRight( char *word, char alien[MAX_OF_L][MAX_OF_CHARACTER], const int size[MAX_OF_L], const int L ){
	int i, j;
	bool flag;

	for( i = 0; i < L; i++ ){
		//cout << i << ' ' << size[i] << ' ' << alien[i] << endl;
		if( size[i] == 1 ){
			if( word[i] != alien[i][0] ) return false;
		}
		else{
			flag = false;

			for( j = 0; j < size[i]; j++ ){
				if( word[i] == alien[i][j] ) flag = true; 
			}
			if( flag == false ) return false;
		}
	}

	return true;
}