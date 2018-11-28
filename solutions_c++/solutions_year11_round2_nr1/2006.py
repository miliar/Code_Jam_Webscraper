

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
		
		int num_teams = -1;
		inputfile >> num_teams;
		
		cout << "TEAMS : " << num_teams << endl;
		
		vector< vector<char> > matchmatrix( num_teams, vector<char>(num_teams, '.') );
		
		matchmatrix.resize( num_teams );
		for( int i = 0; i < num_teams; i++ ){
			matchmatrix[i].resize( num_teams);
			for( int j = 0; j < num_teams; j++ ){
				inputfile >> matchmatrix[i][j];
			}
			
		}
			
		
		// Test input
		
		for( int i = 0; i < num_teams; i++ ){
			for( int j = 0; j < num_teams; j++ ){
				cout << matchmatrix[i][j];
			}
			cout << endl;
		}
		
		/*** COMPUTE SOLUTION ***/
		
		
		
		//TODO Berechne nun den Gewinnanteil
		
		cout << "COMPUTE N" << endl;
		
		// Anzahl der spiele
		vector< int > N ( num_teams, 0 );
		for( int i = 0; i < num_teams; i++ )
		{
			N[i] = 0;
			for( int j = 0; j < num_teams; j++ ){
				if( matchmatrix[i][j] == '.' ) {
					continue;
				} else if( matchmatrix[i][j] == '0' ) {
					N[i]++;
				} else if( matchmatrix[i][j] == '1' ) {
					N[i]++;
				}
			}
		}
		
		cout << "COMPUTE WP" << endl;
		// anteil der matches won
		vector< double > WP( num_teams, 0. );
		
		/* Fraction of games won */
		for( int i = 0; i < num_teams; i++ ) {
			int num_wins = 0;
			for( int j = 0; j < num_teams; j++ ) {
				if( matchmatrix[i][j] == '.' ) {
					continue;
				} else if ( matchmatrix[i][j] == '1' ){
					num_wins++;
				} else if ( matchmatrix[i][j] == '0' ) {
					continue;
				} else assert( false );
			}
			
			WP[i] = num_wins / double(N[i]) ;
		}
		
		
		cout << "COmpute OWP tilda" << endl;
		// TODO BERECHNE DEN OWP 	
		
		vector< vector<double> > owptilda( num_teams, vector<double>( 0., num_teams) );
		
		owptilda.resize( num_teams );
		for( int i = 0; i < num_teams; i++ ){
			owptilda[i].resize( num_teams);
			for( int j = 0; j < num_teams; j++ ){
				;
			}	
		}
		
		//TEST
		cout << "TEST" << endl;
		for( int i = 0; i < num_teams; i++ ){
			for( int j = 0; j < num_teams; j++ ){
				cout << owptilda[i][j];
			}
			cout << endl;
		}
		
		cout << "foo" << endl;

		// Compute OWP
		for( int i = 0; i < num_teams; i++ ){
			
			cout << "i : " << i << endl;
			
			for( int j = 0; j < num_teams; j++ ){
			
				if( i == j ) continue;
				
				cout << "j : " << j << endl;
				
				// Compute gewinne von i ohne gegenspieler j
				for( int k = 0; k < num_teams; k++ ){
					cout << "k : " << k << endl;
					if( k == i ){
						continue;
					} else if( matchmatrix[j][k] == '.' ){
						continue;
					} else if( matchmatrix[j][k] == '0' ){
						continue;
					} else if( matchmatrix[j][k] == '1' ){
						owptilda[i][j]++;
					}
					else assert(false);
				}
				cout << "i,j: " << i << " " << j << endl;
				assert( N[j] >= 2 );
				owptilda[i][j] /= (double)( N[j] - 1);
			}
		}
		
		cout << "COMPUTE OWP" << endl;
		vector< double > OWP( num_teams, 0. );
		
		for( int i = 0; i < num_teams; i++ ) {
			for( int j = 0; j < num_teams; j++ ) {
				if( matchmatrix[i][j] == '.' ) continue;
				OWP[i] += owptilda[i][j];
			}
			OWP[i] /= N[i];
		}
		
		
		cout << "Compute OOWP" << endl;
		// Compute average OWP i.e. OOWP
		
		vector< double > OOWP( num_teams, 0. );
		
		for( int i = 0; i < num_teams; i++ ) {
			OOWP[i] = 0;
			for( int j = 0; j < num_teams; j++ ) {
				if( matchmatrix[i][j] == '.' ) continue;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= N[i];
		}
		
		vector<double> MPI( num_teams, 0. );
		
		for( int i = 0; i < num_teams; i++ ) {
			MPI[i] = 0.25 * WP[i]  + 0.5 * OWP[i] + 0.25 * OOWP[i];
		}
		
		
		cout << "OUTPUT" << endl;
		/*** SOLUTION COMPUTED ***/
		
		outputfile << "Case #" << ll+1 << ":" << endl;
		
		for( int i = 0; i < num_teams; i++ ) {
			outputfile << MPI[i] << endl;
		}
	
	}
	
	inputfile.close();
	outputfile.close();
	
	return 0;
	
}


