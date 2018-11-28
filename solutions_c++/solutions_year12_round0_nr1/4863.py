/**
 a b c d e f g h i j k l m n o p q r s t u v w x y z
 y h e s o c v x d u i g l b k r z t n w j p f m a q
 **/

#include <iostream>
#include <fstream>

using namespace std;

string translate(const string & text);

typedef unsigned int uint;
typedef unsigned long ulong;

int numCases;
char G[100];

static char mapping[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g',
	'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

string translate(const string & text)
{
	string translated = "";
	for (int i = 0; i < text.length(); i++)
	{
		if (text[i] >= 'a' && text[i] <= 'z')
		{
			translated += mapping[text[i] - 'a'];
		} else
		{
			translated += text[i];
		}
	}
	return translated;
}

int main (int argc, char * const argv[]) 
{
	if ( argc != 2 ) return -1;
	
	ifstream inFile(argv[1]);
	inFile >> numCases;
	string text;
	getline(inFile, text);
	
	for ( int caseIndex = 0; caseIndex < numCases; caseIndex++ )
	{
		cout << "Case #" << caseIndex + 1 << ": ";
		
		getline(inFile, text);
		cout << translate(text) << endl;;
	}
	
	inFile.close();
	return 0;
}
