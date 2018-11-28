//
//  main.cpp
//
//  Created by lelaloutre on 14 april 2012.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main (int argc, const char * argv[])
{
    using namespace std;
    
    ifstream inf("Input.dat");
    ofstream outf("Output.dat");
    
    if ( !inf || !outf ) {
        cout << "Argh...\n";
        return 1;
    }

	int nTest;
	inf >> nTest;
	
				
		string text;
		getline( inf, text );

	for ( int i = 0 ; i < nTest ; i++ ) {
		
		outf << "Case #" << (i+1)<< ": ";
		getline( inf, text );

		for ( unsigned long int j = 0 ; j < text.size() ; j++ )	
			{
				if( text[j] == 'y' )
					outf << "a";
				else if( text[j] == 'n' )
					outf << "b";
				else if( text[j] == 'f' )
					outf << "c";
				else if( text[j] == 'i' )
					outf << "d";
				else if( text[j] == 'c' )
					outf << "e";
				else if( text[j] == 'w' )
					outf << "f";
				else if( text[j] == 'l' )
					outf << "g";
				else if( text[j] == 'b' )
					outf << "h";
				else if( text[j] == 'k' )
					outf << "i";
				else if( text[j] == 'u' )
					outf << "j";
				else if( text[j] == 'o' )
					outf << "k";
				else if( text[j] == 'm' )
					outf << "l";
				else if( text[j] == 'x' )
					outf << "m";
				else if( text[j] == 's' )
					outf << "n";
				else if( text[j] == 'e' )
					outf << "o";
				else if( text[j] == 'v' )
					outf << "p";
				else if( text[j] == 'z' )
					outf << "q";
				else if( text[j] == 'p' )
					outf << "r";
				else if( text[j] == 'd' )
					outf << "s";
				else if( text[j] == 'r' )
					outf << "t";
				else if( text[j] == 'j' )
					outf << "u";
				else if( text[j] == 'g' )
					outf << "v";
				else if( text[j] == 't' )
					outf << "w";
				else if( text[j] == 'h' )
					outf << "x";
				else if( text[j] == 'a' )
					outf << "y";
				else if( text[j] == 'q' )
					outf << "z";
				else outf << text[j];
			}
		
		outf << "\n";
	}
    
    return 0;
}

