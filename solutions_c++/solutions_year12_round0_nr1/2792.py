#include <iostream>
#include <fstream>
#include <string>

#define INPUT_FILE "A-small-attempt0.in"
#define OUTPUT_FILE "A-small-attempt0.out"

using namespace std;

const char arr[] = "yhesocvxduiglbkrztnwjpfmaq";

void main()
{
    ifstream fi( INPUT_FILE, ios::in );
    ofstream fo( OUTPUT_FILE, ios::out );

    int t;
    fi >> t;
    fi.ignore( 1 );

    for ( int i = 1; i <= t; ++i )
    {
        fo << "Case #" << i << ": ";
        string s;
        getline( fi, s );
        for ( int j = 0; j < s.length(); ++j )
            if ( s[j] >= 'a' && s[j] <= 'z' )
                fo << arr[ (int) s[j] - (int) 'a' ];
            else
                fo << s[j];
        fo << endl;
    }

    fi.close();
    fo.close();
}