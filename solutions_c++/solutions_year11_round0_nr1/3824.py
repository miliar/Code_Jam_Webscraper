

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


typedef struct {
	char bot;
	int button;
	int index;
} action;

int main( int argc, char** argv )
{

	// Which file has to be processed?
	cout << "Processing " << argv[1] << endl;
	
	ifstream inputfile( argv[1], ios_base::in );
	ofstream outputfile( "outputfile", ios_base::out );
	
	//assert( inputfile.good() );
	
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
	
	int num_actions;
	vector<action> actions;
	
	/*** variables done ***/
	
	//assert( inputfile.good() );
	
	for( int ll = 0; ll < num_cases; ll++ )
	{
	
		cout << "Process case " << ll << endl;
		
		outputfile << "Case #" << ll+1 << ": ";
		
		/*** clean case variables and read input ***/
		inputfile >> num_actions;
		actions.resize(num_actions);
		for( int k = 0; k < num_actions; k++ )
		{
			inputfile >> actions[k].bot >> actions[k].button;
			actions[k].index = k;
		}
		
		list<action> blue, orange;
		int pos_blue = 1, pos_orange = 1;
		
		for( int k = 0; k < num_actions; k++ )
		{
			if( actions[k].bot == 'B' ) {
				blue.push_back( actions[k] );
			} else {
				orange.push_back( actions[k] );
			}
		}
		
		/*** COMPUTE SOLUTION ***/
		
		int solution = 0; //accumulated seconds the robots take to finish
		int next_action = 0;
		
		while( next_action < num_actions )
		{
			
			action ablue = *(blue.begin()) , aorange = *(orange.begin());
			bool rblue = false, rorange = false;
			
			cout << "Blue is at " << pos_blue << ", Orange is at " << pos_orange << endl;
			
			if( blue.size() > 0 ) if( ablue.button < pos_blue ) {
				pos_blue--;
			} else if ( ablue.button > pos_blue ) {
				pos_blue++;
			} else if ( ablue.button == pos_blue && ablue.index == next_action ) {
				rblue = true;
			}
			
			if( orange.size() > 0 ) if( aorange.button < pos_orange ) {
				pos_orange--;
			} else if ( aorange.button > pos_orange ) {
				pos_orange++;
			} else if ( aorange.button == pos_orange && aorange.index == next_action ) {
				rorange = true;
			}
			
			if ( rblue ){ blue.pop_front(); next_action++; }
			if ( rorange ){ orange.pop_front(); next_action++; }
			
			solution++;
			
		}
		
				
		
		cout << "num of actions: " << actions.size() << endl;
		
		
		
		/*** SOLUTION COMPUTED ***/
		
		outputfile << solution << endl;
	
	}
	
	inputfile.close();
	outputfile.close();
	
	return 0;
	
}


