// Speaking in Tongues 2012/04/14 (Sat) Google Code Jam

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <map>


using namespace std;

/*
INPUT
4
3 1 5 15 13 11   (number of scores, surprizing count, at-least num)
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
 */

int main( int argc, char* argv[] )
{
    if( argc != 2 )
    {
        cout << "Usage: exe <input>" << endl;
        return -1;
    }

    ifstream fin;
    ofstream fout;

    fin.open( argv[1] );
    fout.open( "output" );


    string buffer;

    getline( fin, buffer );
    if( fin.eof() )
    {
        cerr << "Wrong input at the first line: " << buffer << endl;
        return -1;
    }

    int count = atoi( buffer.c_str() );

    for( int nCase = 1; nCase <= count; nCase++ )
    {
        getline( fin, buffer );
        stringstream ss;

        ss << buffer;   // input data

        int nScore = 0;
        int nSurprise = 0;
        int nAtleast = 0;

        int answer = 0;

        ss >> nScore;
        ss >> nSurprise;
        ss >> nAtleast;

        for( int i = 0; i < nScore; i++ )
        {
            int val = 0;
            int result = 0;
            int remainder = 0;

            ss >> val;

            if( val == 0 )
            {
                result    = 0;
                remainder = -1;
            }
            else
            {
                result      = val / 3;
                remainder   = val % 3;
            }
            
            int normalScore = 0;
            int surpScore = 0;

            switch( remainder )
            {
                case -1:
                    normalScore = 0;
                    surpScore = 0;
                    break;
                case 0:
                    normalScore = result;
                    surpScore = result + 1;
                    break;
                case 1:
                    normalScore = result + 1;
                    surpScore = result + 1;
                    break;
                case 2:
                    normalScore = result + 1;
                    surpScore = result + 2;
                    break;
            }

            if( nAtleast > normalScore )
            {
                if( nSurprise > 0 && nAtleast <= (surpScore))
                {
                    nSurprise--;
                    answer++;
                }
            }
            else
            {
                answer++;
            }
                    
        } // score

        fout << "Case #" << nCase << ": " << answer << endl;
    }

    
    fin.close();
    fout.close();


    return 0;
}
