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
#define in "A-large.in"
#define out "A-small2.out"
//}

using namespace std;

int main()
{
	ifstream fin;
	fin.open( in );
	ofstream fout;
	fout.open( out );

	int i, l, d, n, j, k, w, m, num;
	bool match;
	fin >> l >> d >> n;
	string word[d], message;
	for ( j = 0; j  < d; j++ )
            {
                fin >> word[j];
            }
    for ( i = 1; i <= n; i++ )
    {
            num = 0;
            fin >> message;
            for ( k = 0; k  < d; k++ )
            {
                w = 0;
                m = 0;
                match = true;
                while ( match == true && w < word[k].length() && m < message.length() )
                {
                    if ( word[k][w] == message[m] )
                    {
                        m++;
                        w++;
                    }
                    else if ( message[m] == '(' )
                    {
                        while ( message[m] != word[k][w] )
                        {
                            m++;
                            if ( message[m] == ')' )
                            {
                                match = false;
                                break;
                            }
                        }
                        if ( message[m] == word[k][w] )
                        {
                            w++;
                        }
                        while ( message[m] != ')' )
                        {
                            m++;
                        }
                        m++;
                    }
                    else
                    {
                        match = false;
                        break;
                    }
                }
                if ( match == true ) num++;
            }
            fout << "Case #" << i << ": " << num << endl;
    }

    fin.close();
	fout.close();

	return 0;
}
