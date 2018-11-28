#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <cstring>

using namespace std;

map<char, char>myTranslator;
void populateTranslator()
{
	myTranslator.insert( pair<char, char>('y', 'a') );
	myTranslator.insert( pair<char, char>('n', 'b') );
	myTranslator.insert( pair<char, char>('f', 'c') );
	myTranslator.insert( pair<char, char>('i', 'd') );
	myTranslator.insert( pair<char, char>('c', 'e') );
	myTranslator.insert( pair<char, char>('w', 'f') );
	myTranslator.insert( pair<char, char>('l', 'g') );
	myTranslator.insert( pair<char, char>('b', 'h') );
	myTranslator.insert( pair<char, char>('k', 'i') );
	myTranslator.insert( pair<char, char>('u', 'j') );
	myTranslator.insert( pair<char, char>('o', 'k') );
	myTranslator.insert( pair<char, char>('m', 'l') );
	myTranslator.insert( pair<char, char>('x', 'm') );
	myTranslator.insert( pair<char, char>('s', 'n') );
	myTranslator.insert( pair<char, char>('e', 'o') );
	myTranslator.insert( pair<char, char>('v', 'p') );
	myTranslator.insert( pair<char, char>('z', 'q') );
	myTranslator.insert( pair<char, char>('p', 'r') );
	myTranslator.insert( pair<char, char>('d', 's') );
	myTranslator.insert( pair<char, char>('r', 't') );
	myTranslator.insert( pair<char, char>('j', 'u') );
	myTranslator.insert( pair<char, char>('g', 'v') );
	myTranslator.insert( pair<char, char>('t', 'w') );
	myTranslator.insert( pair<char, char>('h', 'x') );
	myTranslator.insert( pair<char, char>('a', 'y') );
	myTranslator.insert( pair<char, char>('q', 'z') );

}

string translateString( string str_in );

int main( int argv, char* argc[])
{
	fstream aInFile;
	fstream aOutFile;

	aInFile.open( argc[1], ios::in);
	if( aInFile.is_open() )
	{
		// populate the translator map
		populateTranslator();
		// output file
		aOutFile.open( "output.txt", ios::out );
		int noOfTCs = 0;
		int count = 1;
		aInFile >> noOfTCs;
		string aInString;
		getline( aInFile, aInString );
		while( !aInFile.eof() && noOfTCs > 0)
		{
			string aInString, aConvertedStr;
			getline( aInFile, aInString );
			cout << aInString << endl;
			aConvertedStr = translateString( aInString );
			cout << aConvertedStr << endl << endl;
			aOutFile << "Case #" << count <<": "<< aConvertedStr << endl;
			noOfTCs--;
			count++;
		}
		aOutFile.close();
	}
	aInFile.close();
	return 0;
}

string translateString( string str_in )
{
	int aInStrSize = str_in.size( );
	char* aInStr = new char[ aInStrSize + 1 ];
	strcpy( aInStr, str_in.c_str() );

	string aStr;
	map<char, char>::iterator myMapItr;

	for( int i = 0; i< strlen( aInStr ); i++ )
	{
		char aNextChar = aInStr[ i ];
		if( aNextChar == ' ' )
		{
			aStr += ' ';
		}
		else
		{
			myMapItr = myTranslator.find( aInStr[i] );
			if( myMapItr != myTranslator.end() )
			{
				char aTranslatedChar = myMapItr->second;
				aStr += aTranslatedChar;
			}
		}
	}

	return aStr;
}
