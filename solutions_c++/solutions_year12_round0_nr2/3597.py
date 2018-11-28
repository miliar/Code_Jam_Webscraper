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
	
	
	for ( int i = 0 ; i < nTest ; i++ ) {
		
		outf << "Case #" << (i+1)<< ": ";
		
		unsigned int ja = 0;
		unsigned int ev = 0;
		unsigned int anz;
		unsigned int p;
		unsigned int s;
		unsigned int k;
		
		inf >> anz;
		inf >> s;
		inf >> p;
		
		for ( unsigned int j = 0 ; j < anz ; j++ ) {
			inf >> k;
			
			if ( k % 3 == 0 ) {
				if ( k/3 >= p ) ja++;
				else if ( k/3 + 1 >= p && k != 0) ev++;
				}
			else if ( k % 3 == 2 ) {
				if ( (k+1)/3 >= p ) ja++;
				else if ( (k+1)/3 + 1 >= p ) ev++; 
			}
			else {
				if ( (k+2)/3 >= p ) ja++;
			}
		}
		
		if( s <= ev ) outf << ja + s;
		else outf << ja + ev;
		
		outf << "\n";
	}
    
    return 0;
}

