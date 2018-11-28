
#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

ofstream outfile;
ifstream infile;

void setup()
{
	infile.open( "input.in");
	outfile.open( "output.txt");
}

void cleanup()
{
	infile.close();
	outfile.close();
}

int main()
{
	setup();

	int numberOfPuzzles;
	infile >> numberOfPuzzles;
	char temp[10];
	infile.getline(temp, 10);

	for( int i = 0; i < numberOfPuzzles; i ++)
	{
		// read the sentance
		char message[101];
		infile.getline( message, 101);
		cout << "Case #" << (i+1) << ": ";
		outfile << "Case #" << (i+1) << ": ";
		// for each google letter, output the corresponding english letter
		for( int j = 0; j < 100; j ++)
		{
			if( message[j] == 0)
			{
				// exit
				j = 100000;
			}
			else
			{
#define SWITCHAROO(X,Y) \
	case (X): \
	cout << (Y); \
	outfile << (Y); \
	break;
				switch( message[j])
				{
					SWITCHAROO('a','y')
					SWITCHAROO('b','h')
					SWITCHAROO('c','e')
					SWITCHAROO('d','s')
					SWITCHAROO('e','o')
					SWITCHAROO('f','c')
					SWITCHAROO('g','v')
					SWITCHAROO('h','x')
					SWITCHAROO('i','d')
					SWITCHAROO('j','u')
					SWITCHAROO('k','i')
					SWITCHAROO('l','g')
					SWITCHAROO('m','l')
					SWITCHAROO('n','b')
					SWITCHAROO('o','k')
					SWITCHAROO('p','r')
					SWITCHAROO('q','z')
					SWITCHAROO('r','t')
					SWITCHAROO('s','n')
					SWITCHAROO('t','w')
					SWITCHAROO('u','j')
					SWITCHAROO('v','p')
					SWITCHAROO('w','f')
					SWITCHAROO('x','m')
					SWITCHAROO('y','a')
					SWITCHAROO('z','q')
					// space
					SWITCHAROO(' ',' ')
				}
			}
		}
		cout << endl;
		outfile << endl;
	}

	cleanup();
	system("pause");
}

