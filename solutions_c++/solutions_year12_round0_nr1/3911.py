// Speaking in Tongues 2012/04/14 (Sat) Google Code Jam

#include <iostream>
#include <fstream>
#include <string>
#include <map>

//'a' -> 'y', 'o' -> 'e', 'z' -> 'q'.



using namespace std;

map<char, char> g2t;

void initMapping()
{
    g2t.clear();

    g2t['a'] = 'y';
    g2t['b'] = 'h';
    g2t['c'] = 'e';
    g2t['d'] = 's';
    g2t['e'] = 'o';
    g2t['f'] = 'c';
    g2t['g'] = 'v';
    g2t['h'] = 'x';
    g2t['i'] = 'd';
    g2t['j'] = 'u';
    g2t['k'] = 'i';
    g2t['l'] = 'g';
    g2t['m'] = 'l';
    g2t['n'] = 'b';
    g2t['o'] = 'k';
    g2t['p'] = 'r';
    g2t['q'] = 'z';
    g2t['r'] = 't';
    g2t['s'] = 'n';
    g2t['t'] = 'w';
    g2t['u'] = 'j';
    g2t['v'] = 'p';
    g2t['w'] = 'f';
    g2t['x'] = 'm';
    g2t['y'] = 'a';
    g2t['z'] = 'q';
}

int main( int argc, char* argv[] )
{
    if( argc != 2 )
    {
        cout << "Usage: exe <input>" << endl;
        return -1;
    }

    initMapping();

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

    for( int i = 0; i < count; i++ )
    {
        getline( fin, buffer );

        if( fin.eof() )
            break;

        for( int j = 0; j < buffer.length(); j++ )
        {
            if( buffer[j] >= 'a' && buffer[j] <= 'z' ) 
            {
                buffer[j] = g2t[buffer[j]];
            }
            else if( buffer[j] >= 'A' && buffer[j] <= 'Z' )
            {
                buffer[j] = g2t[(char)(buffer[j] + 32)] - 32;
            }
        }

        fout << "Case #" << (i+1) << ": " << buffer << endl;
    }

    
    fin.close();
    fout.close();


    return 0;
}
