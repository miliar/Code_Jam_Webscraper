#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <vector>
#include <cassert>
#include <limits>
using namespace std;

int main()
{
    ifstream mapFile("googlerese.txt");
    // skip the first line
    mapFile.ignore( std::numeric_limits<int>::max(), '\n' );

    vector<char> googlerize( 26 );
    //now comes the translation result
    for( unsigned int i=0; i < googlerize.size(); i++ )
    {
        char letter;
        mapFile >> letter;
        googlerize[ (letter - 'a') ] = 'a'+i;
    }

    //assert( mapFile.eof() );

    mapFile.close();

    ifstream input("B-large.in");
    ofstream output("output.txt");

    unsigned int N;
    input >> N;
    input.ignore( 1 );
    for( unsigned int i=1; i <= N; i++ )
    {
        string line;
        getline( input, line );

        output << "Case #" << i << ": ";

        for( string::iterator it = line.begin(),
                              end = line.end();
             it != end;
             ++it
             )
        {
            char out = ' ';
            if( *it != ' ')
            {
                out = googlerize[(*it)-'a'];
            }
            output << out;
        }
        output << endl;
    }

    return 0;
}

