//
//  main.cpp
//
//  Created by lelaloutre on 14 april 2012.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>


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
		
		unsigned int ANZ = 0;
		unsigned int A,B;
		
		inf >> A;
		inf >> B;
		
		bool good [B-A] [B-A];
				
		for ( unsigned int j = 0 ; j < B-A ; j++ ) 
			for ( unsigned int k = 0 ; k < B-A ; k++ )
				good[j][k] = false;
				
		for ( unsigned int j = 0 ; j < B-A ; j++ ) {
						
			unsigned int N = A + j;
			unsigned int M;
			string numberN,numberM;			
			
			stringstream ss1 (stringstream::in | stringstream::out);

			ss1 << N;
			numberN = ss1.str();
						
			for ( unsigned int j = 1 ; j < numberN.size() ; j++ ) {
				numberM = numberN.substr(j,numberN.size()) + numberN.substr(0,j);
				
				stringstream ss2 (stringstream::in | stringstream::out);

				ss2 << numberM;
				ss2 >> M;
				
				if ( N < M && M <= B ) {
					good[B-N][N-M] = true;
				}
			}
		}
		
		for ( unsigned int j = 0 ; j < B-A ; j++ )
			for ( unsigned int k = 0 ; k < B-A ; k++ )
				if ( good[j][k] ) ANZ++;
		
		outf << ANZ;
		outf << "\n";
	}
    
    return 0;
}

