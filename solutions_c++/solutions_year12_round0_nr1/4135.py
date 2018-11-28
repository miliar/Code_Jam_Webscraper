#include <iostream>
#include <fstream>

using namespace std;

void process( const int caseNumber, ifstream &inputStream, char *translate );
void print( const int caseNumber, long long int answer );
int getNumber( char *number );

//const char* nameOfInput = "input.txt";
const char* nameOfInput = "A-small-attempt0.in";

char googlerese[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

#define MAX ( 101 )

int main ( void ){
	int i;
	int n;
	ifstream inputStream( nameOfInput );
	char temp[MAX];
	char translate[26];

	inputStream >> n;
	inputStream.getline( temp, MAX );

	for( i = 0; i < n; i++ ){
		process( i, inputStream, translate );
	}

	/*
	for( i = 0; i < 26; i++ ){
		cout << "'";

		if( i == 16 ) cout << "z";
		else if( i == 25 ) cout << "q";
		else cout << translate[i];

		cout << "', ";
	}
	*/
	
	return 0;
}



void process( const int caseNumber, ifstream &inputStream, char *translate ){
	char inputText[MAX];
	char outputText[MAX];
	int i;
	int a;

	inputStream.clear();
	inputStream.getline( inputText, MAX );

	cout << "Case #" << caseNumber + 1 << ": ";

	for( i = 0; i < strlen( inputText ); i++ ){
		if( inputText[i] != ' ' ){
			a = inputText[i] - 'a';
			cout << googlerese[a];
		}
		else cout << ' ';
	}

	cout << endl;
}