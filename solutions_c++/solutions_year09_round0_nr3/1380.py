/*
ID: Zupijs
PROG:
LANG: C++
*/

//{ Includes
#include <iostream>
#include <fstream>
#include <string>
//}

//{ Defines
#define in "C-large.in"
#define out "C-large.out"
//}

using namespace std;

const string PHRASE = "welcome to code jam";
const int MOD = 10000;

int main()
{
	ifstream fin;
	fin.open( in );
	ofstream fout;
	fout.open( out );

	int c, n, i, j;
	string input;
	fin >> n;
	getline ( fin, input );

	for ( c = 1; c <= n; c++ )
	{
        getline ( fin, input );
        int subString[ PHRASE.length() ];
        for ( i = 0; i < PHRASE.length(); i++ )
        {
            subString[i] = 0;
        }
        for ( i = 0; i < input.length(); i++ )
        {
            for ( j = 0; j < PHRASE.length(); j++ )
            {
                if ( input[i] == PHRASE[j] )
                {

                    if ( j > 0 )
                    {
                        subString[j] = ( subString[j-1] + subString[j] ) % MOD ;
                    }
                    else
                    {
                        subString[j] = ( subString[j] + 1 ) % MOD;
                    }
                }
            }
        }
        fout << "Case #" << c << ": ";
        if ( subString[ PHRASE.length() - 1 ] < 10 ) fout << "000" << subString[ PHRASE.length() - 1 ] << endl;
        else if ( subString[ PHRASE.length() - 1 ] < 100 ) fout << "00" << subString[ PHRASE.length() - 1 ] << endl;
        else if ( subString[ PHRASE.length() - 1 ] < 1000 ) fout << "0" << subString[ PHRASE.length() - 1 ] << endl;
        else if ( subString[ PHRASE.length() - 1 ] < 10000 ) fout << subString[ PHRASE.length() - 1 ] << endl;
	}

	fin.close();
	fout.close();

	return 0;
}
