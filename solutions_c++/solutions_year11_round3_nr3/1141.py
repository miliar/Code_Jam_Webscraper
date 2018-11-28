

/*** This code is supposed to run variable length arrays ***/


#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <cassert>
#include <cmath>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;





int main( int argc, char** argv )
{

	// Which file has to be processed?
	cout << "Processing " << argv[1] << endl;
	
	ifstream inputfile( argv[1], ios_base::in );
	ofstream outputfile( "outputfile", ios_base::out );
	
	assert( inputfile.good() );
	
	// How many cases to treat
	int num_cases;
	inputfile >> num_cases;
	cout << num_cases << endl;
	
	// Check whether this suffices in any case
	const int LINEMAX = 2001;
	
	char dummy[ LINEMAX ];
	
	// Skip the rest of the first line, which is empty anyway
	inputfile.getline( dummy, LINEMAX );
	
	/*** Init variables for each case ***/
	
	/*** variables done ***/
	
	assert( inputfile.good() );
	
	;
	
	for( int ll = 0; ll < num_cases; ll++ )
	{
	
		cout << "Process case " << ll << endl;
		
		
		/*** clean case variables and read input ***/
		
		int N, L, H;
		inputfile >> N >> L >> H;
		
		vector<unsigned long> note( N );
		for( int i = 0; i < N; i++ ) inputfile >> note[i];
		
		/*** COMPUTE SOLUTION ***/
		
		// Brute force attack
		
		bool found = false;
		unsigned long freq = 1;
		
		for( freq = L; freq <= H; freq++ ) {
		
			bool col = false;
			for( int b = 0; b < note.size(); b++ ) {
				
				if( freq <= note[b] ){
				
					if( ( note[b] % freq ) != 0 ) col = true;
					
				}else{
					
					if( ( freq % note[b] ) != 0 ) col = true;
					
				}
				
			}
			
			if( col == true ) {
				continue;
			} else { // next freq
				found = true;
				break;
			}
			
		}
		
		/*** SOLUTION COMPUTED ***/
		outputfile << "Case #" << ll+1 << ": ";
		if( !found ) {
			outputfile << "NO";
		} else {
			outputfile << freq;
		}
		outputfile << endl;
	}
	
	inputfile.close();
	outputfile.close();
	
	return 0;
	
}


