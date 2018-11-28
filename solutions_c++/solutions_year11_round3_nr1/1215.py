

/*** This code is supposed to run variable length arrays ***/


#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <cassert>
#include <cmath>
#include <vector>
#include <list>

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
	
	for( int ll = 0; ll < num_cases; ll++ )
	{
	
		cout << "Process case " << ll << endl;
		
		/*** clean case variables and read input ***/
		
		int R, C;
		inputfile >> R >> C;
		cout << R << " " << C << endl;
		
		vector< vector<char> > tiles( R ) ;
		// TEST
		cout << "Read" << endl;
		tiles.resize( R );
		for( int l = 0; l < R; l++ )
		{
			tiles[l].resize(C);
			for( int k = 0; k < C; k++ ) {
				inputfile >> tiles[l][k];
				cout << tiles[l][k];
			}
			cout << endl;
		}
		
		cout << "TEST" << endl;
		for( int l = 0; l < R; l++ )
		{
				for( int k = 0; k < C; k++ ) {
					cout << tiles[l][k];
				}
				cout << endl;
		}
		
		/*** COMPUTE SOLUTION ***/
		
		cout << "COMPUTE " << endl;
		bool dead = false;
		
		for( int l = 0; l < R; l++ ){
			
			for( int k = 0; k < C; k++ ) {
		
				if( tiles[l][k] == '#' ) {
				
					//Replace or die if impossible
					assert( !dead );
					dead |= ( l+1 >= R);
					dead |= ( k+1 >= C);
					if( dead ){
						cout << "DEAD A " << l << " " << k << endl;
						for( int l = 0; l < R; l++ ){
							for( int k = 0; k < C; k++ ) {
								cout << tiles[l][k];
							}
							cout << endl;
						}
						break;
					}
					dead |= ( tiles[l][k] != '#');
					dead |= ( tiles[l][k+1] != '#');
					dead |= ( tiles[l+1][k] != '#');
					dead |= ( tiles[l+1][k+1] != '#');
					if( dead ){
						cout << "DEAD B " << l << " " << k << endl;
						for( int l = 0; l < R; l++ ){
							for( int k = 0; k < C; k++ ) {
								cout << tiles[l][k];
							}
							cout << endl;
						}
						break;
					}
					
					tiles[l][k] = '/';
					tiles[l][k+1] = '\\';
					tiles[l+1][k] = '\\';
					tiles[l+1][k+1] = '/';
					
					k++;
					
					cout << "CHANGE" << endl;
					for( int l = 0; l < R; l++ ){
						for( int k = 0; k < C; k++ ) {
							cout << tiles[l][k];
						}
						cout << endl;
					}
				
				
				}
				
				if( dead ) break;
				
			}
			
			if( dead ) break;
			
		}
		
		cout << "OUTPUT" << endl;
		
		/*** SOLUTION COMPUTED ***/
		
		outputfile << "Case #" << ll+1 << ":" << endl;
		if( dead ) {
			outputfile << "Impossible" << endl;
		} else {
			cout << tiles.size() << endl;
			for( int l = 0; l < R; l++ ){
				cout << tiles[l].size() << endl;
				for( int k = 0; k < C; k++ ) {
					outputfile << tiles[l][k];
				}
				outputfile << endl;
			}
		}
		
		cout << "NEXT" << endl;
	
	}
	
	inputfile.close();
	outputfile.close();
	
	return 0;
	
}


